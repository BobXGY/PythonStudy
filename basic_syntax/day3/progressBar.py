#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 文本进度条

import time


def textProgressBar():
    width = 100
    print('start！'.center(width // 2 * 2, '#'))
    startTime = time.perf_counter()
    for i in range(width + 1):
        a = '*' * i
        b = '.' * (width - i)
        c = (i / width) * 100
        time.sleep(0.01)
        timeUsed = time.perf_counter() - startTime
        print("\r{:>3.0f}%[{}->{}]{:.2f}s".format(c, a, b, timeUsed), end='')
    print('\nfinished!')


textProgressBar()
