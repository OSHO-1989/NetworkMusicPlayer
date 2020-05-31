#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Author  :   心道不止（OSHO）
# @License :   (C) Copyright 2019-2021, 天地无极
# @Contact :   xiaoxiaolong1989@foxmail.com
# @Software:   PyCharm
# @File    :   FormCenterWidgetContext.py
# @Time    :   2020/5/31 15:59
# @Desc    :
from PySide2 import QtWidgets
from PySide2.QtGui import QFont, QPixmap, Qt, QStandardItem, QIcon, QStandardItemModel
from PySide2.QtWidgets import QHBoxLayout, QVBoxLayout, QLabel, QListView, QStackedWidget
from enum import Enum


class PageContextIndex(Enum):
    local_music_index = 0


class FormMidContextWidget(QtWidgets.QWidget):
    #定义成员变量

    #定义信号

    def __init__(self):
        super().__init__()

        self.__initForm()
        self.__loadMusicLibraryListWidgetData()
        self.__loadSongsNameListWidgetData()
        self.__loadCollectionMusicListWidgetData()


    def __initForm(self):
        self.mainLayout = QHBoxLayout()
        self.mainLayout.setContentsMargins(1,1,1,1)
        self.contextFrame = QtWidgets.QFrame()
        self.contextFrame.setObjectName("contextFrame")
        self.midContextLayout = QHBoxLayout()
        self.midContextLayout.setSpacing(1)
        self.midContextLayout.setContentsMargins(0, 1, 0, 1)
        self.midLeftFrame = QtWidgets.QFrame()
        self.midLeftFrame.setObjectName("midLeftFrame")
        self.midLeftLayout = QVBoxLayout()
        self.midLeftFrame.setLayout(self.midLeftLayout)
        self.midLeftLayout.setSpacing(0)
        self.midLeftLayout.setContentsMargins(2, 2, 2, 2)

        self.musicLibraryTitleLabel = QLabel("音乐库")
        self.textFont = QFont("微软雅黑", 11)
        self.textFont.setBold(True)
        self.musicLibraryTitleLabel.setFont(self.textFont)
        self.musicLibraryListView = QListView()
        self.musicLibraryListView.setFixedHeight(140)
        self.musicLibraryListView.setObjectName('musicLibraryListView')
        self.musicLibraryListView.setFixedWidth(190)

        self.localCollectionTitleLabel = QLabel("本地收藏")
        self.localCollectionTitleLabel.setFont(self.textFont)
        self.localCollectionListView = QListView()
        self.localCollectionListView.setObjectName('localCollectionListView')
        self.localCollectionListView.setFixedWidth(190)

        self.songsNameListTitleLabel = QLabel("歌单列表")
        self.songsNameListTitleLabel.setFont(self.textFont)
        self.songsNameListView = QListView()
        self.songsNameListView.setObjectName('songsNameListView')
        self.songsNameListView.setFixedWidth(190)
        self.songsNameListView.setFixedHeight(300)

        self.midLeftLayout.addWidget(self.musicLibraryTitleLabel)
        self.midLeftLayout.addWidget(self.musicLibraryListView)
        self.midLeftLayout.addWidget(self.songsNameListTitleLabel)
        self.midLeftLayout.addWidget(self.songsNameListView)
        self.midLeftLayout.addWidget(self.localCollectionTitleLabel)
        self.midLeftLayout.addWidget(self.localCollectionListView)
        self.rightContextStackWidget = QStackedWidget()
        self.testLabel = QLabel()
        self.testLabel.setScaledContents(True)
        self.testLabel.setPixmap(
            QPixmap(":/icon/Resources/icon/icon-meinv.jpg").scaled(self.testLabel.width(), self.testLabel.height(),
                                                                   Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.rightContextStackWidget.addWidget(self.testLabel)
        self.midContextLayout.addWidget(self.midLeftFrame)
        self.midContextLayout.addWidget(self.rightContextStackWidget)
        self.midContextLayout.setStretch(0, 0)
        self.midContextLayout.setStretch(1, 1)
        self.contextFrame.setLayout(self.midContextLayout)
        self.mainLayout.addWidget(self.contextFrame)
        self.setLayout(self.mainLayout)


    def __loadMusicLibraryListWidgetData(self):
        self.textFont = QFont("微软雅黑", 11)

        self.localMusicItemData = QStandardItem("本地音乐")
        self.localMusicItemData.setFont(self.textFont)
        self.localMusicItemData.setEditable(False)
        self.localMusicItemData.setData(QIcon(":/icon/Resources/icon/icon-localmusic.svg"), Qt.DecorationRole)

        self.wangyiYunItemData = QStandardItem("网易云音乐")
        self.wangyiYunItemData.setFont(self.textFont)
        self.wangyiYunItemData.setEditable(False)
        self.wangyiYunItemData.setData(QIcon(":/icon/Resources/icon/icon-wangyiyunmusic.svg"), Qt.DecorationRole)

        self.qqMusicItemData = QStandardItem("QQ音乐")
        self.qqMusicItemData.setFont(self.textFont)
        self.qqMusicItemData.setEditable(False)
        self.qqMusicItemData.setData(QIcon(":/icon/Resources/icon/icon-qqmusic.svg"), Qt.DecorationRole)

        self.xiaMiItemData = QStandardItem("虾米音乐")
        self.xiaMiItemData.setFont(self.textFont)
        self.xiaMiItemData.setEditable(False)
        self.xiaMiItemData.setData(QIcon(":/icon/Resources/icon/icon-xiamimusic.svg"), Qt.DecorationRole)

        self.musicLibraryModel = QStandardItemModel()
        self.musicLibraryModel.appendRow(self.localMusicItemData)
        self.musicLibraryModel.appendRow(self.wangyiYunItemData)
        self.musicLibraryModel.appendRow(self.qqMusicItemData)
        self.musicLibraryModel.appendRow(self.xiaMiItemData)

        self.musicLibraryListView.setSpacing(2)
        self.musicLibraryListView.setModel(self.musicLibraryModel)


    def __loadSongsNameListWidgetData(self):
        self.wubaiItemData = QStandardItem("伍佰&China blue")
        self.textFont = QFont("微软雅黑", 11)
        self.wubaiItemData.setFont(self.textFont)
        self.wubaiItemData.setEditable(False)
        self.wubaiItemData.setData(QIcon(":/icon/Resources/icon/icon-gedanlist.svg"), Qt.DecorationRole)

        self.zongguanxianItemData = QStandardItem("纵贯线")
        self.zongguanxianItemData.setFont(self.textFont)
        self.zongguanxianItemData.setEditable(False)
        self.zongguanxianItemData.setData(QIcon(":/icon/Resources/icon/icon-gedanlist.svg"), Qt.DecorationRole)

        self.zhaoleiItemData = QStandardItem("赵雷专辑")
        self.zhaoleiItemData.setFont(self.textFont)
        self.zhaoleiItemData.setEditable(False)
        self.zhaoleiItemData.setData(QIcon(":/icon/Resources/icon/icon-gedanlist.svg"), Qt.DecorationRole)

        self.xuweiItemData = QStandardItem("许巍专辑")
        self.xuweiItemData.setFont(self.textFont)
        self.xuweiItemData.setEditable(False)
        self.xuweiItemData.setData(QIcon(":/icon/Resources/icon/icon-gedanlist.svg"), Qt.DecorationRole)

        self.zhouhuajianItemData = QStandardItem("周华健专辑")
        self.zhouhuajianItemData.setFont(self.textFont)
        self.zhouhuajianItemData.setEditable(False)
        self.zhouhuajianItemData.setData(QIcon(":/icon/Resources/icon/icon-gedanlist.svg"), Qt.DecorationRole)

        self.banderuiItemData = QStandardItem("班得瑞专辑")
        self.banderuiItemData.setFont(self.textFont)
        self.banderuiItemData.setEditable(False)
        self.banderuiItemData.setData(QIcon(":/icon/Resources/icon/icon-gedanlist.svg"), Qt.DecorationRole)

        self.yaogunItemData = QStandardItem("摇滚专辑")
        self.yaogunItemData.setFont(self.textFont)
        self.yaogunItemData.setEditable(False)
        self.yaogunItemData.setData(QIcon(":/icon/Resources/icon/icon-gedanlist.svg"), Qt.DecorationRole)

        self.yinshiyuanshenItemData = QStandardItem("影视原声")
        self.yinshiyuanshenItemData.setFont(self.textFont)
        self.yinshiyuanshenItemData.setEditable(False)
        self.yinshiyuanshenItemData.setData(QIcon(":/icon/Resources/icon/icon-gedanlist.svg"), Qt.DecorationRole)

        self.minyaoItemData = QStandardItem("民谣专辑")
        self.minyaoItemData.setFont(self.textFont)
        self.minyaoItemData.setEditable(False)
        self.minyaoItemData.setData(QIcon(":/icon/Resources/icon/icon-gedanlist.svg"), Qt.DecorationRole)

        self.tianlaizhiyinItemData = QStandardItem("天籁之音")
        self.tianlaizhiyinItemData.setFont(self.textFont)
        self.tianlaizhiyinItemData.setEditable(False)
        self.tianlaizhiyinItemData.setData(QIcon(":/icon/Resources/icon/icon-gedanlist.svg"), Qt.DecorationRole)

        self.songsNameListModel = QStandardItemModel()
        self.songsNameListModel.appendRow(self.wubaiItemData)
        self.songsNameListModel.appendRow(self.zongguanxianItemData)
        self.songsNameListModel.appendRow(self.zhaoleiItemData)
        self.songsNameListModel.appendRow(self.xuweiItemData)
        self.songsNameListModel.appendRow(self.zhouhuajianItemData)
        self.songsNameListModel.appendRow(self.banderuiItemData)
        self.songsNameListModel.appendRow(self.yaogunItemData)
        self.songsNameListModel.appendRow(self.yinshiyuanshenItemData)
        self.songsNameListModel.appendRow(self.minyaoItemData)
        self.songsNameListModel.appendRow(self.tianlaizhiyinItemData)

        self.songsNameListView.setSpacing(2)
        self.songsNameListView.setModel(self.songsNameListModel)


    def __loadCollectionMusicListWidgetData(self):
        self.jingdianItemData = QStandardItem("经典老歌")
        self.textFont = QFont("微软雅黑", 11)
        self.jingdianItemData.setFont(self.textFont)
        self.jingdianItemData.setEditable(False)
        self.jingdianItemData.setData(QIcon(":/icon/Resources/icon/icon-collectionmusic.svg"), Qt.DecorationRole)

        self.qinyinyueItemData = QStandardItem("轻音乐系")
        self.qinyinyueItemData.setFont(self.textFont)
        self.qinyinyueItemData.setEditable(False)
        self.qinyinyueItemData.setData(QIcon(":/icon/Resources/icon/icon-collectionmusic.svg"), Qt.DecorationRole)

        self.jitaxilieItemData = QStandardItem("吉他系列")
        self.jitaxilieItemData.setFont(self.textFont)
        self.jitaxilieItemData.setEditable(False)
        self.jitaxilieItemData.setData(QIcon(":/icon/Resources/icon/icon-collectionmusic.svg"), Qt.DecorationRole)

        self.remengequItemData = QStandardItem("热门歌曲")
        self.remengequItemData.setFont(self.textFont)
        self.remengequItemData.setEditable(False)
        self.remengequItemData.setData(QIcon(":/icon/Resources/icon/icon-collectionmusic.svg"), Qt.DecorationRole)

        self.songsNameModel = QStandardItemModel()
        self.songsNameModel.appendRow(self.jingdianItemData)
        self.songsNameModel.appendRow(self.qinyinyueItemData)
        self.songsNameModel.appendRow(self.jitaxilieItemData)
        self.songsNameModel.appendRow(self.remengequItemData)
        self.localCollectionListView.setSpacing(2)
        self.localCollectionListView.setModel(self.songsNameModel)