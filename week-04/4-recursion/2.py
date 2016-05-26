# 2. write a recursive function
# that takes one parameter: n
# and adds numbers from 1 to n


def sum_to_n(n):
	if n == 0:
		return 0
	return n + sum_to_n(n - 1)

print(sum_to_n(100))
