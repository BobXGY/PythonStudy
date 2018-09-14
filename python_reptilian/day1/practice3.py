#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 百度搜索结果爬取

import requests
baidu_search_url = 'https://www.baidu.com/s'
key_word = 'python'
key_values = {'wd': key_word}

headers = {'user-agent': 'Mozilla/5.0'}

try:
    baidu_search_robj = requests.get(baidu_search_url, params=key_values)
    baidu_search_robj.raise_for_status()
    baidu_search_robj.encoding = baidu_search_robj.apparent_encoding
    baidu_search_text = baidu_search_robj.text
except:
    print('错误')

print(baidu_search_robj.request.url)
print(baidu_search_text)
