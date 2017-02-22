#import subprocess
import os
import shutil
#from html_vars import html_start, time, html_dynamic, html_end


#subprocess.call('arp-scan 192.168.1.100-192.168.1.199 > test', shell="True")

#MAC = {'70:a2:b3:d9:dc:6b': "Kristen's iPad",
#       '50:2e:5c:ca:16:1c': "Rhys' Phone",
#       '70:70:0d:f3:1f:d3': "Marc's iPhone",
#       '34:f3:9a:47:aa:27': "Kristen's Laptop",
#       'e0:cb:4e:79:8a:5e': "Rhys' Computer",
#        }


#with open('test', 'r') as infile, open('index.html', 'w') as outfile:

#    for el in infile.readlines():
#        for k,v in MAC.items():
#            if k in el:
#                html_dynamic += '\t<li>{} is home</li>\n'.format(v)

#    outfile.write(html_start + time + html_dynamic + html_end)

try:
    target = os.path.join('/usr','share','nginx','www','whoshome','index.html')
    print('Moving {} to {}'.format('index.html', target))
    shutil.copyfile('index.html', target)
except Exception as e:
    print('failed')
    print(e)