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



def runner():

    with shelve.open('userdb', writeback=True) as db:
        for user in db['users'].keys(): # loop users
            for ip_add in db['users'][user]['ip'].keys(): # loop ips
                db['users'][user]['ip'][ip_add]['online'] = ping(ip_add)

                if db['users'][user]['ip'][ip_add]['online'] == True:
                    db['users'][user]['ip'][ip_add]['seen'] = datetime.datetime.now()
                else:
                    pass
                    # calculate last seen
                    datetime.datetime.strptime('2017-02-26 01:22:09.489923', '%Y-%m-%d %H:%M:%S.%f')





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