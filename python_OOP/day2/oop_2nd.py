#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 三个方法 getattr()、setattr()以及hasattr()
import types


class MyObj(object):
    name = ''
    __id = ''

    def __init__(self, myid: str, name: str = 'myobj'):
        self.name = name
        self.__id = myid


def main():
    test_obj = MyObj('001', 'OBJ1')
    print("hasattr('name'):"            , hasattr(test_obj, 'name'))
    print("hasattr(test_obj, '__id'):"  , hasattr(test_obj, '__id'))    # 私有变量用hasattr()返回一定为False

    print("name:", getattr(test_obj, 'name'))
    # print("__id:", getattr(test_obj, '__id'))                         # 私有变量用这个方法也会抛出异常: AttributeError

    setattr(test_obj, 'time', '12:00')                                  # 增加成员变量
    print(getattr(test_obj, 'time'))                                    # 如果试图获取不存在的属性会抛出AttributeError

    print(main.__name__)                        # 特殊变量__name__, 函数也是一个对象
    print(isinstance(main, types.FunctionType))
    print(type(main), types.FunctionType)
    print(dir(main))


if __name__ == '__main__':
    main()
