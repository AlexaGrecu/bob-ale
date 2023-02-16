import requests
from pprint import pprint
import webbrowser

r_post = requests.post('https://en.wikipedia.org/w/index.php', data={'search': 'Skillsoft'})
print(r_post.status_code)
print(type(r_post))
pprint(r_post.text)

with open('skillsoft.html', 'wb') as f:
    for chunk in r_post.iter_content(chunk_size=10000):
        f.write(chunk)


## url = 'http://httpbin.org/post'
#
# files = {'files': open('test.txt', 'rb')}
# values = {'upload_file': 'test.txt', 'OUT': 'csv'}
#
# print(files)
#
# r_post = requests.post(url, files=files, data=values)
# print(r_post.status_code)

# Post Requests with Multiple Parameters - demo on https://pastebin.com

post_link = 'https://pastebin.com/api/api_post.php'
payload = "{'username': 'john', 'email': 'john@john.com'}"
API_KEY = '068et8c5332427952bd43af129886ca0'
parameters = {'api_dev_key': API_KEY, 'api_option': 'paste', 'api_paste_code': payload, 'api_paste_format': 'python'}
r_post = requests.post(post_link, data=parameters)
if (r_post.status_code == 200):
    print('The request to the url was successful')
    print('You can find the code pasted on this link: {}'.format(r_post.text))

else:
    print('The request was not successful')

