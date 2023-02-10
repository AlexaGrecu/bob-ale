# class Competition:
#
#     raise_amount = 1.04
#
#     def __init__(self, name, prize):
#
#         self.name = name
#         self.prize = prize
#
#     def raise_prize(self):
#         self.prize = self.prize * Competition.raise_amount
#
#
# debate = Competition('Debate', 500)
#
# print(debate.raise_amount)
# print(Competition.raise_amount)
#
# essay = Competition('Essay', 500)
# print(essay.prize)
# print(essay.raise_prize())
# print(essay.prize)
#
# simulation = Competition('Simulation', 100)
# print(simulation.prize)
# print(simulation.raise_prize())
# print(simulation.prize)
#
# print(Competition.raise_amount)
# print(simulation.raise_amount)
#
#
# print(Competition.__dict__)
#
# racing = Competition('Racing', 1000)
# print(racing.raise_amount)
# Competition.raise_amount = 1.05
# print(Competition.raise_amount)
#
#
# simulation.raise_amount = 10
#
# print(Competition.raise_amount, simulation.raise_amount, racing.raise_amount)


# class Competition:
#     participants = []
#
#     def __init__(self, name, prize):
#
#         self.name = name
#         self.prize = prize
#
#
# debate = Competition('Debate', 500)
# Competition.participants.append('John')
# debate.participants.append('Alice')
# print(debate.participants)
# print(Competition.participants)
#
#
# essay = Competition('Essay', 456)
# print(essay.participants)
#
# debate.participants.append('Lily')
# print(debate.participants)
# print(Competition.participants)
# print(essay.participants)


# class Competition:
#
#     def __init__(self, name, prize):
#
#         self.name = name
#         self.prize = prize
#         self.participants = []
#
#
# debate = Competition('Debate', 500)
# print(debate.participants)
# # print(Competition.participants)
#
# debate.participants.append('Alice')
# print(debate.participants)
#
# essay = Competition('Essay', 456)
# print(essay.participants)
# essay.participants.append('Michael')
# print(essay.participants)
#
# debate.participants.append('Lily')
# print(debate.participants)
# print(essay.participants)
#
# print(Competition.__dict__)
# print(debate.__dict__)

# Private variable hack

# class Dog:
#     def __init__(self, name, breed):
#
#         self.__name = name
#         self.__breed = breed
#
#     def print_details(self):
#         print('My name is %s and I am a %s' % (self.__name, self.__breed))
#
#
# d1 = Dog('Oba', 'Labrador')
# d1.print_details()
# d1.__name = 'Nemo'
# d1.print_details()
# d1.__breed = 'Golden Retriever'
# d1.print_details()
#
# print(Dog.__dict__)
# print(d1.__dict__)
#
# d1._Dog__breed = 'Husky'  # you can change the var if you use class__breed

# class Dog:
#     def __init__(self, name, breed):
#         self.__name = name
#         self.__breed = breed
#
#     def print_details(self):
#         print('My name is %s and I am a %s' % (self.__name, self.__breed))
#
#     def change_name(self, name):
#         self.__name = name
#
#
# d1 = Dog('Nemo', 'Husky')
# d1.change_name('Oba')
# d1.print_details()


# Getters and Setters

# class Dog:
#
#     __species = 'canine'
#
#     def __init__(self, name, breed):
#         self.__name = name
#         self.__breed = breed
#         self.__tricks = []
#
#     def get_name(self):
#         return self.__name
#
#     def set_name(self, name):
#         self.__name = name
#
#     def get_breed(self):
#         return self.__breed
#
#     def set_breed(self, breed):
#         self.__breed = breed
#
#     def add_trick(self, trick):
#         self.__tricks.append(trick)
#
#     def print_details(self):
#         print('My name is %s and I am a %s and I can do tricks! %s' % (self.__name, self.__breed, self.__tricks))
#
#
# d1 = Dog('Moje', 'Golden Retriever')
# d1.print_details()
# d1.add_trick('roll over')
# d1.print_details()
# d1.set_breed('Labrador')
# d1.print_details()

# class Dog:
#     """This is a class which defines a dog.
#     This includes cute dogs and ferocious dogs"""
#
#     __species = 'canine'
#
#     def __init__(self, name, breed):
#         self.__name = name
#         self.__breed = breed
#         self.__tricks = []
#
#     def print_details(self):
#         print('My name is %s and I am a %s ' % (self.__name, self.__breed))
#         print('Here are the trucks I can do: ', self.__tricks)
#
#     def change_name(self, name):
#         self.__name = name
#
#     def change_breed(self, breed):
#         self.__breed = breed
#
#     def change_name_and_breed(self, name, breed):
#         self.change_name(name)
#         self.change_breed(breed)
#
#     def add_tricks(self, trick):
#         self.__tricks.append(trick)
#
#
# d1 = Dog('Moje', 'Golden Retriever')
# d1.print_details()
#
# d1.change_name_and_breed('Oba', 'Labrador')
# d1.print_details()

