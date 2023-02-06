#Python Requests


from pprint import pprint

import requests
import json

pprint(requests.__version__)
pprint(requests.__copyright__)

r_get = requests.get('https://www.accuweather.com/en/ro/bucharest/287430/daily-weather-forecast/287430')
print(r_get.status_code)
print(type(r_get))
print(type(r_get.headers))
pprint(r_get.headers)

data = json.loads(r_get.text)
pprint(data)
print(r_get.is_redirect)

r_get = requests.get('https://swapi.dev/api/planets/3')
print(r_get.status_code)
print(r_get.text)

dir(r_get)