import requests
import re

from bs4 import BeautifulSoup



r = requests.get('http://pocketcultures.com/2008/10/30/say-hello-in-20-languages/')

raw_html = r.text

soup = BeautifulSoup(raw_html, 'html.parser')
strongs = soup("strong")

GREETINGS = {}
hellos = r'\d+\.\s([A-Z]+)'
language = r'\d+.+\–\s([A-Za-z]+)'

for i in strongs:
	if i.text[0].isdigit():
		GREETINGS = {((re.search(hellos, i.text).group(0))):((re.search(language, i.text).group(0)))}
	else:
		continue
	print(GREETINGS)






