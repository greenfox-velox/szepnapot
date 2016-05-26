
# 8. Given a string, compute recursively a new string where all the 'x' chars have been removed.

def x_remove(strng=None):
	char_list = list(strng)
	if 'x' in char_list:
		return x_remove(''.join(remove_string('x', char_list)))
	elif 'X' in char_list:
		return x_remove(''.join(remove_string('X', char_list)))
	return strng

def remove_string(strng, lista):
	lista.remove(strng)
	return lista


print(x_remove('xXhello'))