import sys

for line in sys.stdin:
	line = line.strip()
	if "Dec" in line:
		line = line.split(" ")
		newline = []
		for item in line:
			if item != '':
				newline.append(item)

		print(str(newline[6]) + "\t" + str(newline[-1]))
