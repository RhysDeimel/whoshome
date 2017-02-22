import subprocess

subprocess.call('arp-scan', '192.168.1.100-192.168.1.199', '>', 'test.txt')
