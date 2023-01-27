#1
my_list = [1, 2, 3, 4, 5, 6]
cube_list =[]
for i in my_list:
    cube_list.append(i**3)
print (cube_list)
#
#
#2
car_nested_list = [['Volkswagen','Mercedes', 'BMW'], ['Honda', 'Toyota', 'Mazda']]
car_list_unnested = []
for car_list in car_nested_list:
    for car in car_list:
        car_list_unnested.append(car)
print(car_list_unnested)
#
#
#3
for i in range(2000,3000):
    if i%4 ==0:
        print (i, "is a leap year")
    else: print(i, "is not a leap year")
