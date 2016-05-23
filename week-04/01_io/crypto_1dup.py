def decrypt(file_name):
	duplicate_text = []
	decrypted = []
	count = 0
	with open(file_name) as f:
		for line in f:
			for c in line:
				duplicate_text.append(c)
				while count < len(duplicate_text):
					if count % 2 == 0:
						decrypted.append(duplicate_text[count])
					elif duplicate_text[count] == '\n':
						decrypted.append(duplicate_text[count])
					count += 1
	return ''.join(decrypted)






