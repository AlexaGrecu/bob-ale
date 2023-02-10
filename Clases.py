# class Student:
#     pass
#
#
# print(type(Student))
#
# object_1 = Student()  # creating an object/instance of type student
# object_2 = Student()
#
# print(isinstance(object_1, Student))
#
# object_3 = {}
#
# print(isinstance(object_3, Student))
#
# object_1.name = 'Michel'
# object_1.email = 'Michel@xyz.com'
#
# print(object_1.name)
#
# object_2 = 'Chad'
# object_2 = 'Chad@xyz.com'


# class Student:
#
#     name = ' '
#     score = 0
#     active = True
#
#
# s1 = Student()
# print(s1.name, s1.score, s1.active)
#
# s1.name = 'John'
# s1.score = 50
# print(s1.name, s1.score, s1.active)
#
# s2 = Student()
# print(s2.name, s2.score, s2.active)
# s2.name = 'Lili'
# print(s2.name, s2.score, s2.active)
# s2.active = False
# print(s2.name, s2.score, s2.active)

# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.email = name + "." + "@xyz"
#
#
# s1 = Student('Michel')
# print(s1.name)
# print(s1.email)

class Student:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.email = first + "." + last + "@xyz.com"

    def fullname(self):
        return "{} {}".format(self.first, self.last)


s1 = Student('Rodrigo', 'Joseph')

print(s1.fullname())

s2 = Student('Anthony', "Hopkins")
print(s2.fullname())
print(Student.fullname(s2))

s3 = Student('James', 'Miller')
del s3.first
# print(s3.first) # error: the first name is deleted
print(s3.last)
del s3
print(s3)
