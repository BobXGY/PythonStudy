#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 爬中国天气网的天气

from urllib import request
from bs4 import BeautifulSoup
import chardet


def main():
    resp = request.urlopen('http://www.weather.com.cn/weather1d/101270401.shtml')
    html = resp.read()
    html = html.decode(chardet.detect(html)['encoding'])
    mySoup = BeautifulSoup(html, 'lxml')

    # print(mySoup)
    tempSet = mySoup.find_all('p', class_='tem')
    statSet = mySoup.find_all('p', class_='wea')
    # print(tempSet,statSet)

    # print(tempSet[0].span)

    dayTemp, dayStat, nightTemp, nightStat = tempSet[0].span.string, \
                                             statSet[0].string, \
                                             tempSet[1].span.string, \
                                             statSet[1].string

    print('绵阳\n\
今天白天{}，{}℃\n\
今天晚上{}，{}℃\n\
数据来源 中央气象台'.format(dayStat, dayTemp, nightStat, nightTemp))


if __name__ == '__main__':
    main()
