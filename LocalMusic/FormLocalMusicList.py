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
from PySide2.QtCore import Qt
from PySide2.QtGui import QPixmap, QPalette, QColor, QStandardItemModel, QStandardItem
from PySide2.QtWidgets import QHeaderView, QAbstractItemView

from LocalMusic.ui_FormLocalMusicList import Ui_FormLocalMusicList


class FormLocalMusicList(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(FormLocalMusicList, self).__init__(parent)
        self.ui = Ui_FormLocalMusicList()
        self.ui.setupUi(self)

        self.__initForm()

    def __initForm(self):
        self.ui.leftPictureLabel.setScaledContents(True)
        self.ui.leftPictureLabel.setPixmap(QPixmap(":/icon/Resources/icon/icon-localmusiclogo.svg"))
        self.ui.explainTitleLabel.setText("本地音乐")
        self.ui.explainContextTextEdit.setAutoFillBackground(False)
        self.ui.explainContextTextEdit.setPlainText(
            "本地音乐的理论可以对任何音乐创作、任何音乐表演，作出评论和解释。音乐家无论是创作还是表演，都要以己乡或他乡的音乐素材作为依据去进行艺术创作。没有乡音、没有国籍、没有母系的“作品”不是“创新”，世上没有无根之木，也没有无源之水，只有民族的，才是国际的。")
        self.MusicListModel = QStandardItemModel()
        self.MusicListModel.setColumnCount(2)
        self.MusicListModel.setHorizontalHeaderItem(0, QStandardItem("序号"))
        self.MusicListModel.setHorizontalHeaderItem(1, QStandardItem("路径"))
        self.MusicListModel.setHorizontalHeaderItem(2, QStandardItem("唱片集"))
        self.MusicListModel.setHorizontalHeaderItem(3, QStandardItem("艺术家"))
        self.MusicListModel.setHorizontalHeaderItem(4, QStandardItem("时长"))
        self.ui.musicTableView.setModel(self.MusicListModel)
        self.ui.musicTableView.verticalHeader().hide()
        self.ui.musicTableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.musicTableView.setSelectionMode(QAbstractItemView.SingleSelection)
        self.ui.musicTableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.musicTableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.musicTableView.setAlternatingRowColors(True)
        self.ui.musicTableView.verticalHeader().setDefaultSectionSize(30)
        self.ui.musicTableView.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)

    def setPlayList(self, playList):
        index = 1
        for name in playList:
            indexColumnItem = QStandardItem(str(name.index))
            indexColumnItem.setTextAlignment(Qt.AlignHCenter)
            pathColumnItem = QStandardItem(name.musicPath)
            collectionRecordsColumnItem = QStandardItem(name.collectionRecords)
            artistColumnItem = QStandardItem(name.artist)
            timeColumnItem = QStandardItem(name.time)
            itemList = []
            itemList.append(indexColumnItem)
            itemList.append(pathColumnItem)
            itemList.append(collectionRecordsColumnItem)
            itemList.append(artistColumnItem)
            itemList.append(timeColumnItem)
            self.MusicListModel.appendRow(itemList)
            index = index + 1

        self.ui.musicTableView.selectRow(0)
