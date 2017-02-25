import shelve
import datetime

users = {
    'rhys': {
        'ip': {
            '192.168.1.150': {
                'device': 'desktop',
                'mac': 'e0:cb:4e:79:8a:5e',
                'online': True,
                'seen': [datetime.datetime.strptime('2017-02-26 01:22:09.489923', '%Y-%m-%d %H:%M:%S.%f'), '']
            },
            '192.168.1.111': {
                'device': 'laptop',
                'mac': '78:0c:b8:86:d5:e4',
                'online': True,
                'seen': [datetime.datetime.strptime('2017-02-26 01:22:09.489923', '%Y-%m-%d %H:%M:%S.%f'), '']
            },
            '192.168.1.105': {
                'device': 'phone',
                'mac': '50:2e:5c:ca:16:1c',
                'online': True,
                'seen': [datetime.datetime.strptime('2017-02-26 01:22:09.489923', '%Y-%m-%d %H:%M:%S.%f'), '']
            }
        }
    },
    'kristen': {
        'ip': {
            '192.168.1.106': {
                'device': 'iPad',
                'mac': '70:a2:b3:d9:dc:6b',
                'online': True,
                'seen': [datetime.datetime.strptime('2017-02-26 01:22:09.489923', '%Y-%m-%d %H:%M:%S.%f'), '']
            }
        }
    },
    'sahar': {
        'ip': {}
    },
    'marc': {
        'ip': {}
    },
}

def update():
    with shelve.open('userdb') as db:
        db['users'] = users
    print('db updated!')