#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#第一个爬虫
#爬了百度首页的备案号

from urllib import request
import chardet
from bs4 import BeautifulSoup

response = request.urlopen('http://www.baidu.com')
html = response.read()
htmlCharset = chardet.detect(html)
html = html.decode(htmlCharset['encoding'])
#print(html)
strHtml = str(html)

soup = BeautifulSoup(html,"lxml")
resSet1 = soup.find_all(id='jgwab')	#这里返回类型是<class 'bs4.element.ResultSet'> 用法和原生set类似
print(resSet1[0].string)