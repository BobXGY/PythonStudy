#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @author Bob
# @create time 2018/11/15 16:05
# @file Spider.py
# @software PyCharm
from 实验报告.Spider import NovelGet

if __name__ == '__main__':
    novel = ''
    urls = ['https://read.qidian.com/chapter/-WkNjDCxgv6RTIpqx7GUJA2/YsQf3E-oiR62uJcMpdsVgA2',
            'https://read.qidian.com/chapter/-WkNjDCxgv6RTIpqx7GUJA2/jThFps4zB_Fp4rPq4Fd4KQ2',
            'https://read.qidian.com/chapter/-WkNjDCxgv6RTIpqx7GUJA2/x2yh_sYZBzX4p8iEw--PPw2',
            'https://read.qidian.com/chapter/-WkNjDCxgv6RTIpqx7GUJA2/-LWEHxMgLab4p8iEw--PPw2',
            'https://read.qidian.com/chapter/-WkNjDCxgv6RTIpqx7GUJA2/z8mhFSiOVO62uJcMpdsVgA2']

    for index in range(5):
        novel = novel + '\n================第' + str(index + 1) + '章================'
        chapter = NovelGet(urls[index])
        chapter.get_html()
        chapter.get_text()
        novel += chapter.tag_string

    print(novel)
