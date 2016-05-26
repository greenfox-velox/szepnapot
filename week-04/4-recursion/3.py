
# 3. Given a non-negative int n,
# return the sum of its digits recursively (no loops).
# Note that mod (%) by 10 yields the rightmost digit (126 % 10 is 6),
# while divide (/) by 10 removes the rightmost digit (126 / 10 is 12).


def digit_count(n):
	if n < 10:
		return n
	digit = n % 10
	return digit + digit_count(n // 10)


print(digit_count(526))

