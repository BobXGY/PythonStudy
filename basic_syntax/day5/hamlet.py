#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 哈姆雷特词频统计


def initText():                 # 预处理文本，转换为小写，去掉标点符号
    txt = open("hamlet.txt").read()
    txt = txt.lower()
    for ch in '''~!@#$%^&*()-=_+`[]\;,./{}|:<>?'"''':
        txt = txt.replace(ch, ' ')
    return txt


allWords = initText().split()
wordCounts = {}
for word in allWords:
    wordCounts[word] = wordCounts.get(word, 0) + 1  # 这里不能用wordCounts[word]+=1的原因是：
    # 如果第一次碰到该词而字典里没有相应的键则会抛出‘KeyError’

items = list(wordCounts.items())  # 键值对会变成元组类型(key,value)存入列表

items.sort(key=lambda x: x[1], reverse=True)  # 列表对象的sort方法用法说明:
# 此处列表中的元素是元组(复合类型),需选取一个简单元素作为排序依据
# key的实参应该是一个函数名，这个函数应该返回列表元素(复合类型)中的一个简单元素
# 此处列表元素是元组，用第二个简单元素，也就是之前键值对的‘值’进行排序

print('哈姆雷特中出现频率最高的20个单词：')
for i in range(0, 20):
    print('{:2}:{:10}:{}次'.format(i + 1, items[i][0], items[i][1]))
