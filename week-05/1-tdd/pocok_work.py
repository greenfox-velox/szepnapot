def is_anagramm(str1, str2):
	if type(str1) != str or type(str2) != str:
		return False
	elif len(str1) == 0 or len(str2) == 0:
		return False
	return sorted(list(str1.lower())) == sorted(list(str2.lower()))


def letter_count(strng):
	if type(strng) != str:
		return False
	letter_freq = {}
	for word in strng:
		letter_freq[word] = letter_freq.get(word, 0) + 1
	return letter_freq


