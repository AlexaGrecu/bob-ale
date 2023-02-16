import requests
from pprint import pprint
from PIL import Image  # pip install Pillow to install PIL
from io import BytesIO

resp_obj = requests.get('https://en.wikipedia.org/wiki/Monty_Python')
print(resp_obj.status_code)
print(resp_obj.encoding)
pprint(resp_obj.text)
# print(resp_obj.encoding = 'ISO-8859-1')
print(type(resp_obj.content))

resp = requests.get('https://en.wikipedia.org/wiki/Monty_Python#/media/File:Flyingcircus_2.jpg')
print(resp.status_code)
print(type(resp.content))
# image = Image.open(BytesIO(resp.content))
# print(type(image))
# print(image.save('monty.png'))
# print(image.open('monty.png'))