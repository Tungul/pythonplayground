import threading

toWrite = []
output = open('/storage/emulated/0/primes.txt', 'w')

class WriteOutPrimes(threading.Thread)
	def __init__(self)
		threading.Thread.__init__(self)
	def run(self)
		while True:
			if toWrite[0] != None:
				output.write(str(toWrite.pop(0)) + '\n')
			elif toWrite[0] == 'Done'
				break

source = []
primes = []

outputThread = WriteOutPrimes()
outputThread.start()

for i in range(1, 5000):
	source.append(1)

for i in range(2, len(source)):
	if source[i] == 1:
		toWrite.append(i)
		for j in range(i+i, len(source), i):
			source[j] = 0

outputThread.join()

f.close()