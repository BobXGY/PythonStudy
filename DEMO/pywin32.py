#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @author Bob
# @create time 2018/11/28 21:07
# @file pywin32.py
# @software PyCharm
import win32api
import win32con
import win32gui
import time


def click_position(hwd, x_position, y_position):
    """
    鼠标左键点击指定坐标
    :param hwd:
    :param x_position:
    :param y_position:
    :return:
    """
    # 窗口移到前台
    win32gui.SetForegroundWindow(hwd)
    # 将两个16位的值连接成一个32位的地址坐标
    long_position = win32api.MAKELONG(x_position, y_position)
    print(long_position)
    # 点击左键
    win32api.SendMessage(hwd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, long_position)
    win32api.SendMessage(hwd, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, long_position)
    # time.sleep(1)


if __name__ == '__main__':
    # win32api.MessageBox(win32con.NULL, '我的第一个pywin32窗口！', 'Hello', win32con.MB_OK)

    # 模拟鼠标点击
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0)
    time.sleep(1)

    # 获取鼠标位置
    mpos = win32api.GetCursorPos()
    x, y = 960, 540

    # 获取窗口句柄
    hwnd = win32gui.FindWindow("MSPaintApp", "无标题 - 画图")
    win32gui.SetForegroundWindow(hwnd)  # 将窗口移至前台

    # 获得窗口位置和宽高
    wnd_rect = win32gui.GetWindowRect(hwnd)

    # 移动窗口 参数分别是 窗口句柄，窗口坐标x,y，窗口宽高w,h，是否重绘窗口
    # win32gui.MoveWindow(hwnd, wnd_rect[0], wnd_rect[1], 905, 756, True)

    # wnd_rect = win32gui.GetWindowRect(hwnd)
    print(wnd_rect)

    click_position(hwnd, wnd_rect[0] + 5, wnd_rect[1] + 5)
    click_position(hwnd, wnd_rect[0] + 5, wnd_rect[1] + 5)
    pass
