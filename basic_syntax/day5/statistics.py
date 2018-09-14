#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 数据统计


def inputNum():
    numArr = []
    thisNum = 0
    flag = False
    bsFlag = False

    while True:
        flag = False
        while not flag:
            try:
                thisNum = input('请输入一个数据,按enter结束输入')

                if thisNum == '':  # 空内容判断
                    bsFlag = True
                    break

                thisNum = float(thisNum)  # 输入不为空
                flag = True

            except ValueError:  # 输入不是数字
                print('ValueError')
                flag = False

        if bsFlag:
            break
        numArr.append(thisNum)
    return numArr


def avgF(numbers):  # 数字列表求平均值
    total = 0.0
    for x in numbers:
        total += x
    return total / len(numbers)


def devF(numbers):  # 求方差
    avg = avgF(numbers)
    total = 0.0
    for x in numbers:
        total += (x - avg) ** 2
    return total / len(numbers)


def sdevF(numbers):  # 求标准差
    return devF(numbers) ** 0.5


def midNumF(numbers):  # 求中位数
    sortedNumbers = sorted(numbers)
    lenth = len(sortedNumbers)
    isEven = lenth % 2
    if isEven == 0:
        return (sortedNumbers[lenth // 2 - 1] +
                sortedNumbers[lenth // 2]) / 2
    else:
        return sortedNumbers[lenth // 2]


numbers = inputNum()
print('平均数为：{:.2f}'.format(avgF(numbers)))
print('方差为：{:.2f}'.format(devF(numbers)))
print('标准差为：{:.2f}'.format(sdevF(numbers)))
print('中位数为：{:.2f}'.format(midNumF(numbers)))
