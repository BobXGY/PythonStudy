#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author   : Bob
# @file     : gui2nd.py
# @time     : 2018/9/14   16:46
# @editor   : PyCharm
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 这种静态的方法设置一个用于显示工具提示的字体。我们使用10px滑体字体。
        QToolTip.setFont(QFont('SansSerif', 10))
        # 创建一个提示，我们称之为settooltip()方法。我们可以使用丰富的文本格式
        self.setToolTip('This is a <b>QWidget</b> widget')
        # 创建一个PushButton并为他设置一个tooltip
        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        # btn.sizeHint()显示默认尺寸
        btn.resize(btn.sizeHint())
        # 移动按钮的位置
        btn.move(50, 50)

        # 退出按钮的实现
        quit_btn = QPushButton('QUIT', self)
        quit_btn.clicked.connect(QCoreApplication.instance().quit)
        quit_btn.resize(quit_btn.sizeHint())
        quit_btn.move(50, 100)

        self.setGeometry(100, 100, 600, 480)
        self.setWindowTitle('app')
        self.setWindowIcon(QIcon('icon.png'))
        self.show()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message',
                                     'Are you sure to quit?',
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
