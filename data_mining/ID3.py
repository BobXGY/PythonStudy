#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import math


class DataSample(object):
    def __init__(self, **arg):
        self.arg = arg

    def __str__(self):
        return str(self.arg['index'])

    __repr__ = __str__


class TreeNode(object):
    def __init__(self, parent='root', children=None, key=''):
        if children is None:
            children = []
        self.p = parent
        self.children = children
        self.div_key = key

    def set_div_key(self, key):
        self.div_key = key

    def add_children(self, node):
        self.children.append(node)


def div_func(data_list: list, parent=None):
    if len(data_list) == 0:
        return

    info_gain = dict()  # 存放信息增益的键值对字典

    for attr in data_list[0].arg.keys():  # 尝试分类
        if attr in ['index', 'play']:  # 跳过序号属性
            continue

        temp_list = data_list.copy()
        # print('根据{}列分类'.format(attr))

        attr_set = set()
        for it in temp_list:  # 获取这一种属性的所有值
            attr_set.add(it.arg[attr])
        # print('    列的属性值有{}'.format(attr_set))

        div_dict = {}  # 创建分类容器
        for it in temp_list:
            div_dict[it.arg[attr]] = list()

        for it in temp_list:  # 分类
            div_dict[it.arg[attr]].append(it)
        this_info_gain = cal_info_gain(temp_list, div_dict)
        # print('   分类结果:', div_dict)
        # print('       信息增益为{}'.format(this_info_gain))
        # print('-------------------')
        info_gain[attr] = this_info_gain

    max_info_gain = max(info_gain.values())
    convert_dict = {v: k for k, v in info_gain.items()}
    div_by = convert_dict[max_info_gain]
    print('父节点：{}\n     按{}分类的信息增益最大，为{}'.format(parent, div_by, max_info_gain))

    real_div = {}  # 真实分类容器
    for it in data_list:
        real_div[it.arg[div_by]] = list()

    for it in data_list:  # 开始真实分类
        real_div[it.arg[div_by]].append(it)

    node = TreeNode(children=list(real_div.keys()), key=div_by)

    print('      {}'.format(real_div))
    print('***************')
    for key, li in real_div.items():
        flag = True
        temp = li[0].arg['play']
        get_index = []
        for it in li:
            # global flag
            get_index.append(it.arg['index'])
            if it.arg['play'] != temp:
                flag = False
                break
            else:
                continue
        if flag:
            for it in data_list:
                if it.arg['index'] in get_index:
                    data_list.pop(data_list.index(it))
        else:
            div_func(li, parent=div_by)
    print('')


def cal_entropy(data_list: list):
    lenth = len(data_list)
    t, f = 0, 0
    for it in data_list:
        if it.arg['play']:
            t += 1
        else:
            f += 1
    # 考虑等于0的情况(类型全部分开)，熵等于0
    if t == 0 or f == 0:
        return 0
    else:
        sigma = -((t / lenth) * math.log(t / lenth, 2) + (f / lenth) * math.log(f / lenth, 2))
    return sigma


def cal_info_gain(parent_list: list, dived_complex_list: dict):
    sigma = 0.0
    for ch_list in dived_complex_list.values():
        sigma += len(ch_list) / len(parent_list) * cal_entropy(ch_list)
    return cal_entropy(parent_list) - sigma


if __name__ == '__main__':
    mydata_list = [
        DataSample(index=1, outlook='sunny', temp='hot', humidity='high', windy=False, play=False),
        DataSample(index=2, outlook='sunny', temp='hot', humidity='high', windy=True, play=False),
        DataSample(index=3, outlook='overcast', temp='hot', humidity='high', windy=False, play=True),
        DataSample(index=4, outlook='rainy', temp='mid', humidity='high', windy=False, play=True),
        DataSample(index=5, outlook='rainy', temp='cool', humidity='normal', windy=False, play=True),
        DataSample(index=6, outlook='rainy', temp='cool', humidity='normal', windy=True, play=False),
        DataSample(index=7, outlook='overcast', temp='cool', humidity='normal', windy=True, play=True),
        DataSample(index=8, outlook='sunny', temp='mid', humidity='high', windy=False, play=False),
        DataSample(index=9, outlook='sunny', temp='cool', humidity='normal', windy=False, play=True),
        DataSample(index=10, outlook='rainy', temp='mid', humidity='normal', windy=False, play=True),
        DataSample(index=11, outlook='sunny', temp='mid', humidity='normal', windy=True, play=True),
        DataSample(index=12, outlook='overcast', temp='mid', humidity='high', windy=True, play=True),
        DataSample(index=13, outlook='overcast', temp='hot', humidity='normal', windy=False, play=True),
        DataSample(index=14, outlook='rainy', temp='mid', humidity='high', windy=True, play=False)
    ]

    div_func(mydata_list)
