from urllib.request import urlopen
import re
import operator

data = urlopen("https://s3-eu-west-1.amazonaws.com/knowit-julekalender-2018/input-rain.txt")

slopes = {}

for line in data:
	line = re.sub("[^0-9,;]", "", str(line))
	n1, n2 = line.split(";")
	
	x1, y1 = map(float, n1.split(","))
	x2, y2 = map(float, n2.split(","))

	slope = (y2 - y1) / (x2 - x1)

	if slope in slopes:
		slopes[slope] += 1
	else:
		slopes[slope] = 1

print(max(slopes.items(), key=operator.itemgetter(1)))
