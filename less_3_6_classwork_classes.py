"""lesson_3_6_classwork «Classes ...»

"""

import json
import os


class Car:
    fuel = None
    current_speed = 0
    maxspeed = 220
    position = (0, 0)

    def start(self):
        print('Wroom!')

    def accelerate(self, value):
        self.current_speed += value

    def steer(self, value):
        if value == 'left':
            print('Turning left')
        elif value == 'right':
            print('Turning right')
        else:
            raise Exception

    def brake_car(self):
        self.current_speed = 0

    def stop(self):
        print('Stopped')


def main():
    car = Car()
    print(car)
    print(car.current_speed)
    car.start()
    car.accelerate(60)
    print(car.current_speed)
    car.brake_car()
    car.stop()
    print(car.current_speed)

    exit(0)


if __name__ == '__main__':
    main()
