# 1. write a recursive function
# that takes one parameter: n
# and counts down from n

def count_down(n):
	if n == 0:
		return 0
	return count_down(n - 1)

print(count_down(5))