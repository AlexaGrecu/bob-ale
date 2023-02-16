import requests
from pprint import pprint
import json

# r_head = requests.head('https://en.wikipedia.org/wiki/Main_Page')
# print(r_head.status_code)
# print(r_head.text)  # doesn't get anything. HEAD requests are used
# # only for knowing information about the site where we want to GET info from
#
# print(r_head.content)  # b'' = blank string
#
# pprint(r_head.headers)
# pprint(r_head.headers['content-length'])
# pprint(r_head.headers['content-type'])

url = 'https://swapi.dev/api/planets/3'
headers = {'user-agent': 'Googlechrome'}
resp = requests.get(url, headers=headers)
print(resp.headers)
print(resp.headers['content-type'])
resp_obj = requests.get('https://en.wikipedia.org/wiki/Monty_Python')
print(resp_obj.headers)
print(resp_obj.request.headers)
r = requests.get('https://en.wikipedia.org/wiki/Monty_Python',
                 headers={'User-agent': 'Internet Explorer/2.0'})
data = r.json()

print(data)
# print(data['user-agent'])