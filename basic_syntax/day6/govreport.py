#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 用词云分析政府工作报告

import wordcloud
import jieba

file = open('新时代中国特色社会主义.txt', mode='rt', encoding='utf-8')
txt = file.read()
file.close()

allwordslist = jieba.lcut(txt)
txt = ' '.join(allwordslist)

wcobj = wordcloud.WordCloud(font_path='msyh.ttc',
                            width=1000,
                            height=750,
                            background_color='black',
                            max_words=10)
wcobj.generate(txt)
wcobj.to_file('govWC.png')
