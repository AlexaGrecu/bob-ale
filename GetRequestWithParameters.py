import requests

import webbrowser


url = 'https://www.wikipedia.org/'
resp_obj = requests.get(url)
print(resp_obj.url)
webbrowser.open(resp_obj.url)

search_term = input("Enter the term you need to search: ")
print(search_term)

URL = 'https://youtube.com/search'
PARAMS = {'q':search_term}
r_get = requests.get(url = URL, params = PARAMS)
print(r_get.status_code)
print(r_get.url)
webbrowser.open(r_get.url)