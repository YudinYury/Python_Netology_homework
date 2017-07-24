"""lesson_3_6_classwork «Classes ...»

"""

import json
import os


class Car:
    fuel = None
    current_speed = 0
    maxspeed = 220
    position = 0

    def __init__(self, position, fuel):
        self.position = position
        self.fuel = fuel

    def start(self):
        print('Wroom!')

    def accelerate(self, value):
        self.current_speed += value

    def steer_turn(self, value):
        if value == 'left':
            print('Turning left')
        elif value == 'right':
            print('Turning right')
        else:
            raise Exception

    def steer(self, hours):
        self.position += self.current_speed * hours
        # 10 l/h
        self.fuel -= 10 * hours

    def brake_car(self):
        self.current_speed = 0

    def stop(self):
        print('Stopped')


class ExpensiveCar:
    cost = 1_000_000_000_000

    def start(self):
        print('Wroom!!!!!!!!!!!!')


class SportCar(ExpensiveCar, Car):
    color = 'red'
    max_speed = 300  # km/h

    def __init__(self, position, fuel, color):
        self.color = color
        super().__init__(position, fuel)

    def start(self):
        super().start()  # call metod from patent Class (ExpensiveCar)
        print('sport Wroom!')


class A:
    __slots__ = ['a', 'b']  # для экономии памяти заранее определяем возможные аттрибуты


class B:
    pass


def main():
    # car = Car(101, 100)
    # print(car)
    # print(car.current_speed)
    # print(car.position)
    # print(car.fuel)
    # car.start()
    # car.accelerate(60)
    # print(car.current_speed)
    # car.brake_car()
    # car.stop()
    # print(car.current_speed)
    #
    # car.accelerate(40)
    # car.steer(4)
    # print(car.position)
    # print(car.fuel)
    # print(car.__dict__)
    # print()
    # print(Car.__dict__)

    sport_car = SportCar(0, 100, 'Red')
    sport_car.start()
    print(sport_car.max_speed)
    print(sport_car.current_speed)
    print()
    print(sport_car.__dict__)
    print(SportCar.__dict__)

    print()
    print(SportCar.mro())  # порядок наследования

    exit(0)


if __name__ == '__main__':
    main()
