from sys import argv


def memoize(f):
	memo = {}
	def helper(*args):
		if args not in memo:
			memo[args] = f(*args)
		return memo[args]
	return helper


@memoize
def fib(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fib(n - 1) + fib(n - 2)


def iter_fib(n):
	if n == 0:
		return 0
	prev, curr = 0, 1
	for i in range(2, n + 1):
		prev, curr = curr, prev + curr
	return curr


# TODO hmm
def recursive_bott_up_fib(n):
	pass
	

if __name__ == "__main__":
	num = int(argv[1])
	print(fib(num))
