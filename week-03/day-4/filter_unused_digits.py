def unused_digits(*args):
	all_nums = list(range(0, 11))
	arg = ''.join(map(str, list(args)))
	used_digits = list(arg)
	print(used_digits)
	print(all_nums)





unused_digits(12, 34, 56, 788)