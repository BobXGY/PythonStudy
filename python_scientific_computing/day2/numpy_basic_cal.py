import numpy as np

A = np.arange(2, 14).reshape((3, 4))

# 返回数据集中最值的索引
min_index = np.argmin(A)
max_index = np.argmax(A)
print('最小值的索引：{}\t最大值的索引：{}'.format(min_index, max_index))
