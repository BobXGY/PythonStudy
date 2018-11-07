import numpy as np

if __name__ == '__main__':
    # 创建一个numpy数据集，numpy数据集中元素的类型必须相同
    # 传入参数 dtype(意为data type) 为np.int (当然还有int64 float32 float64 默认为32位)
    array = np.array([[1, 2, 3],
                      [2, 3, 4]], dtype=np.int)
    print(array)
    print('数据集的维度（当前这个数据是一个矩阵，矩阵是二维的）：', array.ndim)
    print('数据集的形状（长宽高等）：', array.shape)
    print('数据集中数据的数量：', array.size)
    print('数据集中数据的类型：', array.dtype)

    # 定义一个全零的数据集
    zeros = np.zeros((3, 4, 5), dtype=np.int32)
    print(zeros)

    # 定义一个全一的数据集
    ones = np.ones((4, 3), dtype=np.int32)
    print(ones)

    # 定义一个空数据集(实际上生成的数据集中的元素全都是接近于0的数字)
    empty = np.empty((3, 3), dtype=float)
    print(empty)
    """
    这里如果把dtype传入整型（int16, int32, int64等）会得到随机值    
        猜想：
        这个方法可能是把申请到的内存单元中的值视为浮点数
        并且只更改阶码的符号位让阶码为负值。以此达到加快执行速度的目的。
        所以如果指定为整型则会直接将数据视为整型处理
    """

    # 生成递增（递减）数组，用法类似于[x for x in range(a, b)]
    ordered_array = np.arange(10, 20, 2)
    print(ordered_array)

    # 重置数据集形状
    reshaped_array = np.arange(0, 20, 1).reshape((4, 5))
    print(reshaped_array)

    # 生成一个线段(其实是用离散化的点模拟的线段, 第三个参数表示点的个数)
    line = np.linspace(1, 3, 10)
    print(line)

    # 生成具有随机值数据的数据集
    random_set = np.random.random((2, 3))
    print(random_set)
