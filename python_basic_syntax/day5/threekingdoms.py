#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 三国演义人物词频统计

import jieba

txt = open('threekingdoms.txt', mode='r', encoding='utf-8').read()
allWords = jieba.lcut(txt)
# print(allWords)
wordCounts = {}
paichu = ['将军', '却说', '二人', '不可', '荆州', '不能', '如此',
          '商议', '如何', '主公', '军士', '左右', '军马', '引兵',
          '次日', '大喜', '天下', '东吴', '于是', '今日', '不敢',
          '魏兵', '陛下', '一人', '都督', '人马', '不知', '汉中',
          '只见', '众将', '蜀兵', '上马', '大叫', '太守', '此人',
          '夫人', '后人', '背后', '城中', '天子', '一面', '何不',
          '大军', '忽报', '先生', '百姓', '何故', '然后', '先锋',
          '不如', '赶来', '原来', '令人', '江东', '下马', '喊声']

for word in allWords:
    if len(word) > 1 and not (word in paichu):
        if word in ['玄德曰', '玄德', '先主']:
            word = '刘备'
        elif word in ['丞相', '孟德']:
            word = '曹操'
        elif word in ['孔明曰', '诸葛亮']:
            word = '孔明'
        elif word in ['关公', '云长']:
            word = '关羽'
        elif word in ['后主']:
            word = '刘禅'

        wordCounts[word] = wordCounts.get(word, 0) + 1

items = list(wordCounts.items())
items.sort(key=lambda x: x[1], reverse=True)

for i in range(0, 16):
    print('{:2}:{:6}{:>6}次'.format(i + 1, items[i][0], items[i][1]))
