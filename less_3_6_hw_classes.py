"""lesson_3_6_homework «Classes»

"""

import chardet
import os
from urllib.parse import urlencode
import osa
import re
import requests
from xml.etree.ElementTree import fromstring, ElementTree


class Animal:
    my_name = 'Animal'
    area = 'Earth'
    prefered_food = 'food'
    sound = 'aaaaaaaaaaaaaaa'
    useful = None

    def __init__(self):
        pass

    def speak(self):
        print('I can speak "{}"'.format(self.sound))

    def about(self):
        print('I am {}. I live in {}. I eat {}.'.format(self.my_name, self.area, self.prefered_food))


class Hoofed(Animal):  # Копытное
    different = 'hooves'

    def __init__(self):
        self.my_name = 'Hoofed'
        self.area = 'a land'
        self.prefered_food = 'plants'
        self.sound = 'ooooooooooooooo'

    def about(self):
        super().about()
        print('I have {}.'.format(self.different))


class Cow(Hoofed):  # Корова
    def __init__(self):
        self.my_name = 'Cow'
        self.area = 'a meadow'
        self.prefered_food = 'fresh plants'
        self.sound = 'Muuuuu'
        self.different = 'horns'
        self.useful = 'I give a milk'

    def about(self):
        super().about()
        print('I am useful because {}.'.format(self.useful))


class Goat(Hoofed):  # Коза
    def __init__(self):
        self.my_name = 'Goat'
        self.area = 'a meadow'
        self.prefered_food = 'fresh plants'
        self.sound = 'baaa'
        self.different = 'small horns'
        self.useful = 'I give a dietary milk'

    def about(self):
        super().about()
        print('I am useful because {}.'.format(self.useful))


class Sheep(Hoofed):  # Овца
    def __init__(self):
        self.my_name = 'Sheep'
        self.area = 'a highland'
        self.prefered_food = 'fresh plants'
        self.sound = 'baaa'
        self.different = 'thick coat'
        self.useful = 'I give a wool'

    def about(self):
        super().about()
        print('I am useful because {}.'.format(self.useful))


class Pig(Hoofed):  # Свинья
    def __init__(self):
        self.my_name = 'Pig'
        self.area = 'a village'
        self.prefered_food = 'any food'
        self.sound = 'piggy-piggy'
        self.different = 'round ass'
        self.useful = 'I give a bacon'

    def about(self):
        super().about()
        print('I am useful because {}.'.format(self.useful))


class Bird(Animal):
    different = 'wings'
    useful = None

    def __init__(self):
        self.my_name = 'Bird'
        self.area = 'a sky'
        self.prefered_food = 'seeds'
        self.sound = 'hr-hr-hr-hr-hr-hr-hr-hr-hr-hr'

    def about(self):
        super().about()
        print('I have {}.'.format(self.different))


class Duck(Bird):  #
    def __init__(self):
        self.my_name = 'Duck'
        self.area = 'a lake'
        self.prefered_food = 'worms'
        self.sound = 'quack quack'
        self.useful = 'I give a dietary meat'


class Chicken(Bird):  #
    def __init__(self):
        self.my_name = 'Chicken'
        self.area = 'about house'
        self.prefered_food = 'seeds and worms'
        self.sound = 'Cock-a-rat'
        self.useful = 'I give an egg'


class Goose(Bird):  #
    def __init__(self):
        self.my_name = 'Goose'
        self.area = 'a lake'
        self.prefered_food = 'seeds and worms'
        self.sound = 'quoock quoock'
        self.useful = 'I give a fluff'


def main():
    enim = Animal()
    enim.about()
    enim.speak()
    print()
    hoofed = Hoofed()
    hoofed.about()
    hoofed.speak()
    print()

    cow = Cow()
    cow.about()
    cow.speak()
    print()

    duck = Duck()
    duck.about()
    duck.speak()

    exit(0)


if __name__ == '__main__':
    main()
