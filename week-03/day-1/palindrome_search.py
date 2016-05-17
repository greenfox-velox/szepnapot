def search(words):
	for word in words:
		if word != word[::-1]:
			words.remove(word)
	print(words)

w = input("Enter words separated by space: ")

word_list = w.split()

search(word_list)