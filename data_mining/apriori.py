#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 产生频繁1-项集
def gen_f1set_li(row_set_li: list, min_sup: int):
    """
    :param row_set_li: 原始数据集列表
    :param min_sup: 最小支持度计数
    :return: 频繁1-项集列表
    """
    candidate_1set_li = []
    for term in row_set_li:
        for item in term:
            tag = False
            for fre_1set_term in candidate_1set_li:
                if item in fre_1set_term[0]:
                    tag = True
                    fre_1set_term[1] += 1
                    break
            if not tag:
                candidate_1set_li.append([{item}, 1])

    fre_1set_li = []
    for term in candidate_1set_li:
        if term[1] >= min_sup:
            fre_1set_li.append(term[0])

    return fre_1set_li


# 根据原始数据集计算候选集的支持度计数
def get_support(candidate_set: set, row_set_li: list):
    """
    :param candidate_set: 候选集
    :param row_set_li: 原始数据集
    :return: 支持度计数
    """
    support = 0
    for row_set in row_set_li:
        if candidate_set | row_set == row_set:
            support += 1
    return support


# 根据频繁k项集列表生成频繁k+1项集的候选集列表
def gen_next_candidate_set_li(previous_fre_set_li: list, fre_1_set_li: list):
    """
    :param previous_fre_set_li: 频繁k项集
    :param fre_1_set_li: 频繁1项集
    :return: k+1项候选集集
    """
    next_candidate_set_li = []
    # 添加逻辑：以频繁k项集列表为基础，往里其中每个项集中添加频繁1-项集中的事务，形成k+1项候选集
    for fre_k_set in previous_fre_set_li:
        for fre_1_set in fre_1_set_li:
            new_set = fre_k_set | fre_1_set
            # 添加新的项集规则：
            # 1.{'A'}里面加入'A'是无效的，相当于没有添加事务，对应下方规则     new_set != fre_k_set[0]
            # 2.避免多次组合出相同项集，须检查是否已经添加过这个组合了，对应下方规则[new_set, 0] not in next_candidate_set_li
            if new_set != fre_k_set and new_set not in next_candidate_set_li:
                next_candidate_set_li.append(new_set)
    return next_candidate_set_li


def gen_next_fre_set_li(candidate_set_li: list, row_data_set_li: list, min_sup: int):
    """

    :param candidate_set_li: k候选集
    :param row_data_set_li: 原始数据集
    :param min_sup: 最小支持度
    :return: 频繁k项集
    """
    next_fre_set_li = []

    for candidate_set in candidate_set_li:
        if get_support(candidate_set, row_data_set_li) >= min_sup:
            next_fre_set_li.append(candidate_set)
    return next_fre_set_li


def gen_rule(fre_k_set: set, h: list, min_conf: int):
    """
    :param fre_k_set:
    :param h:
    :param min_conf:
    :return:
    """
    rule_list = []
    # print(fre_k_set, h)
    if len(fre_k_set) > len(h[0]):
        for each_in_h in h:
            k_set_without_h = fre_k_set - each_in_h
            if k_set_without_h == fre_k_set:
                continue
            support = get_support(fre_k_set, my_data_list)
            # 计算去掉h的项集的支持度
            support_without_h = get_support(k_set_without_h, my_data_list)
            conf = support / support_without_h
            # print(k_set_without_h, '->', each_in_h, conf, '\n', '-' * 50)
            if conf > min_conf:
                rule_list.append([k_set_without_h, each_in_h, conf])
    return rule_list


def gen_k_rules(fre_k_set_li: list, h: list, min_conf: int):
    k_rules = []
    for fre_set_li in fre_k_set_li:
        if fre_set_li == h:
            continue
        arule = gen_rule(fre_set_li, h, min_conf)
        k_rules.extend(arule)
    return k_rules


if __name__ == '__main__':
    # 数据结构设计
    # 原始数据集安排为一个列表，项集以集合形式存入列表
    my_data_list = [
        {'A', 'B', 'C', 'D'},
        {'A', 'C', 'D'},
        {'B', 'C', 'D'},
        {'A', 'B', 'C', 'D', 'E'},
        {'A', 'C', 'D'},
        {'B', 'D', 'E'},
        {'C', 'D', 'E'}
    ]
    # 频繁k-项集/k-候选集 格式如下：
    __sample__fre_2_li = [
        {'A', 'B'},
        {'A', 'C'}
    ]

    # 设置最低支持度计数
    min_support = 4

    fre_1_set_li = gen_f1set_li(my_data_list, 3)
    print('频繁1-项集:')
    for record in fre_1_set_li:
        print(record)

    all_li = [fre_1_set_li]

    fre_k_set_li = fre_1_set_li
    k = 1
    while fre_k_set_li:
        candidate_set_li = gen_next_candidate_set_li(fre_k_set_li, fre_1_set_li)
        fre_k_set_li = gen_next_fre_set_li(candidate_set_li, my_data_list, 3)
        all_li.append(fre_k_set_li)
        k += 1
        print('频繁{}-项集：'.format(k))
        for record in fre_k_set_li:
            print(record)

    rules = gen_k_rules(all_li[1], fre_1_set_li, 0)
    print('-' * 50)
    for each_rule in rules:
        print('{} --> {} conf: {:1.3}'.format(each_rule[0], each_rule[1], each_rule[2]))
