import math

# Subclasses and inheritance


class Shape:
    def __init__(self, shape_type, color='Red'):
        self.__type = shape_type
        self.__color = color

    def get_type(self):
        return self.__type

    def get_color(self):
        return self.__color

    def get_area(self):
        pass

    def get_perimeter(self):
        pass


circle = Shape('circle')
print(type(circle))
print(circle.get_type())

square = Shape('square', color='Blue')
print(square.get_type())
print(circle.get_color())
print(square.get_color())

s = Shape('circle')


class Circle(Shape):
    def __init__(self, color='Green'):
        Shape.__init__(self, 'circle', color)


circle = Circle()


class Square(Shape):
    def __init__(self, color):
        Shape.__init__(self, 'square', color)


square = Square('Orange')

print(circle.get_color())
print(square.get_color())


class Circle(Shape):
    def __init__(self, radius):
        Shape.__init__(self, 'circle')

        self.__radius = radius

    def get_area(self):
        return math.pi * self.__radius * self.__radius

    def get_perimeter(self):
        return 2 * math.pi * self.__radius


c = Circle(10)
print(c.get_area())
print(c.get_perimeter())


class Square(Shape):
    def __init__(self, side):
        Shape.__init__(self, 'square')

        self.__side = side

    def get_area(self):
        return self.__side * self.__side

    def get_perimeter(self):
        return 4 * self.__side


s1 = Square(10)
print(s1.get_area())
print(s1.get_perimeter())


class Competition:
    __raise_amount = 1.10

    def __init__(self, name, prize):
        self.__name = name
        self.__prize = prize

    def get_name(self):
        return self.__name

    def get_prize(self):
        return self.__prize

    def raise_prize(self):
        self.__prize = self.__prize * self.__raise_amount


race = Competition('Race', 100)

help(Competition)


class Sprint(Competition):
    pass


help(Sprint)
sprint = Sprint('100m', 700)

print(type(sprint))
print(sprint.__dict__)
print(sprint.get_name(), sprint.get_prize())

sprint.raise_prize()
print(sprint.get_prize())

chess = Competition('Chess', 1000)
print(chess.get_prize())
chess.raise_prize()
print(chess.get_prize())


class Cycling(Competition):

    def __init__(self, name, prize, country):
        super().__init__(name, prize)
        self.__country = country

    def get_country(self):
        return self.__country


cycling = Cycling('10km', 7500, 'USA')

print(cycling.get_country())
print(cycling.get_name(), cycling.get_prize())

print(issubclass(Cycling, Competition))


class Shooting():

    def __init__(self, name):
        self.first = name


print(issubclass(Shooting, Competition))  # results false, you need to mention the base class between ()


class Shooting(Competition):

    def __init__(self, name, prize):
        super().__init__(name, prize)


shooting = Shooting('Rifle', 1000)
print(shooting.get_name())
print(shooting.get_prize())
print(issubclass(Shooting, Competition))
