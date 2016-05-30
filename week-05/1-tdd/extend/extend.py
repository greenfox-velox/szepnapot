
# Adds a and b, returns as result
def add(a, b):
	if type(a) != int or type(b) != int:
		return False
	return a + b

# Returns the highest value from the three given params
def max_of_three(a, b, c):
	values = [a, b, c]
	highest = 0
	for i in values:
		if type(i) == str or len(values) == 0:
			return False
		elif i > highest:
			highest = i
	return highest


# Returns the median value of a list given as param
def median(pool):
	sortedLst = sorted(pool)
	lstLen = len(pool)
	index = (lstLen - 1) // 2

	if lstLen < 1:
		return False
	elif (lstLen % 2):
		return sortedLst[index]
	else:
		return (sortedLst[index] + sortedLst[index + 1]) / 2.0

# Returns true if the param is a vovel
def is_vovel(char):
	return char in 'aáeéiíoöüűőuúó'

# Create a method that translates hungarian into the teve language
def translate(hungarian):
	teve = ''
	if type(hungarian) != str:
		return False
	for char in hungarian:
		if is_vovel(char):
			teve += (char+'v'+char)
		elif char.isdigit():
			return False
		elif not is_vovel(char):
			teve += char
	return teve
