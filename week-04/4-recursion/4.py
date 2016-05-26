
# 4. Given base and n that are both 1 or more, compute recursively (no loops)
# the value of base to the n power, so powerN(3, 2) is 9 (3 squared).

def recursive_power(n, p):
	if p == 1:
		return n
	return n * recursive_power(n, p - 1)


print(recursive_power(5, 3))