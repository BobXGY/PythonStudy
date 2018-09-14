#!/usr/bin/env python3
# -*- coding: utf-8 -*-
##################################################################

# for ... in ...循环
names = ['bob', 'alice', 'alex', 'cindy']
for name in names:  # 注意不要漏写冒号
    print(name)     # 这样就可以打印names中的所有元素

sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    sum = sum + x
print(sum)  # 这样就可以计算该list中全部元素的和

sum = 0
number = list(range(101))  # 定义一个包含0-100数字的list
for x in number:
    sum = sum + x
print(sum)
##################################################################


# while循环，和C语言，java类似
sum = 0
n = 0
while n <= 100:  # 同样完成了1连加到100的操作
    sum = sum + n
    n = n + 1
print(sum)
# while循环中同样可以像C,JAVA一样使用break和continue，效果相同
##################################################################


input('\n按enter退出\n============================\n')
