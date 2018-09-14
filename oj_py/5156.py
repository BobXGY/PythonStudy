#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://python123.io/student/courses/0/groups/340/problems/programmings/5156
# 百分制到五级制的转换

import sys
lv = ['A', 'B', 'C', 'D', 'E']

try:
    score = int(input())
    if score < 0 or score > 100:
        print("输入数据有误！")
        print('好好学习，天天向上！')
        sys.exit(0)
    if score >= 60:
        print('输入成绩属于{}级别。'.format(lv[-((score-40)//10)]))
        print('祝贺你通过考试！')
    else:
        print('输入成绩属于{}级别。'.format(lv[-((score-40)//10)]))
except ValueError:
    print("输入数据有误！")


print('好好学习，天天向上！')
