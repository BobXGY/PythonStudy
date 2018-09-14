#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://python123.io/student/courses/0/groups/340/problems/programmings/2683
# 阶乘累计求和

import sys


def jiec(num):
    if num == 1:
        return 1
    else:
        return num * jiec(num-1)


try:
    n = int(input())
    if n <= 0:
        print('输入有误，请输入正整数')
        sys.exit(0)
    res = 0
    for i in range(1, n + 1):
        res += jiec(i)
    print(res)
except ValueError:
    print('输入有误，请输入正整数')


