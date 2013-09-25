def _bad_fib(x):
	if (x == 0 or x == 1):
		return x
	else:
		return _bad_fib(x - 1) + _bad_fib(x - 2)
 
def bad_fib(x):
	return _bad_fib(x)

print bad_fib(25);