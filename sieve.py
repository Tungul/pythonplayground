import threading, androidhelper

droid = androidhelper.Android()

target = 1000000

toWrite = []
output = open('/storage/emulated/0/primes.txt', 'w')

class WriteOutPrimes(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
	def run(self):
		while True:
			try:
				value = toWrite.pop(0)
				if value != None and value != 'Done':
					output.write(str(value) + '\n')
#					print value
				elif value == 'Done':
					break
			except:
				continue

source = []
primes = []

outputThread = WriteOutPrimes()
outputThread.start()

for i in range(1, target):
	source.append(1)

for i in range(2, target):
	if source[i] == 1:
		toWrite.append(i)
		for j in range(i+i, target, i):
			source[j] = 0
	if i == (target / 2):
		droid.makeToast('Halfway there.')

toWrite.append('Done')
outputThread.join()

output.close()