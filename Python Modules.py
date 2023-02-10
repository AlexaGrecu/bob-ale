# print(help('modules'))

import math
import os
# from os import path
import datetime

print('Pi = ', math.pi)
print(os.getcwd())
print(os.environ)

# user = os.environ['\Users\']
# print(user)
# path = os.environ['Path']
# print('Path: ', path)


# # print(os.mkdir('./my_temp_dir'))
# print(os.listdir())
# print(path.isdir('./my_temp_dir'))

print(datetime.date.today())
print(datetime.datetime.now())


def area_circle_fn(radius):
    return math.pi * radius * radius


def perimeter_circle_fn(radius):
    return 2 * math.pi * radius


def diameter_circle_fn(radius):
    return 2 * radius


# def calculate_for_circle(radius, fn):
#     return fn(radius)

# print(calculate_for_circle(10, diameter_circle_fn))
# print(calculate_for_circle(10, perimeter_circle_fn))
# print(calculate_for_circle(10, area_circle_fn))
#
# print(calculate_for_circle(20, diameter_circle_fn))
# print(calculate_for_circle(20, perimeter_circle_fn))
# print(calculate_for_circle(20, area_circle_fn))


def calculate(*args, fn):
    return fn(*args)


print(calculate(10, fn=diameter_circle_fn))
print(calculate(10, fn=perimeter_circle_fn))
print(calculate(10, fn=area_circle_fn))


def area_rectangle_fn(length, breadth):
    return length * breadth


def perimeter_rectangle_fn(length, breadth):
    return 2 * (length + breadth)


print(calculate(20, 40, fn=area_rectangle_fn))
print(calculate(20, 40, fn=perimeter_rectangle_fn))
# print(calculate(10, fn=perimeter_rectangle_fn)) - error, only on arg is specified


# def add(a, b):
#     return a+b
#
#
# def sub(a, b):
#     return a-b
#
#
# def mul(a, b):
#     return a*b
#
#
# def div(a, b):
#     return a/b


# calc_dictionary = {'+': add, '-': 'sub', '*': mul, '/': div}
# func = calc_dictionary['/']
# print(func(12, 4))
# print(calc_dictionary['*'](100, 3))


# Lambda function

add = lambda x, y: x + y
sub = lambda x, y: x - y
mul = lambda x, y: x * y
div = lambda x, y: x / y


def calculate(x, y, operation='add'):  # x and y can be replaced with *args
    if operation == 'add':
        return add(x, y)
    if operation == 'sub':
        return sub(x, y)
    if operation == 'mul':
        return mul(x, y)
    if operation == 'div':
        return div(x, y)


print(calculate(100, 4))  # add is the default operation
print(calculate(100, 4, operation='sub'))
# print(calculate(10, 4, operation=lambda x, y: x**y))
print((lambda x: x + 2)(10))  # define and invoke directly the lambda function
print((lambda x: x * 10)(22))
print((lambda x, y: x ** y)(10, 2))


# def check_if_even(x):
#     assert x % 2 == 0
#
#
# print(check_if_even(5))
#
# even_check_lambda = lambda x : assert x % 2 == 0
# print(even_check_lambda(10))

num_list = [1, 5, 6, 7, 11, 78, 99, 34, 105, 214]
greater_than_10_list = list(filter(lambda x: x > 10, num_list))
print(greater_than_10_list)

even_list = list(filter(lambda x: x % 2 == 0, num_list))
print(even_list)

greater_than_10_less_then_100_list = list(filter(lambda x: x > 10 and x < 100, num_list))
print(greater_than_10_less_then_100_list)
