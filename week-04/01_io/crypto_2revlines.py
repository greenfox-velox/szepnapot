# Create a method that decrypts texts/reversed_zen_lines.txt
def decrypt(file_name):
	lines = []
	with open(file_name) as f:
		for line in f:
			line = line.rstrip()
			lines.append(line[::-1] + '\n')
	return ''.join(lines)

