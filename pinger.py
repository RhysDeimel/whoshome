#!/usr/bin/python3

import data
import shelve
import subprocess
import datetime
import copy
import os
import shutil
from jinja2 import FileSystemLoader, Environment


def ping(host):
    """
    Returns True if host (str) responds to a ping request.
    Remember that some hosts may not respond to a ping request even if the host name is valid.
    """
    return subprocess.run(['ping', '-c', '3', host]).returncode == 0


def days_hours_minutes(td):
    """
    Takes a timedela and returns a tuple of (days, hours, minutes)
    """
    return td.days, td.seconds//3600, (td.seconds//60) % 60


def move_files():
    for file in ['index.html', 'style.css']:
        try:
            target = os.path.join('/usr', 'share', 'nginx', 'www', 'whoshome', file)
            print('Moving {} to {}'.format(file, target))
            shutil.copyfile(file, target)
        except Exception as e:
            print('failed')
            print(e)


def runner():
    """
    Opens db and updates using ping() and days_hours_minutes()
    """
    try:
        with shelve.open('userdb', writeback=True) as db:
            for user in db['users'].keys():  # loop users
                for ip_add in db['users'][user]['ip'].keys():  # loop ips
                    db['users'][user]['ip'][ip_add]['online'] = ping(ip_add)

                    if db['users'][user]['ip'][ip_add]['online']:
                        db['users'][user]['ip'][ip_add]['seen'][0] = datetime.datetime.now()
                    else:
                        date1 = db['users'][user]['ip'][ip_add]['seen'][0]
                        date2 = datetime.datetime.now()
                        td = date2 - date1
                        td = days_hours_minutes(td)
                        device = db['users'][user]['ip'][ip_add]['device']
                        db['users'][user]['ip'][ip_add]['seen'][1] = "{}'s {} last seen {} days, {} hours, and {} minutes ago".format(user.title(), device, td[0], td[1], td[2])
    except Exception as e:
        print('runner() failed')
        print(e)


def render_from_template(directory, template_name, **kwargs):
    loader = FileSystemLoader(directory)
    env = Environment(loader=loader)
    template = env.get_template(template_name)
    return template.render(**kwargs)


runner()


try:
    with shelve.open('userdb') as db:
        jinja_data = {
            'names': ['kristen', 'marc', 'rhys', 'sahar'],
            'userdb': copy.deepcopy(db['users']),
            'updated': datetime.datetime.now()
        }

    with open('index.html', 'w') as outfile:
        html = render_from_template(".", "index_template.html", **jinja_data)
        outfile.write(html)

    target = os.path.join('/usr', 'share', 'nginx', 'www', 'whoshome', 'index.html')
    print('Moving {} to {}'.format('index.html', target))
    shutil.copyfile('index.html', target)
except Exception as e:
    print('failed')
    print(e)
