#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 爬中国天气网的天气
# version = 2
from bs4 import BeautifulSoup
from requests import get as req_get
import time


def get_html_text(url=      'http://www.weather.com.cn/weather/101270401.shtml',
                  encoding= 'utf-8'):
    try:
        robj = req_get(url)
        robj.raise_for_status()
        robj.encoding = encoding
        return robj.text
    except:
        return 'err!'


def get_weather_info_list_from_html_text(html_text):
    soup = BeautifulSoup(html_text, 'html.parser')
    weather_info_list = []
    for wea in soup.find_all('p', class_='wea'):
        weather_info_list.append([wea.string])

    count = 0
    for tem in soup.find_all('p', class_='tem'):
        for one in tem.children:
            if one.string != '\n' and one.string != '/':
                weather_info_list[count].append(one.string)
        count += 1
    return weather_info_list


def main():
    html_text = get_html_text()
    lt = get_weather_info_list_from_html_text(html_text)
    print('{:=^50}'.format('绵阳天气'))
    day_flag = ['今天', '明天', '后天', '第四天', '第五天', '第六天', '第七天']
    count = 0
    for day in lt:
        print('{:　<10}{:　<10}{:>16}'.format(day_flag[count], day[0], day[1]+'/'+day[-1]))
        count += 1
    print('{:=^54}'.format(''))
    print('{: >46}'.format('数据来源：中央气象台'))
    print('{: >54}'.format(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))))


if __name__ == '__main__':
    main()
