#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 哔哩哔哩图片爬取并存入硬盘

import requests
import os

url = 'http://i0.hdslb.com/bfs/archive/ae2096cea16c9ddffb650f57ee4edc21b4b0cdba.png'
save_name = url.split('/')[-1]
save_path = '''F:\学习\计算机科学与技术\Python\python_reptilian\day1\\''' + save_name

try:
    robj = requests.get(url)
    # print(robj.status_code)
    if not os.path.exists(save_path):           # 判断是否存在同名文件
        with open(save_path, 'wb') as f:
            f.write(robj.content)
        f.close()
    else:
        print('文件已存在')
except:
    print('网络错误')
