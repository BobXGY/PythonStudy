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


if __name__ == '__main__':
    # 数据结构设计
    # 原始数据集安排为一个列表，项集以集合形式存入列表
    my_data_list = [
        {'A', 'B', 'C'},
        {'A', 'C', 'D'},
        {'B', 'C', 'D'},
        {'A', 'B', 'C', 'D', 'E'},
        {'A', 'C', 'E'},
        {'B', 'D', 'E'},
        {'C', 'D'}
    ]
    # 频繁k-项集/k-候选集 格式如下：
    __sample__fre_li = [
        [{'A', 'B'}, 2],
        [{'A', 'C'}, 4]
    ]

    # 设置最低支持度计数
    min_support = 4

    fre_1_set_li = gen_f1set_li(my_data_list, 3)
    print('频繁1-项集:')
    for record in fre_1_set_li:
        print(record)

    current_li = fre_1_set_li
    i = 1
    while current_li:
        current_li = gen_next_fre_set_li(current_li, fre_1_set_li, 3)
        i += 1
        print('频繁{}-项集：'.format(i))
        for record in current_li:
            print(record)
