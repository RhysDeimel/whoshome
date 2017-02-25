import data
import shelve
from os import system as system_call

user_list = ['kristen', 'rhys']

def get_device_ip_list():
    ip_list = []
    with shelve.open('userdb') as db:
        for user in user_list: # loop through users
            for device in db['users'][user]['device'].keys():
                ip_list.append(db['users'][user]['device'][device]['ip'])

    return ip_list


def ping(host):
    """
    Returns True if host (str) responds to a ping request.
    Remember that some hosts may not respond to a ping request even if the host name is valid.
    """
    return system_call("ping -c 3 " + " " + host) == 0


def update_device_status(user, device):
    """
    Takes a user and a device (str) and accesses the db.
    Switches online status to Bool opposite.
    """
    with shelve.open('userdb') as db:
        if db['users'][user]['device'][device]['online'] == False:
            return True
        else:
            return False










"""
prefix = '192.168.1.'
online = []


for num in range(100, 151):
    ip = prefix + str(num)
    if ping(ip) == True:
        online.append(ip)

print(online)
"""