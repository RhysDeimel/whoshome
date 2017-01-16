import subprocess

sausage = subprocess.Popen(["arp-scan", "-l"], stdout=subprocess.PIPE,
	universal_newlines=True)

test = sausage.stdout

for line in test:
	print(line)