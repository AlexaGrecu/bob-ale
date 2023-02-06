

import requests
from pprint import pprint



# get info from URL -- https://requests.readthedocs.io/en/latest/user/quickstart/
r_get = requests.get('https://swapi.dev/api/people/',
                     headers={'content-type': 'application/json'})

# get all people with blue eyes
# 1. access key "results" which is a list
# 2. loop through all people and access key "eye_color"
# 3. print number of people with eye colour blue
# 4. print only people with eye colour "blue"

# get methods for requests GET object
print(dir(r_get))

#
json_data = r_get.json()

pprint(json_data)
print(type(json_data))


people = list(json_data.values())
my_people_details_list=(people[3])
print(my_people_details_list)

print(len(my_people_details_list))
my_people_with_blue_eyes_list=[]
i=0

while i<10:
    if my_people_details_list[i].get('eye_color')=='blue':
        print('The name of the character with blue eyes is: ', my_people_details_list[i].get('name'))
        my_people_with_blue_eyes_list.append(my_people_details_list[i].get('name'))


    else:
        pass

    i+=1
print('The characters with blue eyes are:', my_people_with_blue_eyes_list)
print('The number of people with blue eyes is: ', len(my_people_with_blue_eyes_list))
