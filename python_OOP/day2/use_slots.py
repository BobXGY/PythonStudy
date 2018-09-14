#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 使用____slots__限制实例的属性
from types import MethodType


class Student(object):
    __slots__ = ('name', 'age')  # 用元组表示允许绑定的属性名，该规则只会限制当前类，对继承该类的子类无效


class MidStudent(Student):
    # __slots__ = super.__slots__ # 这样就可以使子类拥有相同限制
    pass


def main():
    s = Student()
    s.age = 16
    s.name = 'Bob'
    try:  # 如果试图绑定__slots__之外的属性就会抛出AttributeError
        s.score = 99
    except AttributeError:
        print('AttributeError')

    def set_age(self, age: int = 0):
        self.age = age

    try:  # 相同地,试图绑定__slots__之外的方法也会导致AttributeError
        s.set_age = MethodType(set_age, s)
    except AttributeError:
        print('AttributeError')

    mstu = MidStudent()
    mstu.set_age = MethodType(set_age, mstu)    # 这时任然可以任意绑定属性和方法
    mstu.set_age(15)
    print(mstu.age)
    MidStudent.__slots__ = Student.__slots__    # 进行限制
    mstu.grade = 2


if __name__ == '__main__':
    main()
