def unused_digits(*args):
	all_nums = range(10)
	unused = ''
	number = ''.join(str(args))
	for num in all_nums:
		num = str(num)
		if num not in number:
			unused += num
	return str(unused)





unused_digits(12, 34, 56, 788)