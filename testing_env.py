

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
# print(dir(r_get))

#
json_data = r_get.json()

# print(type(json_data))
pprint(json_data)


my_people_details_list = dict(json_data)['results']
# print(my_people_details_list)

print(len(my_people_details_list))

my_people_with_blue_eyes_list = []

print('The characters with blue eyes are: ')

i = 0
while i < 10:
    if my_people_details_list[i].get('eye_color') == 'blue':
        # print(my_people_details_list[i].get('name'))
        my_people_with_blue_eyes_list.append(my_people_details_list[i].get('name'))
    else:
        pass

    i += 1

# print(my_people_with_blue_eyes_list)

for person in my_people_with_blue_eyes_list:
    print(person)

# for i in range(10):
#     if my_people_details_list[i].get('eye_color') == 'blue':
#         print(my_people_details_list[i].get('name'))
#         my_people_with_blue_eyes_list.append(my_people_details_list[i].get('name'))

# print('The number of characters with blue eyes is: ', )

result_var = f'''There are {len(my_people_with_blue_eyes_list)} people with Blue eyes. '''

print("There are " + str(len(my_people_with_blue_eyes_list)) + " people with Blue eyes.")
print(result_var)
