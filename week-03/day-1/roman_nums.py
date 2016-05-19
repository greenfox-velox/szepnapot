
romanList = (('M',  1000),
							('CM', 900),
							('D',  500),
							('CD', 400),
							('C',  100),
							('XC', 90),
							('L',  50),
							('XL', 40),
							('X',  10),
							('IX', 9),
							('V',  5),
							('IV', 4),
							('I',  1))

def to_roman(n):
	if n <= 4:
		print(n * 'I')
	else:
		result = ""

		for roman, decimal in romanList:
			while n >= decimal:
				result += roman
				n -= decimal
		print(result)


def translate(roman):
	letters = []
	decimals = []
	for letter in roman:
		letters.append(letter)
	for k in letters:
		for v in romanList:
			if k == v[0]:
				decimals.append(v[1])
	print(sum(decimals))
	
to_convert = input("Enter arabic number to convert: ")
translate(to_convert.upper())

# to_roman(int(to_convert))