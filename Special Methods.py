class Competition:

    def __init__(self, name, country, prize):
        self.__name = name
        self.__country = country
        self.__prize = prize

    def get_name_country(self):
        return '{}, {}'.format(self.__name, self.__country)

    def __repr__(self):
        return "Competition: {} held in {}, prize: {}"\
            .format(self.__name, self.__country, self.__prize)

    def __str__(self):
        return '{} - {}'.format(self.get_name_country(), self.__prize)

archery = Competition('Archery', 'Spain', 7500)

print(archery)
print(str(archery))
print(archery.__str__())

print(repr(archery))
print(archery.__repr__())

# class Savings:
#     def __init__(self, amount):
#         self.__amount = amount
#
#     def __add__(self, other):
#         return self.__amount + other.__amount
#
#
# s1 = Savings(10000)
# s2 = Savings(2000)

# print(s1 + s2)  #not supported for classes without __add__

#
# print(s1 + s2)
#
#
# class MethodSub:
#     def __init__(self, number):
#         self.__number = number
#
#     def __sub__(self, other):
#         return self.__number * other.__number
#
# num_1 = MethodSub(10)
# num_2 = MethodSub(8)

# print(num_1 - num_2)  # calculates using the information in the __sub__ method
# print(num_1 * num_2)  # no * operation is defined

class Savings:
    def __init__(self, amount):
        self.__amount = amount

    def __add__(self, other):
        return self.__amount + other.__amount

    def __mul__(self, other):
        if type (other) == int or type(other) == float:
            return self.__amount * other
        else:
            raise ValueError('Can only multiply by int or float')

s1 = Savings(1000)
s2 = Savings(2000)
# print(s1 * s2)  #error because s2 is of type Savings not int or float
print(s1*3)
print(s1 * 3.1)


class MethodFloordiv:

    def __init__(self, number):
        self.__number = number

    def __floordiv__(self, other):
        return self.__number // other.__number


num_1 = MethodFloordiv(10)
num_2 = MethodFloordiv(3)

print(num_1 // num_2)


class Participants:

    def __init__(self):
        self.__participants = []
        self.__index = 0

    def add_participant (self, name):
        self.__participants.append(name)

    def __len__(self):
        return len(self.__participants)

    def __iter__(self):
        self.__index = 0
        return self

    def __next__(self):
        if self.__index == len(self.__participants):
            raise StopIteration
        p = self.__participants[self.__index]

        self.__index += 1

        return p

participants = Participants()

participants.add_participant('Lily')
participants.add_participant('James')
participants.add_participant('Harry')
participants.add_participant('Ron')
participants.add_participant('Hermione')

for p in participants:
    print(p)
