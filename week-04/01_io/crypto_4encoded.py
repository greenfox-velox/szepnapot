# Create a method that decrypts texts/encoded_zen_lines.txt
def decrypt(file_name):
	decrypted = []
	with open(file_name) as f:
		for line in f:
			for c in line:
				if c == '\n' or c == ' ':
					decrypted.append(c)
				else:
					new_c = ord(c) - 1
					decrypted.append(chr(new_c))
	return ''.join(decrypted)