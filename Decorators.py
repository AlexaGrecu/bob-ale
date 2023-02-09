# import random
import math

#
# def print_message():
#     print('Yoohoo! Decorators are cool!')
#
#
# # def highlight():
# #     annotations = ['-', '*', '+', ':', '^']
# #     annotate = random.choice(annotations)
# #
# #     print(annotate * 50)
# #
# #     print_message()
# #
# #     print(annotate * 50)
# #
# #
# # print(highlight())
#
#
# def print_another_message():
#     print('Did you know decorators use closures?')
#
#
# def make_highlighted(func):
#     annotations = ['-', '*', '+', ':', '^']
#     annotate = random.choice(annotations)
#
#     def highlight():
#         print(annotate * 50)
#
#         func()
#
#         print(annotate * 50)
#
#     return highlight
#
#
# print(print_message())
# print(print_another_message())
# highlight_and_print_message = make_highlighted(print_message)
# print(highlight_and_print_message())
#
#
# @make_highlighted
# def print_a_third_message():
#     print("Now you'll see how decorators are used")
#
#
# print(print_a_third_message())
#
#
# @make_highlighted
# def print_any_message():
#     print("This is an important result that need to be highlighted")
#
#
# print(print_any_message())
#

# def area_circle_fn(radius):
#     return math.pi * radius * radius
#
#
# def perimeter_circle_fn(radius):
#     return 2 * math.pi * radius
#
#
# def diameter_circle_fn(radius):
#     return 2 * radius


# print(area_circle_fn(5))
# print(area_circle_fn(-1))


def safe_calculate(func):
    def calculate(*args):
        for arg in args:
            if arg <= 0:
                raise ValueError("Argument cannot be negative or zero")
        return func(*args)
    return calculate

#
# area_circle_safe = safe_calculate(area_circle_fn)
# print(area_circle_safe(-1))
#
# perimeter_circle_safe =  safe_calculate(perimeter_circle_fn)
# print(perimeter_circle_safe(-1))


@safe_calculate
def area_circle_fn(radius):
    return math.pi * radius * radius


@safe_calculate
def perimeter_circle_fn(radius):
    return 2 * math.pi * radius


# print(perimeter_circle_fn(-3))


@safe_calculate
def area_rectangle_fn(length, breadth):
    return length * breadth


print(area_rectangle_fn(10, 2))
print(area_rectangle_fn(5, -4))