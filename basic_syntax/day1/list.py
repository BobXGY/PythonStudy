#!/usr/bin/env python3
# -*- coding: utf-8 -*-
##################################################################
classmates = ['bob', 'stu1', 'su']
print('classmates列表如下:')
print(classmates)
print('classmates的长度是：%d' % len(classmates))
print('倒数第一个元素是 %s' % classmates[-1])  # -1表示倒数第一个元素，-2，-3同理

# 指定元素替换，或者说赋值
print('\n')
classmates[0] = 'changed'
print(classmates)
##################################################################


# insert方法
print('\n')
classmates.insert(1, 'hwh')  # 在1号位置插入字符串元素'hwh'
print(classmates)
##################################################################


# append方法
classmates.append('last_one')  # 将元素插入列表末尾
print(classmates)
##################################################################


# pop方法
print('\n')
print('%s被弹出' % classmates.pop())  # 弹出末尾元素
print(classmates)
##################################################################


# 用pop方法删除指定位置元素
print('\n')
print('%s被弹出' % classmates.pop(1))
print(classmates)
##################################################################


# 列表中的元素类型可以各不相同
print('\n')
classmates.insert(-1, 666)
print(classmates)
##################################################################


# list也可以是list的元素
print('\n')
friends = ['kate', 'jimy', 'lisa']
people = ['mother', friends, classmates, ['worker', 'police', 'waiter']]
print('people的长度是:%d' % len(people))  # 长度指元素个数，一个list元素也是一个元素
print(people)
##################################################################


# 另有range函数可以快速生成数字序列,再通过list函数转化为list
number = list(range(101))  # 这样就定义了一个1-100的递增序列，注意是从0开始
print(number)
##################################################################


# ++++++tuple++++++
# 另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改
print('\n')
t = ()  # 定义了一个空tuple
print(t)
t2 = (1,)  # 定义了只有一个整数：1的tuple
# 如果写成t2 = (1)则会被认为是数学小括号而把整数1赋值t2成为一个整形变量
print(t2)
# Python在显示只有1个元素的tuple时，也会加一个逗号,，以免你误解成数学计算意义上的括号。

# 有一种让tuple可变的方法，即在tuple里加入list元素，而list是可变的
li1 = ['elem1', 2, 3.2]
tt = ('first', li1, 'last')
print(tt)
li1.append('++++')
print(tt)
print('\n')
##################################################################


##################################################################
# 练习
# 请用索引取出下面list的指定元素：
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Lisa:
print(L[2][-1])
##################################################################


input('\n按enter退出\n============================\n')
