import shelve

users = {
    'rhys': {
        'device': {
            'desktop': {
                'ip': '192.168.1.150',
                'mac': 'e0:cb:4e:79:8a:5e',
                'online': True,
                'seen': ''
            },
            'laptop': {
                'ip': '192.168.1.111',
                'mac': '78:0c:b8:86:d5:e4',
                'online': False,
                'seen': ''
            },
            'phone': {
                'ip': '192.168.1.105',
                'mac': '50:2e:5c:ca:16:1c',
                'online': False,
                'seen': ''
            }
        }
    },
    'kristen': {
        'device': {
            'iPad': {
                'ip': '192.168.1.106',
                'mac': '70:a2:b3:d9:dc:6b',
                'online': False,
                'seen': ''
            }
        }
    },
    'sahar': {
        'device': {}
    },
    'marc': {
        'device': {}
    },
}

def update():
    with shelve.open('userdb') as db:
        db['users'] = users