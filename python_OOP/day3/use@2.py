#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 有固定参数的函数装饰器


# 和刚才一样，只需加上参数即可
def log(func):
    def wrapper(parameter: str='2018-9-10'):
        print('call %s():' % func.__name__)
        func(parameter)
    return wrapper


@log
def now(date: str='2018-9-10'):              # 现在now()有了参数date
    print(date)


if __name__ == '__main__':
    now()
    now('123123123')
    for p in dir(now):
        print(p)
    print(now.__defaults__)

#####################################################################################################################
# 如果要用修饰器修饰一堆不同参数的函数怎么办呢? 参见use@3.py                                                             #
#####################################################################################################################
