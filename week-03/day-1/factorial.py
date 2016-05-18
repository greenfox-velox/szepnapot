def factorial(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return n * factorial(n - 1)

def factInput():
	n = int(input("Enter which factor you're interested in: "))
	print(str(n) + "! =", factorial(n))

factInput()