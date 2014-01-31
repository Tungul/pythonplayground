import sys

num = int(sys.argv[1])

while num != 1:
	print(num)
	if num % 2 == 0:
		num = num / 2
	else:
		num = num * 3
		num = num + 1
