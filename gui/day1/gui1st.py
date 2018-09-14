#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author   : Bob
# @file     : gui1st.py
# @time     : 2018/9/14   10:54
# @editor   : PyCharm

# pyqt5
import sys
from PyQt5.QtWidgets import QApplication, QWidget


if __name__ == '__main__':
    app1 = QApplication(sys.argv)
    w = QWidget()
    w.resize(600, 480)
    w.move(100, 100)
    w.setWindowTitle('app1')
    w.show()
    sys.exit(app1.exec_())
