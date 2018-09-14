#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 用beautifulsoup查找标签

def main():
    from bs4 import BeautifulSoup
    import requests

    url = 'https://python123.io/ws/demo.html'
    try:
        requests_obj = requests.get(url)
        requests_obj.raise_for_status()
        requests_obj.encoding = requests_obj.apparent_encoding
        obj_txt = requests_obj.text
    except:
        print('err!')
        exit(0)

    soup = BeautifulSoup(obj_txt, 'html.parser')
    tag_a = soup.find_all('a')

    for i in tag_a:
        print(i)


if __name__ == "__main__":
    main()
