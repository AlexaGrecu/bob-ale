import requests
from pprint import pprint
import json

r_put = requests.put('https://en.wikipedia.org/wiki/Main_Page', data={'key': 'value'})
print(r_put.status_code)
print(type(r_put))
print(r_put.text)

r_option = requests.options('https://en.wikipedia.org/wiki/Main_Page')
print(type(r_option))
pprint(r_option.text)
pprint(r_option.headers)

r_delete = requests.delete('https://en.wikipedia.org/wiki/Main_Page')
print(r_delete.status_code)
print(type(r_delete))
print(r_delete.text)
