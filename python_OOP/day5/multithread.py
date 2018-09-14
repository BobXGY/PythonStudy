#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 多线程
from threading import Thread


def t1():
    print('这是一个线程')


if __name__ == '__main__':
    th1 = Thread(target=t1)
    th1.start()
    th1.join()
    print('th1执行完毕')
