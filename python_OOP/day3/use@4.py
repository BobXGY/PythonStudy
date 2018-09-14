#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 含有默认参数的函数的装饰器


def log(func):
    def wrapper(*args, dp = func.__defaults__, **kwargs):
        print('call %s():' % func.__name__)
        func(*args, dp, **kwargs)
    return wrapper


@log
def now(user, date: str='2018-9-10'):              # 我们考虑这样一个函数，参数情况比较复杂
    print('user: ', user)
    print(date)


if __name__ == '__main__':
    now('Bob')
