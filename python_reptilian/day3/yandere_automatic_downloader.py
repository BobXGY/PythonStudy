#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 从yande.re随机爬图(popular页面)

from requests   import get
from urllib     import parse
from bs4        import BeautifulSoup
from random     import sample
from os         import path, system


def get_html_text(url=r'https://yande.re/post/popular_recent', encoding='utf-8'):
    try:
        robj = get(url)
        robj.raise_for_status()
        robj.encoding = encoding
        return robj.text
    except:
        print(-1)
        return 'err!'


def get_all_imgs_links(html_text):
    soup = BeautifulSoup(html_text, 'html.parser')
    a_tag_list = soup.find_all('a', class_='directlink largeimg')
    total_img_quantity = len(a_tag_list)
    link_list = []
    for i in range(total_img_quantity):
        link_list.append(a_tag_list[i]['href'])
    return link_list


def download_img_from_link(link):
    try:
        robj = get(link)
        robj.raise_for_status()
        file_name = parse.unquote(link.split('/')[-1])
        if not path.exists(file_name):
            with open(file_name, 'wb') as file:
                file.write(robj.content)
            return file_name
        else:
            return '文件已存在'
    except:
        return '网络错误'


def main():
    print('{:=^50}'.format('yande.re随机图片获取工具'))
    print('正在获取链接', end='')
    txt = get_html_text()
    img_link_list = get_all_imgs_links(txt)
    print('\r已经获取链接')

    img_quantity: int = 1
    try:
        img_quantity = int(input('输入需要的张数，推荐1张，不要超过5，因为很慢，真的很慢\n'))
    except ValueError:
        pass
    if img_quantity > 5 or img_quantity <= 0:
        img_quantity = 1

    random_link = sample(img_link_list, img_quantity)
    count = 0
    for link in random_link:
        count += 1
        print('正在下载第{}张'.format(count))
        file_name = download_img_from_link(link)
        print('保存为\t{}'.format(file_name))
    system('explorer {}'.format(path.dirname(__file__).replace('/', '\\')))


if __name__ == '__main__':
    main()
