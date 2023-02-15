class Competition:

    __raise_amount = 1.04

    def __init__(self, name, prize):

        self.__name = name
        self.__prize = prize

    def raise_prize(self):
        self.prize = self.__prize * self.__raise_amount

    def print_details(self):
        print('Name: {}, prize: {}'.format(self.__name, self.__prize))

    @classmethod
    def get_raise_amount(cls):
        return cls.__raise_amount

    @classmethod
    def set_raise_amount(cls, amount):
        cls.__raise_amount = amount

    @classmethod
    def from_str(cls, competition_str):
        name, prize = competition_str.split('-')

        return cls(name, prize)


sprint = Competition('Sprint', 10000)
print(Competition.get_raise_amount())
print(sprint.get_raise_amount())
sprint.set_raise_amount(1.06)
print(sprint.get_raise_amount())
print(Competition.get_raise_amount())

# example that is afterwards added as a class method (from_str)
# swimming_str = 'Swimming-8000'
# name, prize = swimming_str.split('-')
# swimming = Competition(name, prize)
# swimming.print_details()


archery_str = 'Archery-8000'
archery = Competition.from_str(archery_str)
archery.print_details()


#Static_Method

class Rectangle:
    @staticmethod
    def area(x, y):
        return x * y

# manual way of converting into a static method
# Rectangle.area = staticmethod(Rectangle.area)
# print('area of the rectangle is:', Rectangle.area(15, 16))