#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @author Bob
# @create time 2018/11/15 17:05
# @file Spider.py
# @software PyCharm


from urllib import request
from bs4 import BeautifulSoup


class NovelGet(object):
    def __init__(self, url):
        self.html = ''
        self.tag_string = ''
        self.url = url

    def get_html(self):
        rep = request.urlopen(self.url)
        html_content = rep.read()
        html_content = str(html_content, encoding='utf-8')
        self.html = html_content
        return self.html

    def get_text(self):
        soup = BeautifulSoup(self.html, 'html.parser')
        read_tag = soup.find('div', class_='j_readContent')
        self.tag_string = str(read_tag.contents[1])
        self.tag_string = self.tag_string.replace('<p>', '\n').replace('</p>', '')
        return self.tag_string
