import shelve
import datetime

users = {
    'rhys': {
        'ip': {
            '192.168.1.150': {
                'device': 'desktop',
                'mac': 'e0:cb:4e:79:8a:5e',
                'online': False,
                'seen': [datetime.datetime.strptime('2017-02-26 01:22:09.489923', '%Y-%m-%d %H:%M:%S.%f'), '']
            },
            '192.168.1.149': {
                'device': 'laptop',
                'mac': '78:0c:b8:86:d5:e4',
                'online': False,
                'seen': [datetime.datetime.strptime('2017-02-26 01:22:09.489923', '%Y-%m-%d %H:%M:%S.%f'), '']
            },
            '192.168.1.148': {
                'device': 'phone',
                'mac': '50:2e:5c:ca:16:1c',
                'online': False,
                'seen': [datetime.datetime.strptime('2017-02-26 01:22:09.489923', '%Y-%m-%d %H:%M:%S.%f'), '']
            }
        }
    },
    'kristen': {
        'ip': {
            '192.168.1.106': {
                'device': 'iPad',
                'mac': '70:a2:b3:d9:dc:6b',
                'online': False,
                'seen': [datetime.datetime.strptime('2017-02-26 01:22:09.489923', '%Y-%m-%d %H:%M:%S.%f'), '']
            }
        }
    },
    'sahar': {
        'ip': {
            '192.168.1.114': {
                'device': 'Unknown',
                'mac': '28:37:37:19:9c:de',
                'online': False,
                'seen': [datetime.datetime.strptime('2017-02-26 01:22:09.489923', '%Y-%m-%d %H:%M:%S.%f'), '']
            }
        }
    },
    'marc': {
        'ip': {
            '192.168.1.103': {
                'device': 'iPhone',
                'mac': '70:70:0d:f3:1f:d3',
                'online': False,
                'seen': [datetime.datetime.strptime('2017-02-26 01:22:09.489923', '%Y-%m-%d %H:%M:%S.%f'), '']
            }
        }
    },
}


def update():
    with shelve.open('userdb') as db:
        db['users'] = users
    print('db updated!')
    