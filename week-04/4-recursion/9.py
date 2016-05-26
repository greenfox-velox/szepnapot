# 9. Given a string, compute recursively a new string where all the
# adjacent chars are now separated by a "*".

def word_separtor(strng=None, position=1):
	char_list = list(strng)
	separator = '*'
	if len(char_list) == position:
		return ''.join(char_list)
	char_list.insert(position, separator)
	return word_separtor(''.join(char_list), position + 2)



print(word_separtor('Helooooooooo'))



