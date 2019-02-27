#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @author Bob
# @create time 2019/2/25 18:08
# @file cookies_test.py
# @software PyCharm

# 用于测试接收到的cookies的DEMO
from requests import post, utils


if __name__ == '__main__':
    url = 'https://www.baidu.com/'

    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                             'AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/71.0.3578.98 Safari/537.36'
               }

    resp = post(url=url, headers=headers)

    cookies_dict = utils.dict_from_cookiejar(resp.cookies)

    if cookies_dict:
        print(cookies_dict)
