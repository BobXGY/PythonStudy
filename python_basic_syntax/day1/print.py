#!/usr/bin/env python3
# -*- coding: utf-8 -*-
##################################################################
n = 123
f = 456.789
s1 = 'Hello, world'
s2 = 'Hello, \'Adam\''
s3 = r'Hello, "Bart"'
s4 = r'''Hello,
Lisa!'''

print(n)
print(f)
print(s1)
print(s2)
print(s3)
print(s4)
s1.encode('ascii')
##################################################################

str='Runoob'

print(str)                 # 输出字符串
print(str[0:-1])           # 输出第一个到倒数第二个的所有字符
print(str[0])              # 输出字符串第一个字符
print(str[2:5])            # 输出从第三个开始到第五个的字符
print(str[2:])             # 输出从第三个开始的后的所有字符
print(str * 2)             # 输出字符串两次
print(str + '你好')        # 连接字符串

print('------------------------------')

print('hello\nrunoob')     # 使用反斜杠(\)+n转义特殊字符
print(r'hello\nrunoob')    # 在字符串前面添加一个 r，表示原始字符串，不会发生转义

##################################################################
# print 默认输出是换行的，如果要实现不换行需要在变量末尾加上 end=""或end=''
print(x, end="")
print(y, end='')


input('\n按enter退出\n============================\n')