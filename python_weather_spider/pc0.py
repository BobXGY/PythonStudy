#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Python爬虫初探

from urllib import request
import chardet				#检测html编码方式的模块

if __name__ == '__main__':
    response = request.urlopen("http://www.baidu.com")
    html = response.read()
    htmlCharset = chardet.detect(html)	#会得到一个字典 类似{'encoding': 'utf-8', 'confidence': 0.99, 'language': ''}
    #print(htmlCharset['encoding'])
    html = html.decode(htmlCharset['encoding'])
    print(html)