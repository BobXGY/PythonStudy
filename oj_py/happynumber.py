#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://python123.io/student/courses/0/groups/340/problems/programmings/675
# 快乐的数字

strnumber = input()
res = 0
count = 0
flag = 0

while res != 1:
    res = 0
    count += 1
    for i in strnumber:
        res += int(i) ** 2
    # print(res)
    strnumber = str(res)
    if count == 100:
        print('False')
        flag = 1
        break

if flag == 0:
    print('True')
