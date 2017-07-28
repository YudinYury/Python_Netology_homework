"""lesson_3_6_homework «Classes»

"""

import chardet
import os
from urllib.parse import urlencode


# from xml.etree.ElementTree import fromstring, ElementTree


class Animal:
    my_type = 'Animal'
    area = 'Earth'
    prefered_food = 'food'
    sound = 'aaaaaaaaaaaaaaa'
    useful = None

    def __init__(self):
        pass

    def speak(self):
        print('I can speak "{}"'.format(self.sound))

    def about(self):
        print('I am {}. I live in {}. I eat {}.'.format(self.my_type, self.area, self.prefered_food))


class Hoofed(Animal):  # Копытное
    different = 'hooves'
    my_type = 'Hoofed'
    area = 'a land'
    prefered_food = 'plants'
    sound = 'ooooooooooooooo'

    def __init__(self):
        pass

    def about(self):
        super().about()
        print('I have {}.'.format(self.different))


class Cow(Hoofed):  # Корова
    my_type = 'Cow'
    area = 'a meadow'
    prefered_food = 'fresh plants'
    sound = 'Muuuuu'
    different = 'horns'
    useful = 'I give a milk'

    def __init__(self, name=''):
        self.my_name = name

    def about(self):
        if len(self.my_name):
            print('My name is {}'.format(self.my_name))
        else:
            print('My name is ... oops. Parents forgot to give me a name.')
        super().about()
        print('I am useful because {}.'.format(self.useful))


class Goat(Hoofed):  # Коза
    my_type = 'Goat'
    area = 'a meadow'
    prefered_food = 'fresh plants'
    sound = 'baaa'
    different = 'small horns'
    useful = 'I give a dietary milk'

    def __init__(self, name=''):
        self.my_name = name

    def about(self):
        if len(self.my_name):
            print('My name is {}'.format(self.my_name))
        else:
            print('My name is ... oops. Parents forgot to give me a name.')
        super().about()
        print('I am useful because {}.'.format(self.useful))


class Sheep(Hoofed):  # Овца
    my_type = 'Sheep'
    area = 'a highland'
    prefered_food = 'fresh plants'
    sound = 'baaa'
    different = 'thick coat'
    useful = 'I give a wool'

    def __init__(self, name=''):
        self.my_name = name

    def about(self):
        if len(self.my_name):
            print('My name is {}'.format(self.my_name))
        else:
            print('My name is ... oops. Parents forgot to give me a name.')
        super().about()
        print('I am useful because {}.'.format(self.useful))


class Pig(Hoofed):  # Свинья
    my_type = 'Pig'
    area = 'a village'
    prefered_food = 'any food'
    sound = 'piggy-piggy'
    different = 'round ass'
    useful = 'I give a bacon'

    def __init__(self, name=''):
        self.my_name = name

    def about(self):
        if len(self.my_name):
            print('My name is {}'.format(self.my_name))
        else:
            print('My name is ... oops. Parents forgot to give me a name.')
        super().about()
        print('I am useful because {}.'.format(self.useful))


class Bird(Animal):
    different = 'wings'
    useful = None
    my_type = 'Bird'
    area = 'a sky'
    prefered_food = 'seeds'
    sound = 'hr-hr-hr-hr-hr-hr-hr-hr-hr-hr'

    def __init__(self):
        pass

    def about(self):
        super().about()
        print('I have {}.'.format(self.different))


class Duck(Bird):  #
    my_type = 'Duck'
    area = 'a lake'
    prefered_food = 'worms'
    sound = 'quack quack'
    useful = 'I give a dietary meat'

    def __init__(self, name=''):
        self.my_name = name

    def about(self):
        if len(self.my_name):
            print('My name is {}'.format(self.my_name))
        else:
            print('My name is ... oops. Parents forgot to give me a name.')
        super().about()
        print('I am useful because {}.'.format(self.useful))

class Chicken(Bird):  #
    my_type = 'Chicken'
    area = 'about house'
    prefered_food = 'seeds and worms'
    sound = 'Cock-a-rat'
    useful = 'I give an egg'

    def __init__(self, name=''):
        self.my_name = name

    def about(self):
        if len(self.my_name):
            print('My name is {}'.format(self.my_name))
        else:
            print('My name is ... oops. Parents forgot to give me a name.')
        super().about()
        print('I am useful because {}.'.format(self.useful))

class Goose(Bird):  #
    my_type = 'Goose'
    area = 'a lake'
    prefered_food = 'seeds and worms'
    sound = 'quoock quoock'
    useful = 'I give a fluff'

    def __init__(self, name=''):
        self.my_name = name

    def about(self):
        if len(self.my_name):
            print('My name is {}'.format(self.my_name))
        else:
            print('My name is ... oops. Parents forgot to give me a name.')
        super().about()
        print('I am useful because {}.'.format(self.useful))


def main():
    enim = Animal()
    enim.about()
    enim.speak()
    print()
    hoofed = Hoofed()
    hoofed.about()
    hoofed.speak()
    print()

    cow = Cow('Дуня')
    cow.about()
    cow.speak()
    print()

    duck = Duck()
    duck.about()
    duck.speak()

    exit(0)


if __name__ == '__main__':
    main()
