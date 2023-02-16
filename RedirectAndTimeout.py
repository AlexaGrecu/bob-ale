import requests
from pprint import pprint
response = requests.get('https://gmail.com')
print(response.history)  # shows redirects
print(response.status_code)
print(response.url)
if response.history:
    print('Redirect history:')
    for resp in response.history:
        print(resp.status_code, resp.url)

    print('\nFinal destination:')
    print(response.status_code, response.url)

else:
    print('Request was not redirected')


print(response.is_redirect)
print(response.is_permanent_redirect)
print(response.history[0].is_redirect)

response = requests.get('https://google.com', allow_redirects=False)  # False is the default, no need to be mentioned
print(response.status_code)
print(response.history)
resp_head = requests.head('https://google.com', allow_redirects=True)
print(resp_head.status_code)

# print(requests.get('https://github.com', timeout=0.001))
print(requests.get('https://github.com', timeout=(5, 18)))
print(requests.get('https://github.com', timeout=None))
