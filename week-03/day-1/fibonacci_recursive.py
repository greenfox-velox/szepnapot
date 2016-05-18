def fibo(n):
	if n == 0:
		return 0
	elif n <= 1:
		return 1
	else:
		return (fibo(n - 1) + fibo(n - 2))

'''
nums = int(input("How long series you want?: "))

for i in range(nums):
	print(fibo(i))
'''

print(fibo(100))