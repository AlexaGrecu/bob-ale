import requests
from pprint import pprint
import json

resp_obj = requests.get('https://swapi.dev/api/vehicles/4')
print(resp_obj.status_code)
pprint(resp_obj.json())
print(resp_obj.headers['content-type'])
resp = requests.get('https://www.yahoo.com')
print(resp.status_code)
# pprint(resp.json())  # the url above is not a json format
print(resp.headers['content-type'])

resp_obj = requests.get('https://maps.googleapis.com/maps/api/js')
print(resp_obj.status_code)
# print(resp_obj.json()) # the url above is not a json format

resp_obj = requests.get('https://swapi.dev/api/vehicles/4', stream=True)  # doesn't save in memory, streams form the online
print(resp_obj.raw)
print(resp_obj.raw.read(10))

# with requests.get('https://swapi.dev/api/vehicles/4', steam=True) as response:
#     with open('raw_file.txt', wb) as b:
#         for chunk in response.iter_content(1000):
#             b.write(chunk)
#
# print('raw_file.txt')
print(resp_obj.ok)