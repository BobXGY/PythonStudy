#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# wordcloud 库的使用

import wordcloud
import jieba
import os.path

print('准备分析')
file = open('threekingdoms.txt', mode='rt', encoding='utf-8')
txt = jieba.lcut(file.read())
file.close()
qofwords = len(txt)

q = 0
while True:
    if q % 500 == 0:
        print('\r正在分析"threekingdoms.txt"{:>8.1f}%'.format(100 * q / len(txt)), end='')
    try:
        if len(txt[q]) == 1:
            del txt[q]
            continue
        else:
            q += 1
    except IndexError:
        break
    if q == qofwords:
        break

print('\r正在分析"threekingdoms.txt"{:>8.1f}%\n生成词云图片中...'.format(100), end='')
wc = wordcloud.WordCloud(background_color='white', width=1000, height=750, font_path='msyh.ttc')
wc.generate(' '.join(txt))
# print(' '.join(txt))
wc.to_file('wc.jpg')
print('完成！\n图片保存为"wc.jpg"')
os.system('wc.jpg')
