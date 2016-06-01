# create a function that takes a number and divides ten with it and prints the result
# it should print "fail" if it is divided by 0


def divider(n):
	try:
		return 10 / n
	except ZeroDivisionError:
		return "fail"


print(divider(5))