#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ip归属地查询

import requests
from bs4 import BeautifulSoup


def main():
    url = 'http://m.ip138.com/ip.asp'
    print('IP地址查询工具'.center(40, '='))
    myip = input('输入你要查询的ip地址：\n')

    paramsKV = {'ip': myip}
    try:
        robj = requests.get(url, params=paramsKV)
        robj.raise_for_status()
        robj.encoding = robj.apparent_encoding
        text = robj.text
    except:
        print('网络错误')
        exit(0)

    mysoup = BeautifulSoup(text, 'html.parser')
    res = mysoup.find_all('p', class_="result")
    try:
        print('物理地址查询结果：{}'.format(res[0].string[6:]))
    except:
        print('输入错误！')


if __name__ == '__main__':
    main()
