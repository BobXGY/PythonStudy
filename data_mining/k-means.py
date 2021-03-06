#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @author Bob
# @create time 2018/10/24 10:05
# @file k-means.py
# @software PyCharm
"""
# 数据结构设计
# 数据点存储为tuple类型
# 原始数据为装有tuple的列表
data_list = [(4.63, 30.46), (11.36, 14.58),
             (31.15, 39.6), (43.33, 96.68),
             (25.24, 70.65), (46.13, 19.81),
             (22.39, 58.25), (17.39, 80.83),
             (63.8, 56.79), (93.46, 93.18),
             (90.18, 80.57), (13.61, 87.32),
             (44.23, 70.62), (98.77, 48.79),
             (31.41, 62.5), (85.87, 12.12),
             (74.84, 23.13), (14.48, 64.83),
             (76.19, 66.21), (74.03, 7.86)]
# 簇以集合形式存储在簇列表中
__sample_clusters__ = [{(4.63, 30.46), (11.36, 14.58)},
                       {(76.19, 66.21)},
                       {}]

# 质心存储为列表
__sample_cores__ = [(31.41, 62.5), (74.03, 7.86), (13.61, 87.32)]
"""

from random import random, sample
from math import pow


def cal_dist(core: tuple, dot: tuple):
    """
    计算两个点之间的欧氏距离
    :param core: 质心坐标 (x,y) 类型为tuple
    :param dot:  要计算距离的点(m,n) 类型为tuple
    :return: 距离 dist 类型为float
    """
    dist = pow(((dot[0] - core[0]) ** 2 + (dot[1] - core[1]) ** 2), 0.5)
    return dist


def cal_cluster(dot: tuple, cores: list):
    """
    计算给定点应该指派到哪一个质心
    :param dot: 待处理的点
    :param cores: 质心列表
    :return: 应该指派到的质心的序号
    """
    distance_list = []
    for core in cores:
        dist = cal_dist(core, dot)
        distance_list.append(dist)

    min_dist = min(distance_list)
    put_to_index = distance_list.index(min_dist)
    return put_to_index


def init_cores(row_data: list, k: int):
    """
    根据原始数据生成初始质心
    :param row_data: 原始数据
    :param k: k值
    :return: 质心列表
    """
    cores = sample(row_data, k)
    return cores


def put_dot_into_clusters(row_data: list, k: int, cores: list):
    """
    将点指派至最近质心的簇
    :param cores:
    :param row_data:
    :param k:
    :return: 已分配点的簇
    """
    clusters = []
    for each in range(k):
        clusters.append(set())

    for each_data in row_data:
        index = cal_cluster(each_data, cores)
        clusters[index].add(each_data)

    return clusters


def re_cal_core(cluster: set):
    """
    计算当前簇的下一个质心
    :param cluster:
    :return:
    """
    all_x = []
    all_y = []
    for each_dot in cluster:
        all_x.append(each_dot[0])
        all_y.append(each_dot[1])
    avg_x = sum(all_x) / len(all_x)
    avg_y = sum(all_y) / len(all_y)
    new_core = (round(avg_x, 2), round(avg_y, 2))
    return new_core


if __name__ == '__main__':
    # 生成n个点
    data_list = []
    for num in range(10):
        adot = (round(random() * 20 - 100, 2), round(random() * 20 - 100, 2))
        data_list.append(adot)

    for num in range(100):
        adot = (round(random() * 100 + 100, 2), round(random() * 50 + 150, 2))
        data_list.append(adot)

    for num in range(50):
        adot = (round(random() * 20, 2), round(random() * 20, 2))
        data_list.append(adot)

    for num in range(50):
        adot = (round(random() * 100 + 100, 2), round(random() * 20, 2))
        data_list.append(adot)

    for num in range(100):
        adot = (round(random() * 200, 2), round(random() * 200, 2))
        data_list.append(adot)

    # 设置k值
    k = 4
    # 生成初始质心
    my_cores = init_cores(data_list, k)
    print("初始质心：")
    print(my_cores)

    roundx = 0
    while True:
        roundx += 1
        # 指派
        cl = put_dot_into_clusters(data_list, k, my_cores)
        print("第{}次迭代".format(roundx))
        print("簇：")
        for cluster in cl:
            print(cluster)

        # 重新计算质心
        new_cores = list()
        for index in range(k):
            new_cores.append(re_cal_core(cl[index]))
        print("质心：")
        print(new_cores)

        print('-' * 100)
        if new_cores == my_cores:
            break
        else:
            my_cores = new_cores

    import matplotlib.pyplot as plt

    colors = ['#0000FF', '#FF0000', '#00FF00', '#666666', '#FFFF00']
    for index in range(k):
        color = colors[index % 5]
        for each_dot in cl[index]:
            plt.scatter(each_dot[0], each_dot[1], c=color, alpha=0.5)
        plt.scatter(my_cores[index][0], my_cores[index][1], marker='+', c='#000000', s=180)
    plt.show()
