#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 使用内置装饰器@property来限制属性的取值范围

# 定义一个学生类：


class Student(object):
    __score = 0.0
    # 我们希望有一个成员属性:score
    # 要对对其的访问加以限制，同时又想像直接使用成员变量一样方便访问
    # 就可以使用@property

    def __init__(self):
        pass

    @property       # 这样一来就可以直接通过.score而不是.score()来访问__score了
    def score(self):
        return self.__score

    # 这个时候@property会自动生成一个.setter装饰器，这里我们写人@score.setter
    # 重载score方法，就可以通过.score来设置成员属性，同时实现对属性的修改限制
    @score.setter
    def score(self, value: float):
        if 0 <= value <= 100:
            self.__score = value
        else:
            raise ValueError


if __name__ == '__main__':
    stu1 = Student()
    stu1.score = 88.5
    try:
        stu1.score = 200
    except ValueError:
        print('ValueError')
    print(stu1.score)
