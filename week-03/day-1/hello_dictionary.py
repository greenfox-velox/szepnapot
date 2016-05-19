import requests
import re

from bs4 import BeautifulSoup

r = requests.get('http://pocketcultures.com/2008/10/30/say-hello-in-20-languages/')

raw_html = r.text

soup = BeautifulSoup(raw_html, 'html.parser')
strongs = soup("strong")

GREETINGS = {}
hellos = r'\d+\.\s([A-Z]+\s?[A-Z]+.).?'
language = r'\d+.+\–\s([A-Za-z\s()]+)'

for i in strongs:
	i = i.text
	print(i)

	# if i[0].isdigit():
	# 	hello_parts = re.match(hellos, i).group(1)
	# 	# hy = (''.join(hello_parts)).capitalize()
	# 	print(hello_parts)
	# 	# country = re.match(language, i).group(0)
	# 	# print(country)






