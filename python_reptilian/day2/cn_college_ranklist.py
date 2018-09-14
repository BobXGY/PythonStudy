#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 中国大学排行榜爬取

import bs4
import requests


def main():
    url = "http://zuihaodaxue.cn/zuihaodaxuepaiming2018.html"
    print('{}'.format('中国大学排名列表'.center(35, '=')))
    print('正在获取...', end='')

    ranklist = []
    html_txt = getHtmlTxet(url)
    print('\r', end='')
    if html_txt != 'err!':
        fillUList(ranklist, html_txt)
        printUList(ranklist, 100)
    else:
        print('网络错误！')


def getHtmlTxet(url):
    try:
        requests_obj = requests.get(url, timeout=300)
        requests_obj.raise_for_status()
        requests_obj.encoding = requests_obj.apparent_encoding
        return requests_obj.text
    except:
        return 'err!'


def fillUList(ulist, html_string):
    soup = bs4.BeautifulSoup(html_string, 'html.parser')
    for tr in soup.find('tbody'):
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[0].string, tds[1].string, tds[2].string, tds[3].string])


def printUList(ulist, top_n):
    count = 0
    print("{:^10}\t{:　^12}{:^}".format('排名', '学校名称', '省市'))
    for item in ulist:
        print("{:^10}\t{:　<12}{:<}".format(item[0], item[1], item[2]))
        count += 1
        if count == top_n:
            break


if __name__ == '__main__':
    main()
