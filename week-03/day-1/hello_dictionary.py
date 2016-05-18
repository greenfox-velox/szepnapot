import requests
import regex


r = requests.get('http://www.athropolis.com/hello2.htm')

lang_pattern = r'http://www.travlang.com/languages/([a-z]+)'
hello_pattern = regex.compile(r'<font size=3 color="#ff0000" FACE="arial, helvetica">\n<b>(?:<IMG SRC="language/[a-z]+\s+.gif" BORDER=0 ALIGN="absbottom">)*([A-Za-z\D]+\S*)</b>')

old = '<b>([A-Za-z]+\S*\s*)'

raw_html = r.text
print(raw_html)


langs = regex.findall(lang_pattern, raw_html)
print(langs)
print(len(langs))
hellos = regex.findall(hello_pattern, raw_html)
print(hellos)
print(len(hellos))

GREETINGS = dict(zip(langs, hellos))

# print(GREETINGS)