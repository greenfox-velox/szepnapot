# Create a method that decrypts texts/reversed_zen_order.txt
def decrypt(file_name):
	lines = []
	with open(file_name) as f:
		for line in f:
			if len(lines) > 0:
				lines.insert(0, line)
			else:
				lines.append(line)
	return ''.join(lines)

