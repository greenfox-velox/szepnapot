def add(n, m):
	return n + m

def substract(n, m):
	return n - m

def divide(n, m):
	return n / m

def multiply(n, m):
	return n * m

def menu():
	option = input("(A)dd, (S)ubstract, (D)ivide or (M)ultiply? ").upper()
	other_num = int(input("Enter the other number: "))
	return (option,other_num)

def firstnum():
	while True:
		num = input("Enter a number: ")
		try:
			startnum = int(num)
			return startnum
		except ValueError:
			print("{} is not a valid number").format(num)
			continue

while True:
	number2 = firstnum()
	choose = menu()

	if choose[0] == 'S':
		print(substract(number2, choose[1]))

	if choose[0] == 'A':
		print(add(number2, choose[1]))

	if choose[0] == 'D':
		print(divide(number2, choose[1]))

	if choose[0] == 'M':
		print(multiply(number2, choose[1]))

	q = input("QUIT? (y/N)").lower()
	if q == 'y':
		break
	else:
		continue
