ah = [3, 4, 5, 6, 7]
n = len(ah)
sum = 0

while n > 0:
	sum += ah[n-1]
	n -= 1

print(sum)