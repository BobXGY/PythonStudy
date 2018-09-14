#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 多重继承


class Animal(object):
    def __init__(self, lifetime: int=0):
        self.__lifetime = lifetime
    pass


# 大类:
class Mammal(Animal):
    pass


class Bird(Animal):
    pass


class Runnable(object):
    def run(self):
        print('Running...')


class Flyable(object):
    def fly(self):
        print('Flying...')


# 各种动物:
class Dog(Mammal, Runnable):
    def __init__(self):
        super().__init__()


class Bat(Mammal, Flyable):
    def __init__(self):
        super().__init__()


class Parrot(Bird, Flyable):
    pass


class Ostrich(Bird, Runnable):
    pass


if __name__ == '__main__':
    a = object()
    print(dir(a))
