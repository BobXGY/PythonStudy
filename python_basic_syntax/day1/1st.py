#!/usr/bin/env python3
# -*- coding: utf-8 -*-
##################################################################

print('hello world!')
# print(100+500)
# print('please input your name:')
# name=input()
# print('hi!',name)

print('+++++++++++加法计算器+++++++++++')
numa = int(input('输入第一个数'))
numb = int(input('输入第二个数'))
result = numa + numb
print('计算结果:%d + %d = %d' % (numa, numb, result))
# 可以看见print函数和C语言中的printf使用方式类似
# 占位符也一样 常见有%d %f %s 等等
##################################################################

input('\n按enter退出\n============================\n')
