#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 正则表达式和正则表达式库： re
# 不使用bs4库而使用正则表达式处理爬取的信息

import re
import requests
import math


def get_html_text(url, data_dict=None):
    if data_dict is None:
        data_dict = {}
    try:
        requests_obj = requests.get(url, params=data_dict)
        requests_obj.raise_for_status()
        requests_obj.encoding = requests_obj.apparent_encoding
        text = requests_obj.text
        return text
    except:
        return 'err!'


def html_text_process(html_text):
    price_lt = re.findall(r'\"view_price\"\:\"[\d\.]*\"', html_text)
    title_lt = re.findall(r'\"raw_title\"\:\".*?\"', html_text)
    return_list = []
    try:
        for i in range(len(price_lt)):
            this_price = eval(price_lt[i].split(':')[1])
            this_title = eval(title_lt[i].split(':')[1])
            return_list.append([this_price, this_title])
        return return_list
    except:
        return return_list


def print_table(result_list, print_quantity):
    print('{:<8}{:<12}{:<50}'.format('序号', '价格', '名称'))
    try:
        for i in range(print_quantity):
            print('{:<8}{:<10}{:<40}'.format(i+1, result_list[i][0],result_list[i][1]))
    except IndexError:
        print('只找到{:^6}个结果({})'.format(i, print_quantity))
    if len(result_list) == 0:
        print('访问过于频繁，淘宝可能暂时禁止访问！')


def main():
    print('{:=^50}'.format('淘宝物品检索程序'))

    good = input('|{: ^48}|\n'.format('输入你要搜索的东西'))
    if good == '':
        good = '多皮哦'

    try:
        list_quantity = int(input('|{: ^48}|\n'.format('输入你要的结果数量')))
    except ValueError:
        list_quantity = 1

    pages = math.ceil(list_quantity//44) + 1    # 淘宝一页显示44个数据

    page_flag = 0
    data = {'q': good, 's': page_flag}
    url = 'https://s.taobao.com/search'

    print('爬取中...')
    result_list = []
    for page in range(0, pages):
        page_flag = str(pages * 44)
        txt = get_html_text(url, data)
        if txt == 'err!':
            print('网络错误')
            exit(0)
        processed_list = html_text_process(txt)
        result_list.extend(processed_list)

    print_table(result_list, list_quantity)


if __name__ == '__main__':
    main()
