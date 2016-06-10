import requests
from pprint import pprint

api_key = "AIzaSyCFo_S__0Lq0FyhpMkhLztLnsGjDT8MWUs"

service_url = "https://maps.googleapis.com/maps/api/geocode/json?"

search = input("Enter location >>: ")

spec = {'key': api_key, 'address': search}

result = requests.get(service_url, params=spec)

pprint(result.json())