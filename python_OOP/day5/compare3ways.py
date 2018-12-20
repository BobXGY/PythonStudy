#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 用一系列运算测试一下多进程多线程和普通方法的速度
from multiprocessing import Process, Queue
from threading import Thread
import time


# 待解决问题：尝试过将子进程、线程函数分别装入 多进程计算主函数 和 多线程计算主函数
# 会导致程序报错
""""""


# 普通方法计算
def normal(number):
    res = 0
    for i in range(number):
        res = res + i + i ** 2 + i ** 3 + i ** 4
    return res


# 在多进程/线程中将计算任务拆分成两部分
def job1(q, number):
    """ 计算任务1 """
    res = 0
    for i in range(number):
        res = res + i + i ** 2 + i ** 3
    q.put(res)


def job2(q, number):
    """ 计算任务2 """
    res = 0
    for i in range(number):
        res = res + i ** 4
    q.put(res)


# 多进程计算主函数
def mp(number, *args):
    queue = Queue()
    p1 = Process(target=args[0], args=(queue, number))
    p2 = Process(target=args[1], args=(queue, number))
    p1.start()
    p2.start()
    p2.join()
    p1.join()

    return queue.get() + queue.get()


# 多线程计算主函数
def mt(number, *args):
    queue = Queue()
    t1 = Thread(target=args[0], args=(queue, number))
    t2 = Thread(target=args[1], args=(queue, number))
    t1.start()
    t2.start()
    t2.join()
    t1.join()
    return queue.get() + queue.get()


def main():
    # 计算1-n的平方、立方、四次方的和
    number = 10000000

    time_normalstart = time.time()
    normal_res = normal(number)
    time_normalend = time.time()
    print('普通计算：\n用时:{}s\n结果:{}\n'.format(time_normalend - time_normalstart, normal_res))

    time_mpstart = time.time()
    mp_res = mp(number, job1, job2)
    time_mpend = time.time()
    print('多进程：\n用时:{}s\n结果:{}\n'.format(time_mpend - time_mpstart, mp_res))

    time_mtstart = time.time()
    mt_res = mt(number, job1, job2)
    time_mtend = time.time()
    print('多线程：\n用时:{}s\n结果:{}\n'.format(time_mtend - time_mtstart, mt_res))


if __name__ == '__main__':
    main()
