#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 类变量


class Myobj(object):
    # 在这里定义一个类变量，用于统计生成了这个类的实体的个数
    # 类变量不属于任何实例，属于类本身
    obj_counts = 0

    def __init__(self, name):
        self.__name = name
        Myobj.obj_counts += 1
        # 强调:self关键字是指当前的对象实体，而不是这个实体所属的类
        # 因此在这里操作类变量不能写成self.obj_counts

    def __del__(self):
        Myobj.obj_counts -= 1


if __name__ == '__main__':
    o1 = Myobj('bob')
    o2 = Myobj('kate')
    o3 = Myobj('ada')

    o3.obj_counts = 5
    # 这个赋值语句相当于在实体o3中创建了一个成员变量obj_counts并赋值为5
    # 不会对类变量 Myobj.obj_counts 造成任何影响
    print("Myobj.obj_counts = {}, o3.obj_counts = {}, o1.obj_counts = {}".format(Myobj.obj_counts,
                                                                                 o3.obj_counts,
                                                                                 o1.obj_counts))
    del o3
    print("Myobj.obj_counts = {}".format(Myobj.obj_counts))
