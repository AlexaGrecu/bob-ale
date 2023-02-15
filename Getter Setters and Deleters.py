class Wrestler:

    def __init__(self):
        self.__name = ''

    def set_name(self, name):
        print('setter method called')
        self.__name = name

    def get_name (self):
        print('getter method called')
        return self.__name

    def del_name(self):

        print('delete method called')

        del self.__name
    name = property(get_name, set_name, del_name)

# w1 = Wrestler()
# w1.set_name('Steve')
# print(w1.get_name())
# print(w1.name)


w = Wrestler()
w.name = 'Kart'
print(w.name)

#  Defining properties using decorators


class Wrestler:

    def __init__(self, name):
        self.__name = name

    @property  # decorator
    def name(self):
        print('getter method called')
        return self.__name

    @name.setter # decorator
    def name(self, value):
        print('setter method called')
        self.__name =  value

    @name.deleter # decorator
    def name(self):
        print('deleter method called')
        del self.__name


w = Wrestler('Adam')
print(w.name)

w.name = 'John'
print(w.name)

# del w.name
# print(w.name)

class Wrestler:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property  # decorator
    def name(self):
        print('getter method called')
        return self.__name

    @name.setter  # decorator
    def name(self, value):
        print('setter method called')
        self.__name = value

    @name.deleter  # decorator
    def name(self):
        print('deleter method called')
        del self.__name

    @property
    def age(self):
        print('age getter method called')
        return self.__age

    @age.setter
    def age(self, value):
        print('age setter method called')
        return self.__age

    @age.deleter
    def age(self):
        print('age deleter method called')
        del self.__age


w = Wrestler('Mark', 25)
print(w.name)
w.name = 'John'
print(w.name)
print(w.age)


class Employee(object):
    def __init__(self, employee_id):
        self.__employee_id = employee_id

    @property
    def employee_id(self):
        return self.__employee_id

    @employee_id.setter
    def employee_id(self, employee_id):
        self.__employee_id = employee_id

    @employee_id.deleter
    def employee_if(self):
        del self.__employee_id


