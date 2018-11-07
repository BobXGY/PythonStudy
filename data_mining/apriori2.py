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
            fre_1set_li.append(term)

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


# 根据频繁k项集列表生成频繁k+1项集列表
def gen_next_fre_set_li(previous_fre_set_li: list, fre_1_set_li: list, min_sup: int):
    """
    :param previous_fre_set_li: 频繁k项集
    :param fre_1_set_li: 频繁1项集
    :param min_sup: 最小支持度计数
    :return: 频繁k+1项集
    """
    next_candidate_set_li = []
    # 添加逻辑：以频繁k项集列表为基础，往里其中每个项集中添加频繁1-项集中的事务，形成k+1项候选集
    for p_record in previous_fre_set_li:
        for fre_1_set_record in fre_1_set_li:
            n_set = p_record[0] | fre_1_set_record[0]
            # 添加新的项集规则：
            # 1.{'A'}里面加入'A'是无效的，相当于没有添加事务，对应下方规则     n_set != p_record[0]
            # 2.避免多次组合出相同项集，须检查是否已经添加过这个组合了，对应下方规则[n_set, 0] not in next_candidate_set_li
            if n_set != p_record[0] and [n_set, 0] not in next_candidate_set_li:
                next_candidate_set_li.append([n_set, 0])

    next_fre_set_li = []
    for n_record in next_candidate_set_li:
        n_record[1] = get_support(n_record[0], my_data_list)

    for n_record in next_candidate_set_li:
        if n_record[1] >= min_sup:
            next_fre_set_li.append(n_record)
    return next_fre_set_li


# 生成规则
def gen_rule(fre_k_set: list, h: list, min_conf: int):
    """

    :param fre_k_set: 频繁K-项集
    :param h: 规则后件
    :param min_conf: 最低置信度计数
    :return: 包含规则的列表
    """
    rule_list = []
    if len(fre_k_set[0]) > len(h[0][0]):
        for h_n in h:
            k_set_without_h = fre_k_set[0] - h_n[0]
            if k_set_without_h | h_n[0] == k_set_without_h:
                continue
            # 计算去掉h的项集的支持度
            suppor_without_h = get_support(k_set_without_h, my_data_list)
            conf = fre_k_set[1] / suppor_without_h
            if conf > min_conf:
                rule_list.append([k_set_without_h, h_n[0]])
    return rule_list


def gen_k_rules(all_fre_set_li: list):
    for fre_set_li in all_fre_set_li:
        h = all_fre_set_li[0]
        gen_rule()
        pass
    pass


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
    __sample__fre_li = [
        [{'A', 'B'}, 2],
        [{'A', 'C'}, 4]
    ]

    # 设置最低支持度计数
    min_support = 4
    print("最低支持度计数设置为", min_support)

    fre_1_set_li = gen_f1set_li(my_data_list, 3)
    print('频繁1-项集:')
    for record in fre_1_set_li:
        print(record)

    all_li = [fre_1_set_li]

    current_li = fre_1_set_li
    i = 1
    while current_li:
        current_li = gen_next_fre_set_li(current_li, fre_1_set_li, 3)
        all_li.append(current_li)
        i += 1
        print('频繁{}-项集：'.format(i))
        for record in current_li:
            print(record)

    rule_find_list = gen_rule(all_li[1][0], fre_1_set_li, 0)

    print('-' * 50)
    print("生成的规则：")
    for rule in rule_find_list:
        print('{} -> {}'.format(rule[0], rule[1]))
