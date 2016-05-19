
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


def roman2arabic(roman):
	total = 0
	values = {
		'I': 1,
		'V': 5,
		'X': 10,
		'L': 50,
		'C': 100,
		'D': 500,
		'M': 1000
	}
	prevValue = 0
	for char in roman:
		if values[char] > prevValue:
			total -= prevValue
		else:
			total += prevValue
		prevValue = values[char]
	total += prevValue
	print(total)

def menu(num):
	if num == "r":
		to_convert = int(input("Enter number to convert into ROMAN: "))
		to_roman(to_convert)
	else:
		to_convert = input("Enter roman number to convert into ARABIC: ")
		roman2arabic(to_convert.upper())

while True:
	num = input("Convert to (R)oman or (A)rabic? : ").lower()
	menu(num)