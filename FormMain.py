#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Author  :   心道不止（OSHO）
# @License :   (C) Copyright 2019-2021, 天地无极
# @Contact :   xiaoxiaolong1989@foxmail.com
# @Software:   PyCharm
# @File    :   FormMain.py
# @Time    :   2020/5/16 21:59
# @Desc    :

from PySide2 import (QtWidgets)
from PySide2.QtCore import Qt
from PySide2.QtGui import QCursor, QFont
from PySide2.QtWidgets import (QSizePolicy, QLabel, QVBoxLayout, QHBoxLayout, QToolButton, QSlider)

import FormApplicationTitleBar
import FormCenterWidgetContext
import FormPlayControlToolBar

class FormMain(QtWidgets.QMainWindow):
    # 窗口最大化标志
    windowMaxFlag = False

    def __init__(self):
        super().__init__()

        # 自定义标题栏
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Window)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setWindowTitle("网络音乐播放器")
        self.topFrame = QtWidgets.QFrame()
        self.topFrame.setObjectName("topFrame")
        self.setCentralWidget(self.topFrame)

        self.topLayout = QtWidgets.QVBoxLayout()

        # 1.标题栏布局
        self.appTitleBar = FormApplicationTitleBar.FormApplicationTitleBar()
        self.appTitleBar.setFixedHeight(25)

        # 2.中间主体显示内容
        self.midContextWidget = FormCenterWidgetContext.FormMidContextWidget()

        # 3.控制条部分内容
        self.controlToolBar = FormPlayControlToolBar.FormPlayControlToolBar()
        self.controlToolBar.setFixedHeight(70)

        self.topLayout.setStretch(0, 0)
        self.topLayout.setStretch(1, 1)
        self.topLayout.setStretch(2, 0)
        self.topLayout.setContentsMargins(1,1,1,1)
        self.topLayout.addWidget(self.appTitleBar)
        self.topLayout.addWidget(self.midContextWidget)
        self.topLayout.addWidget(self.controlToolBar)
        self.topLayout.setMargin(3)

        self.topFrame.setLayout(self.topLayout)

        self.connectSignalsAndSlots()


    def connectSignalsAndSlots(self):
        '''
        连接信号与槽
        :return:
        '''
        self.appTitleBar.minButtonClicked.connect(self.showMinimized)
        self.appTitleBar.maxButtonClicked.connect(self.__changeWindowSize)
        self.appTitleBar.closeButtonClicked.connect(self.close)


    def showMaximizedSlot(self):
        self.showMaximized()


    def showNormalSlot(self):
        self.showNormal()


    def __changeWindowSize(self):
        '''
        窗口在最大化和窗口化之间切换
        :return:
        '''
        if self.windowMaxFlag == False:
            self.showMaximized()
            self.windowMaxFlag = True
        else:
            self.showNormal()
            self.windowMaxFlag = False


    def mousePressEvent(self, QMouseEvent):
        '''
        鼠标按下
        '''
        if QMouseEvent.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_Position = QMouseEvent.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            QMouseEvent.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))  # 更改鼠标图标


    def mouseMoveEvent(self, QMouseEvent):
        '''
        鼠标移动
        '''
        if Qt.LeftButton and self.m_flag:
            if self.windowMaxFlag == False:
                self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
                QMouseEvent.accept()


    def mouseReleaseEvent(self, QMouseEvent):
        '''
        鼠标释放
        '''
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))


    def mouseDoubleClickEvent(self, QMouseEvent):
        if self.m_Position.y() <= self.appTitleBar.rect().height():
            if self.windowMaxFlag == False:
                self.showMaximized()
                self.windowMaxFlag = True
            else:
                self.showNormal()
                self.windowMaxFlag = False