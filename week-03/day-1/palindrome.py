def palindrome(word):
	print(word + word[::-1])


word_in = input("Enter a word: ")

palindrome(word_in)