
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


def to_arabic(n)
	
to_convert = int(input("Enter arabic number to convert: "))

to_roman(to_convert)