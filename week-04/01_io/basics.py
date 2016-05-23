# 1. Create a method that reads all contents of a file when its name given as param
def readfile(file_name):
		with open(file_name) as f:
			return f.read()

# 2. Create a method that gets a file_name and a number as param and reads the numberth line of the file
def readline(file_name, number):
		with open(file_name) as f:
			for i, line in enumerate(f):
				line = line.rstrip()
				if i == number-1:
					return line

# 3. Create a method that gets a long sentence as param and gives back the contained words in a list
def words(sentence):
	import re
	word = re.sub(r'\W+', ' ', sentence)
	return word.split()

# 4. Create a method that gets a list of words and creates a sentence with the words separated by spaces
def sentence(words):
	return ' '.join(words) + '.'

# 5. Create a method that gets a string and gives back the character codes in a list
def char_codes(string):
	codes = []
	for code in string:
		codes.append(ord(code))
	return codes

# 6. Create a method that gets a list of integers and gives back a string which characters are created from the numbers used as character codes
def string(char_codes):
	strings = ''
	for codes in char_codes:
		strings += chr(codes)
	return strings