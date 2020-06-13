#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Author  :   心道不止（OSHO）
# @License :   (C) Copyright 2019-2021, 天地无极
# @Contact :   xiaoxiaolong1989@foxmail.com
# @Software:   PyCharm
# @File    :   FormLocalMusicList.py
# @Time    :   2020/6/13 15:27
# @Desc    :
from PySide2 import QtWidgets
from PySide2.QtGui import QPixmap, QPalette, QColor

from LocalMusic.ui_FormLocalMusicList import Ui_FormLocalMusicList


class FormLocalMusicList(QtWidgets.QWidget):
    def __init__(self, parent = None):
        super(FormLocalMusicList, self).__init__(parent)

        self.ui = Ui_FormLocalMusicList()
        self.ui.setupUi(self)

        self.__initForm()

    def __initForm(self):
        self.ui.leftPictureLabel.setScaledContents(True)
        self.ui.leftPictureLabel.setPixmap(QPixmap(":/icon/Resources/icon/icon-localmusiclogo.svg"))
        self.ui.explainTitleLabel.setText("本地音乐")
        self.ui.explainContextTextEdit.setPlainText("本地音乐的理论可以对任何音乐创作、任何音乐表演，作出评论和解释。音乐家无论是创作还是表演，都要以己乡或他乡的音乐素材作为依据去进行艺术创作。没有乡音、没有国籍、没有母系的“作品”不是“创新”，世上没有无根之木，也没有无源之水，只有民族的，才是国际的。")