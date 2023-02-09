# Recursions
# import sys
# print(sys.getrecursionlimit())


# def increment(num):
#     print(num, end=' ')
#
#     increment(num + 1)
#
#     return
#
#
# print(increment(1))  #runs into error when/before the recursion limit is exceeded

#
# def decrement(num):  #decrement function using a while loop
#
#     while num > 0:
#         print(num)
#         num = num - 1
#
#
# print(decrement(10))


# def decrement(num):  # decrement function using recursion function
#
#     if num == 0:
#         return
#
#     print(num)
#     decrement(num - 1)
#
#
# print(decrement(10))
#
#
# def recursive_sum(num):
#     if num == 0:
#         return 0
#     result = num + recursive_sum(num - 1)
#     return result
#
#
# print(recursive_sum(5))
#
#
# def factorial(number):
#     if number < 0:
#         print('Sorry, factorial does not exist for negative numbers')
#         return
#     if number == 0:
#         return 1
#     return number * factorial(number - 1)
#
#
# print(factorial(5))

#
# def fibonacci(number, fib_series):
#     if number < 2:
#         return
#
#     length = len(fib_series)
#
#     new_number = fib_series[length - 1] + fib_series[length - 2]
#
#     fib_series.append(new_number)
#     print('Series so far', fib_series)
#     fibonacci(number - 1, fib_series)
#
#
# series = [0, 1]
# print(fibonacci(10, series))


# def generator():
#     n = 1
#     print('One!')
#     yield n
#
#     n += 1
#     print('Two!')
#     yield n
#
#     n += 1
#     print('Three!')
#     yield n
#
#     n += 1
#     print('Four')
#     yield n
#
#
# g = generator()
#
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
#
# g = generator()
# print(next(g))

# def generate_even_number(limit):
#     for i in range (0, limit, 2):
#         yield i
#
#
# g = generate_even_number(7)
#
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
#
# g = generate_even_number(7)
# l = list(g)
#
# print(l)


def generate_squares(limit):
    for i in range(0, limit):
        yield i**2


gen = generate_squares(10)

squares_list = list(gen)
print(squares_list)
squares_tuple = tuple(generate_squares(10))
print(squares_tuple)
