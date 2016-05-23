from translate import Translator

text = "Shit"
languages = []

with open('languages.txt') as langs:
	for line in langs:
		line = line.replace('\n', '').replace('\t', ' ')
		languages.append(line)

count = 0
for i in languages:
	print(i, end=' ,')
	count += 1
	if count == 8:
		print("\n")
		count = 0


while True:
	lang = input("\n\nEnter language prefix >>: ")
	translator = Translator(to_lang=lang)
	translation = translator.translate(text)
	print(translation)

