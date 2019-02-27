#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @author Bob
# @create time 2019/1/6 14:50
# @file sign_up.py
import requests
import os

if __name__ == '__main__':
    url = 'https://kiwifree.pw/user/checkin'
    my_cookies = {'__cfduid': 'df60855bb71a10cdb1da75f3fab31a6a01534082192',
                  'uid': '3196',
                  'email': '736385398%40qq.com',
                  'key': 'ed188373e1208fc6c648b5cbe8d9419d211b2625ebf45',
                  'ip': 'de5e1874b1c265275c69e723f9ac940f',
                  'expire_in': '1552656429'
                  }
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                             'AppleWebKit/537.36 (KHTML, like Gecko)'
                             'Chrome/71.0.3578.98 Safari/537.36'
               }
    print("正在连接到" + url + "...")
    resp = requests.post(url=url, cookies=my_cookies, headers=headers)

    if resp.json()['msg'] == '您似乎已经续命过了...':
        print('今天已经签过到了...')
    elif resp.json()['msg'][:3] == '获得了':
        gain = int(resp.json()['msg'][4:-6])
        print('获得流量：' + str(gain))
    else:
        print(resp.content.decode('utf-8'))
    os.system("pause")
