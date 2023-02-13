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
    name = property(get_name, set_name, del_name())

w = Wrestler()
w.name = 'Kart'
print(w.name)

