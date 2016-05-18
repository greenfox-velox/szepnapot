import requests

r = requests.get('https://primes.utm.edu/lists/small/10000.txt',verify=False)

print(r.text)
