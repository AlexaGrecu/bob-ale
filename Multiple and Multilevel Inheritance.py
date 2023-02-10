class Father:
    pass


class Mother:
    pass


class Child1(Father, Mother):
    pass


help(Child1)


class Child2(Mother, Father):
    pass


help(Child2)


class Father:
    def height(self):
        print('I have inherited my height from my father')


class Mother:
    def intelligence(self):
        print('I have inherited my intelligence from my mother')


class Child(Father, Mother):
    def experience(self):
        print('My experiences are all my own')


c = Child()
c.height()
c.intelligence()
c.experience()


class Employee:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def show_name(self):
        print(self.__name)

    def show_age(self):
        print(self.__age)


class Salary:

    def __init__(self, salary):
        self.__salary = salary

    def get_salary(self):
        print(self.__salary)


class Database(Employee, Salary):

    def __init__(self, name, age, salary):
        Employee.__init__(self, name, age)
        Salary.__init__(self, salary)


emp1 = Database('Robin', 26, 98000)
emp1.show_name()
emp1.show_age()
emp1.get_salary()


class Grandparent:

    def height(self):
        print('I have inherited my height from my grandparent')


class Parent(Grandparent):

    def intelligence(self):
        print('I have inherited my intelligence form my parent')


class Child(Parent):

    def experience(self):
        print('My experiences are all my own')


help(Child)
c = Child()
c.height()
c.intelligence()
c.experience()
