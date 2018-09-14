#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 类的高级用法1

from types import MethodType


class Student(object):
    pass


def main():
    s = Student()
    s.name = 'Bob'
    print(s.name)

    def set_age(self, age: int):    # 给实例定义的方法
        self.age = age

    s.set_age = MethodType(set_age, s)  # 将方法与一个实例绑定, 这样实例s就有了set_age()方法

    s.set_age(5)                        # 这样一来实例s有了一个属性: s = 5
    print(s.age)

    # 当然也可以给类绑定方法
    def set_score(self, score: int):
        self.score = score

    Student.set_score = MethodType(set_score, Student)
    Student.set_score(99)
    print(Student.score)
    # 这样Student类就有了set_score()方法和score属性，该类所有实例都可用，如下：

    s.set_score(80)
    print(s.score)  # 会输出80而不是99


if __name__ == '__main__':
    main()
