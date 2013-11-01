import threading

target = 1000

toWrite = []
output = open('primes.txt', 'w')

class WriteOutPrimes(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)

	def run(self):
		while True:
			try:
				value = toWrite.pop(0)
				if value != None and value != 'Done':
					output.write(str(value) + '\n')
				elif value == 'Done':
					print 'Thread done, dying...'
					break
			except IndexError:
				continue

source = []
primes = []

outputThread = WriteOutPrimes()
outputThread.start()

for i in range(1, target + 1):
	source.append(1)

for i in range(2, target):
	try:
		if source[i] == 1:
			toWrite.append(i)
			primes.append(i)
			for j in range(i+i, target, i):
				try:
					source[j] = 0
				except IndexError:
					print 'Index Error in all-loop', str(i), str(j)
					continue
	except:
		print 'Error at main loop', str(i)
	if i == (target / 2):
		print 'Halfway there in calculations...'

toWrite.append('Done')
print 'killing child thread, awaiting join'
outputThread.join(5) # Wait 5 seconds for thread to be done, then proceed anyway.
output.close()
print 'closing file object'

for i in range(1, len(primes), 5):
	try:
		print "PRIME:", primes[i], primes[i+1], primes[i+2], primes[i+3], primes[i+4]
	except:
		continue

print 'program closing'
quit()