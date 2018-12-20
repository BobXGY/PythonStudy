#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @author Bob
# @create time 2018/11/28 23:03
# @file mouse.py
# @software PyCharm
import win32api
import win32con
import win32gui
import time


if __name__ == '__main__':
    QQ = win32gui.FindWindow("TXGuiFoundation", "QQ")
    wnd_rect = win32gui.GetWindowRect(QQ)
    print(wnd_rect)

    win32api.SetCursorPos((wnd_rect[0] + 45, wnd_rect[1] + 75))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    time.sleep(0.7)

    my_info = win32gui.FindWindow("TXGuiFoundation", "我的资料")
    win32gui.SetForegroundWindow(my_info)
    wnd_rect = win32gui.GetWindowRect(my_info)
    win32api.SetCursorPos((wnd_rect[0] + 330, wnd_rect[1] + 330))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    time.sleep(0.7)

    win32api.SetCursorPos((1135, 500))
    loop = 100
    while loop:
        i = 10
        while i:
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
            time.sleep(0.1)
            i -= 1

        # win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, 0, 0, -100, 0)
        loop -= 1
    pass
