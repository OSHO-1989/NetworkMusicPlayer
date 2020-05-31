#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Author  :   心道不止（OSHO）
# @License :   (C) Copyright 2019-2021, 天地无极
# @Contact :   xiaoxiaolong1989@foxmail.com
# @Software:   PyCharm
# @File    :   FormLocalMusicContext.py
# @Time    :   2020/5/31 20:58
# @Desc    :
from PySide2 import QtWidgets
from PySide2.QtWidgets import QFrame


class FormLocalMusicContext(QtWidgets.QWidget):
    #定义成员变量

    #定义自定义信号

    def __init__(self):
        super().__init__()


    def __initForm(self):
        self.localMusicMainFrame = QFrame()
