#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Author  :   心道不止（OSHO）
# @License :   (C) Copyright 2019-2021, 天地无极
# @Contact :   xiaoxiaolong1989@foxmail.com
# @Software:   PyCharm
# @File    :   FormApplicationTitleBar.py
# @Time    :   2020/5/31 15:56
# @Desc    :
from PySide2.QtCore import Signal, Qt
from PySide2 import (QtCore, QtWidgets)
from PySide2.QtCore import QSize
from PySide2.QtGui import QPixmap, QFont, QCursor
from PySide2.QtWidgets import QSizePolicy, QHBoxLayout, QApplication, QVBoxLayout

import ApplicationResources_rc

class FormApplicationTitleBar(QtWidgets.QWidget):
    # 定义成员变量和类变量

    # 定义信号
    minButtonClicked = Signal()
    maxButtonClicked = Signal()
    closeButtonClicked = Signal()

    def __init__(self):
        super().__init__()
        self.mainLayout = QVBoxLayout()
        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        self.mainLayout.setMargin(0)
        self.titleFrame = QtWidgets.QFrame()
        self.titleFrame.setObjectName("titleFrame")
        self.titleFrame.setContentsMargins(0, 0, 0, 0)
        self.titleBoxLayout = QtWidgets.QHBoxLayout()
        self.titleBoxLayout.setMargin(0)
        self.titleBoxLayout.setContentsMargins(0, 0, 0, 0)

        self.leftSpaceItem = QtWidgets.QSpacerItem(3, 20, QSizePolicy.Fixed)
        self.middleSpaceItem = QtWidgets.QSpacerItem(5, 20, QSizePolicy.Expanding)
        self.minButton = QtWidgets.QToolButton()
        self.minButton.setObjectName("minButton")
        self.maxButton = QtWidgets.QToolButton()
        self.maxButton.setObjectName("maxButton")
        self.closeButton = QtWidgets.QToolButton()
        self.closeButton.setObjectName("closeButton")
        self.appIconLabel = QtWidgets.QLabel()
        self.appIconLabel.setFixedSize(QSize(25, 25))
        self.appIconLabel.setScaledContents(True)
        self.appIconLabel.setPixmap(QPixmap(':/icon/Resources/icon/icon-music.png'))
        self.titleContextLabel = QtWidgets.QLabel("网络音乐播放器")
        self.titleContextLabel.setObjectName('titleContextLabel')
        self.contextFont = QFont('微软雅黑', 11)
        self.titleContextLabel.setFont(self.contextFont)
        self.rightSpaceItem = QtWidgets.QSpacerItem(5, 20, QSizePolicy.Fixed)
        self.titleBoxLayout.addItem(self.leftSpaceItem)
        self.titleBoxLayout.addWidget(self.appIconLabel)
        self.titleBoxLayout.addWidget(self.titleContextLabel)
        self.titleBoxLayout.addItem(self.middleSpaceItem)
        self.titleBoxLayout.addWidget(self.minButton)
        self.titleBoxLayout.addWidget(self.maxButton)
        self.titleBoxLayout.addWidget(self.closeButton)
        self.titleBoxLayout.addItem(self.rightSpaceItem)
        self.titleBoxLayout.setSpacing(20)
        self.titleFrame.setLayout(self.titleBoxLayout)
        self.mainLayout.addWidget(self.titleFrame)
        self.setLayout(self.mainLayout)

        self.__connectSignalsAndSlots()


    def __connectSignalsAndSlots(self):
        self.minButton.clicked.connect(self.minButtonClicked)
        self.maxButton.clicked.connect(self.maxButtonClicked)
        self.closeButton.clicked.connect(self.closeButtonClicked)

