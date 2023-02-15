# clasa films
# atribut name, metoda get si del

# clasa people, atribute: name, metode get si if  daca este people intr-un anum film

import requests
from pprint import pprint
import json

r_get = requests.get('https://swapi.dev/api/people/',
                        headers={'content-type': 'application/json'}, verify=False)

json_data = r_get.json()
pprint(json_data)
all_data_list = dict(json_data)['results']
print(all_data_list)


class People:
    def __init__(self, name):
        self.__name = name

    def get_name(self, name):
        self.__name = name

        return self.__name

class Films(People):

    def __init__(self, name, film):
        super().__init__(name)
        self.__film = film

    def get_film(self, name, film):
        self.__name = name
        self.__film = film
        return "{} : {}".format(self.__name, self.__film)

    def del_film(self):
        print('delete method called')

        del self.__film


for person_dict in all_data_list:
    character = person_dict['name']
    P = People(character)
    print(P.get_name(character))

for person_dict in all_data_list:
    character = person_dict['name']
    films = person_dict['films']
    F = Films(character, films)
    print(F.get_film(character, films))

print(F.del_film())