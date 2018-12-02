from urllib.request import urlopen

data = urlopen("https://s3-eu-west-1.amazonaws.com/knowit-julekalender-2018/input-vekksort.txt")

prev = 0
s = 0

for line in data:
	num = int(line)
	if num >= prev:
		s += num
		prev = num

print(s)
