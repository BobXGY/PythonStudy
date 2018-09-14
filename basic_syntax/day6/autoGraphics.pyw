#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 根据文件自动轨迹绘制

import turtle


def gdraw(cmd):
    if cmd[-1] >= 1:
        turtle.pendown()
        turtle.pensize(cmd[0])
        colortp = (cmd[1][0] / 255.0,  # 颜色预处理，文件中RGB取值为区间[0,255]
                   cmd[1][1] / 255.0,
                   cmd[1][2] / 255.0)
        turtle.pencolor(colortp)  # pencolor方法接受一个3元组对应RGB，值在区间[0,1]
        turtle.right(cmd[2])
        turtle.fd(cmd[3])
        turtle.penup()
    else:
        turtle.penup()
        turtle.right(cmd[2])
        turtle.fd(cmd[3])


def openFile():
    while True:
        try:
            fileName = input('输入要打开的文件名(当前目录下，含扩展名)\n')
            file = open(fileName, mode='rt')  # 取得文件句柄
            return file
        except:
            print('输入错误')


def prepLine(file):
    thisLine = file.readline()
    return thisLine.replace(' ', '')           #去空格


def main():
    file = openFile()
    turtle.setup(854, 480, 0, 0)
    while True:
        thisLine = prepLine(file)
        if thisLine == '':                          #文件结束
            break
        if thisLine == '\n' or thisLine[0] == '#':  #跳过空行和注释行
            continue
        gdraw(eval(thisLine))

    turtle.done()


main()
