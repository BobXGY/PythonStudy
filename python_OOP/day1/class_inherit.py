#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 类的继承


class Animal(object):
    def __init__(self, name: str = 'animal'):
        self.__name = name

    def __len__(self):                  # 使用系统函数len()时会调用类的__len__()方法
        return self.__name.__len__()    # len(obj)和obj.__len__()效果相同

    def run(self):
        print('{} is running...'.format(self.__name))

    def eat(self):
        print('{} is eating...'.format(self.__name))


class Cat(Animal):
    def __init__(self, name: str = 'cat'):
        super().__init__(name)


class Dog(Animal):
    def __init__(self, name: str = 'cat'):
        super().__init__(name)


class Python(Animal):
    def __init__(self, name: str = 'python'):
        super().__init__(name)


def main():
    mycat = Cat('mycat')
    mycat.run()
    print(isinstance(mycat, Cat))       # 判断对象实例的类型是否是Cat
    print(isinstance(mycat, Animal))    # 继承自Animal的Cat仍然也是Animal
    print('len(mycat):', len(mycat), 'mycat.__len__():', mycat.__len__())
    print('dir(mycat):', dir(mycat))    # 查看实例的所有属性和方法


if __name__ == '__main__':
    main()
