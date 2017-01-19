import subprocess

sausage = subprocess.Popen(["arp-scan", "-l"], stdout=subprocess.PIPE,
	universal_newlines=False
	)

test = sausage.stdout

for line in test:
	print(line)

print("="*10)

print(test.readline())