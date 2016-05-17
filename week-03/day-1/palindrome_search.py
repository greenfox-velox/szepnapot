w = input("Enter words separated by space: ")

word_list = w.split()

def search(words):
	for word in words:
		if word != word[::-1]:
			words.remove(word)
	print(words)

search(word_list)