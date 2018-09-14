#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# bilibili搜索结果爬取

import requests

bilibili_url = 'https://search.bilibili.com/all'
kvp = {'keyword': 'python'}
ua = {'user-agent': 'Mozilla/5.0'}
bilibili_robj = requests.get(bilibili_url, params=kvp, headers=ua)

print(bilibili_robj.text)
print(bilibili_robj.request.url)
print(len(bilibili_robj.text))
print(bilibili_robj.request.headers)
