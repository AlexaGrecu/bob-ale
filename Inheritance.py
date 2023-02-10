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
    pass


circle = Circle('circle')
