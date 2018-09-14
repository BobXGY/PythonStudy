#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 创建最简单的子进程
from multiprocessing import Process, Queue
import os


# 将需要进程处理的代码放进这个函数
def while_process_run(queue, name):
    print('Process {} (pid:{}) starting...'.format(name, os.getpid()))
    queue.put('return结果')
# 这个函数不能用return来返回值（无法得到这个值）
# 实现类似return值的效果要借助一个传入的参数
# 这个参数就是用Queue()创建的一个变量


if __name__ == '__main__':
    q = Queue()
    p1 = Process(target=while_process_run, args=(q, 'test',))
    p1.start()
    p1.join()
    print('process ended.')
    print(q.get())
