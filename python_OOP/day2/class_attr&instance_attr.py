#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 类属性和实例属性


class Student(object):
    count = 0           # count是一个类属性
    name = 'Student'    # name是一个类属性

    def __init__(self, name: str='stu_name'):
        self.name = name  # self.name是一个实例属性
        Student.count += 1


def main():
    stu1 = Student('Bob')
    print(Student.count)
    stu2 = Student('Jack')
    print(Student.count)

    print(stu1.name)            # 和成员方法一样,实例的属性也会覆盖类属性
    print(Student.name)


if __name__ == '__main__':
    main()
