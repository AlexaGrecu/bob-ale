from abc import ABC, abstractmethod


class Hominidae(ABC):
    @abstractmethod
    def diet(self):
        pass

    @abstractmethod
    def walk(self):
        pass

    def behavior(self):
        print('They show complex facial expression and social behaviour')


chimpanzee = Hominidae()
chimpanzee.behavior()
chimpanzee.diet()
chimpanzee.walk()


class Human(Hominidae):
    def diet(self):
        print('Humans are omnivorous.')

    def walk(self):
        print('They are bipeds.')


paul = Human()
paul.diet()
paul.walk()
help(ABC)