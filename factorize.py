import concurrent.futures, decimal
import android
droid = android.Android()
cores = 4

Decimal = decimal.Decimal

def aprint(string):
	print(str(string))

#target = Decimal(17849117530175954689)
target = Decimal(999962000357)

print(target)

def check(n):
	if target % n == 0:
		droid.makeToast("Completed. Target is %s." % n)
		exit(0)

def longCheck(low, high):
	aprint("Beginning calculations.")
	for n in range(int(low), int(high)):
		check(n)
	print("Ending calculations")

def divideAndBegin():
	# divvy up work based on client threads
	numbers = [2]
	for i in range(1, cores + 1):
		num = Decimal((target / cores) * i)
		print(num)
		if "." in str(num):
			print("Normalizing...")
			while num % 1 != 0:
				num = num - Decimal(1 / cores)
			num = num.normalize()
		print(num)
		numbers.append(num)
	
	with concurrent.futures.ThreadPoolExecutor(max_workers=cores) as e:
		for i in range(0,cores):
			lownum = numbers[i]
			highnum = numbers[i + 1]
			aprint("Launching new thread [%s], %s to %s" % (i, lownum, highnum))
			e.submit(longCheck, lownum, highnum)
			

if __name__ == "__main__":
	divideAndBegin()
	print("Nothing found. Is it prime?")