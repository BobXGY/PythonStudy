#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#温度转换

print('华氏摄氏温度转换器')
tempstr = input("请输入温度 例: 23C(23摄氏度) 52F(52华氏度)\n")
if tempstr[-1] in ['C', 'c']:
    f = float(tempstr[0:-1])*1.8+32
    print('{:.2f}F'.format(f))
elif tempstr[-1] in ['F', 'f']:
    c = (float(tempstr[0:-1])-32)/1.8
    print('{:.2f}C'.format(c))
else:
    print('输入错误！')
