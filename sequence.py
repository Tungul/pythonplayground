import sys

NUMBER = int(sys.argv[1])

while NUMBER != 1:
    print(NUMBER)
    if NUMBER % 2 == 0:
        NUMBER = NUMBER / 2
    else:
        NUMBER = NUMBER * 3
        NUMBER = NUMBER + 1
