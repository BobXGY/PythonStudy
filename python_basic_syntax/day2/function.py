#!/usr/bin/env python3
# -*- coding: utf-8 -*-
##################################################################

# python函数

# type() 函数可以用来查询变量所指的对象类型

# abs() 求绝对值函数
number1 = abs(-184.9)
print('绝对值:%d' % number1)
##################################################################


# max() 求最大值函数，参数数量任意
maxNumber = max(999, number1, -1, 19, 0)
print('最大值%d:' % maxNumber)
##################################################################


# 同样有min()函数
minNumber = min(999, number1, -1, 19, 0)
print('最小值：%d' % minNumber)
##################################################################


##################################################################
# 数据类型转换函数
##################################################################

# int() 可以把其他数据类型转换为整数
number2 = int('123')  # 会将字符串’123‘转换为整数123
number3 = int(9.99)
number4 = int(False)  # False	会转化为0
number5 = int(True)  # True	会转化为1
# 注意：在 Python2 中是没有布尔型的，它用数字 0 表示 False，用 1 表示 True。
# 到 Python3 中，把 True 和 False 定义成关键字了，但它们的值还是 1 和 0，它们可以和数字相加。
print('转换为整数:\t%d\t%d\t%d\t%d' % (number2, number3, number4, number5))
##################################################################

# 另有str() 转换为字符串,bool() 转换为布尔值 等转换函数

# 一个小技巧，可以把函数名赋值给一个变量，例如
myFunction = bool
print(myFunction(-1))

input('\n按enter退出\n============================\n')
