#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# class day1


class Student(object):
    # 类的定义方法 class <类名>(<继承的父类>):
    # 没有合适的父类就填object 所有的类最终都继承自object
    # 所有成员方法的第一个参数必定是self,表示自己, 个人认为和java的this类似
    def __init__(self, name: str, score: float):
        # 构造函数： __init__
        # 以'__'两个下划线开头的变量会成为私有变量
        if 0 < score < 100:
            self.__score = score
        else:
            raise ValueError('bad score')
        self.__name = name

    def get_info(self):
        return [self.__name, self.__score]

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score


def main():
    stu1 = Student('Bob', 98)
    print(stu1.get_info())


if __name__ == '__main__':
    main()
