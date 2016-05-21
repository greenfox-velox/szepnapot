def check_palindrome(word):
	if word == word[::-1]:
		return True
	return False


def check_in_word(word):
	left = 0
	right = len(word)

	while left < right - 1:
		temp = word[left:right]
		right -= 1

		if check_palindrome(temp):
			results.append(temp)
		if right < left + 3:
			left += 1
			right = len(word)


def palindrome_in_words(long_string):
	words = long_string.split(' ')
	check_in_word(long_string)
	for word in words:
		check_in_word(word)
	print(list(set(results)))

results = []

palindrome_in_words('mom and dad sit in a kayak')