#Python Requests


from pprint import pprint

import requests
import json

pprint(requests.__version__)
pprint(requests.__copyright__)

r_get = requests.get('https://swapi.dev/api/planets/3')
print(r_get.status_code)
print(type(r_get))
print(type(r_get.headers))
pprint(r_get.headers)

data = json.loads(r_get.text)
pprint(data)
print(r_get.is_redirect)

r_get = requests.get('https://swapi.dev/api/people/9')
print(r_get.status_code)  # successful request
print(r_get.text)

dir(r_get)