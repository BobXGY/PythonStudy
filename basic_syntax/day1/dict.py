#!/usr/bin/env python3
# -*- coding: utf-8 -*-
##################################################################

# dict：dictionary的简写，类似于c++的map，键值对方式存储
# dict的存储是没有顺序的

# 定义一个字典
person1 = {'name': 'bob', 'id': '5120162657', 'math': 99, 'c++': 87}
# 定义一个空字典
emptyD = {}

# 通过如下方式取得值
print('name:%s id:%s math_score:%d' % (person1['name'], person1['id'], person1['math']))

# 通过键赋值
person1['name'] = 'peter'
print(person1['name'])
##################################################################


# 如果键不存在则会报错，可以通过以下2种方法避免

# 1	用in判断
judge = 'alice' in person1  # 在person1中不存在键：alice 则会返回布尔值false
print(judge)
# 2	用get()方法
judge = person1.get('alice')  # 在person1中不存在键：alice 会返回None
print(judge)
# 3	也可以指定返回的值
judge = person1.get('alice', -1)  # 指定返回值为为整数-1
print(judge)
##################################################################


# 用pop方法通过键删除键值对
person1.pop('math')  # 删除不存在的键同样会报错，也可以用上面方法解决
print(person1)

##################################################################
# keys	方法返回字典中所有键
print(person1.keys())
# values	方法返回字典中所有值
print(person1.values())
# items	方法返回字典中所有键值对
print(person1.items())
# 这三种方法返回值类型分别是dict_keys,dict_values,dict_items而不是列表或其他常用类型

# 用如下方法转换成列表，每个键值对会变成一个二元元组
print(list(person1.items()))

print('\n============================\n')
