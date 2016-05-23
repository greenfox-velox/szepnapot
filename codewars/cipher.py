def encryptor(key, message):
	cipher = ''
	for char in message:
			if char.isalpha():
					cipher_char = ord(char) + key
					if cipher_char > ord('z'):
							cipher_char -= 26
					if cipher_char < ord('a'):
						cipher_char += 26
					cipher += chr(cipher_char)
			else:
					cipher_char = ord(char)
					cipher += chr(cipher_char)
	return cipher



print(encryptor(-5, 'Hello World!'))