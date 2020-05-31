#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Author  :   心道不止（OSHO）
# @License :   (C) Copyright 2019-2021, 天地无极
# @Contact :   xiaoxiaolong1989@foxmail.com
# @Software:   PyCharm
# @File    :   main.py
# @Time    :   2020/5/16 21:40
# @Desc    :   网络音乐播放区主界面

import sys

from PySide2 import QtWidgets
from PySide2.QtCore import QIODevice, QFile

from FormMain import FormMain


def importStyle():
    file = QFile(':/qss/Resources/qss/ApplicationStyle.qss')
    file.open(QIODevice.ReadOnly)
    applicationStyle = file.readAll()
    pyBytesStr = applicationStyle.data()
    styleStr = pyBytesStr.decode('utf-8')
    file.close()

    return styleStr


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    applicationStyle = importStyle()
    app.setStyleSheet(str(applicationStyle))

    widget = FormMain()
    widget.setStyleSheet(str(applicationStyle))
    widget.resize(1366, 768)
    widget.setMaximumSize(1920, 1080)
    widget.show()

    sys.exit(app.exec_())
