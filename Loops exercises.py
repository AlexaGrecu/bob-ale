# #For loops
# #
# #1
# my_list = [1, 2, 3, 4, 5, 6]
# cube_list =[]
# for i in my_list:
#     cube_list.append(i**3)
# print (cube_list)
# #
# #
# #2
# car_nested_list = [['Volkswagen','Mercedes', 'BMW'], ['Honda', 'Toyota', 'Mazda']]
# car_list_unnested = []
# for car_list in car_nested_list:
#     for car in car_list:
#         car_list_unnested.append(car)
# print(car_list_unnested)
# #
# #
# #3
# for i in range(2000,3000):
#     if i%4 ==0:
#         print (i, "is a leap year")
#     else: print(i, "is not a leap year")
#
# #
# #
# #4
#
# random_list = [124, 148, 173, 231, 256, 301, 315, 361, 399]
#
# for i in random_list:
#     if i==315:
#         break
#     if i%7 == 0:
#         continue
#     print (i, end =" ")
# #
# #
# #5
# #
# #
# list = [2, 3, 6, 7, 8, 11, 12, 13, 17, 18]
#
# cubes_list = [x**3 for x in list if x%3 == 0]
#
# print(cubes_list)
# #
# #While loops
# #6
#
# capital = ""
# while True:
#     capital=input("Please enter the Capital of Egypt")
#
#     if capital == "quit":
#         print ("The correct capital of Egypt is Cairo")
#         break
#     if capital.upper() == "CAIRO":
#         print("That is the correct answer")
#         break
#     else:
#         print("That is not the correct answer. Try again")
