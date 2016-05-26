# 7. Given a string, compute recursively (no loops) a new string where all the
# lowercase 'x' chars have been changed to 'y' chars.

def x_to_y(strng=None):
	char_list = list(strng)
	if 'x' in char_list:
		x_position = char_list.index('x')
		char_list[x_position] = 'y'
		return x_to_y(''.join(char_list))
	return strng



print(x_to_y('xXhello'))