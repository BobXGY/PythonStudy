import numpy as np

if __name__ == '__main__':
    a = np.arange(0, 5)
    b = np.array([1, -29, -2, 51, 3])
    # 四则运算：将每个对应位置的数据相运算
    c = a - b
    print(c)
    c = c * 10
    print(c)
    print('-' * 100)

    # 三角函数 默认为弧度
    PI = 3.1415926
    arr = np.array([PI, np.pi, np.pi / 2, 2])
    print('sin:', np.sin(arr))
    print('cos:', np.cos(arr))
    print('tan:', np.tan(arr))
    print('-' * 100)

    # 矩阵点乘
    matrix_1 = np.array([[1, 0],
                         [4, 1]])
    matrix_2 = np.array([[1, 2],
                         [3, 1]])
    # 方法1
    matrix_3 = np.dot(matrix_1, matrix_2)
    print(matrix_3)
    # 方法2
    matrix_3 = matrix_1.dot(matrix_2)
    print(matrix_3)
    print('-' * 100)

    # 数据集求和、取最值等
    max_in_m3 = np.max(matrix_3)
    min_in_m3 = np.min(matrix_3)
    sum_of_m3 = np.sum(matrix_3)
    avg_of_m3 = np.average(matrix_3)
    print('max: {} min: {} sum: {} avg: {}'.format(max_in_m3, min_in_m3, sum_of_m3, avg_of_m3))
    # 另外两种求平均值的(等价)方法
    avg1 = np.mean(matrix_3)
    avg2 = matrix_3.mean()
    print('另外两种方法求得的平均值为：', avg1, avg2)
    # 逐行求和、最值等 加入关键字参数axis=0
    # 逐列求和axis=1
    max_by_rows = np.max(matrix_3, axis=0)
    sum_by_cols = np.sum(matrix_3, axis=1)
    print(max_by_rows, sum_by_cols)
    print('-' * 100)
