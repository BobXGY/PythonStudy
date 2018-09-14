#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 京东商品信息爬取

import requests

jd_url = 'https://item.jd.com/7321794.html'
kvp = {'User-Agent': 'Chrome/50'}
try:
    robj_jd = requests.get(jd_url)
    robj_jd.raise_for_status()
    robj_jd.encoding = robj_jd.apparent_encoding
    jd_txt = robj_jd.text
except:
    print('错误')

print(jd_txt[:1000])
