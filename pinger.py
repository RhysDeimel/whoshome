import data
import shelve
import subprocess
import datetime

user_list = ['kristen', 'rhys']

''' # trash this
def get_device_ip_list():
    ip_list = []
    with shelve.open('userdb') as db:
        for user in user_list: # loop through users
            for device in db['users'][user]['device'].keys():
                ip_list.append(db['users'][user]['device'][device]['ip'])

    return ip_list
'''

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
    return td.days, td.seconds//3600, (td.seconds//60)%60



def runner():

    with shelve.open('userdb', writeback=True) as db:
        for user in db['users'].keys(): # loop users
            for ip_add in db['users'][user]['ip'].keys(): # loop ips
                db['users'][user]['ip'][ip_add]['online'] = ping(ip_add)

                if db['users'][user]['ip'][ip_add]['online'] == True:
                    db['users'][user]['ip'][ip_add]['seen'][0] = datetime.datetime.now()
                else:
                    date1 = db['users'][user]['ip'][ip_add]['seen'][0]
                    date2 = datetime.datetime.now()
                    td = date2 - date1
                    print(td)
                    td = days_hours_minutes(td)
                    device = db['users'][user]['ip'][ip_add]['device']
                    db['users'][user]['ip'][ip_add]['seen'][1] = "{}'s {} last seen {} days, {} hours, and {} minutes ago".format(user.title(), device, td[0], td[1], td[2])
                    print(db['users'][user]['ip'][ip_add]['seen'][1])




'''

populate jinja
move file

'''

















"""
prefix = '192.168.1.'
online = []


for num in range(100, 151):
    ip = prefix + str(num)
    if ping(ip) == True:
        online.append(ip)

print(online)
"""