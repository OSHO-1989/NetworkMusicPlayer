#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Author  :   心道不止（OSHO）
# @License :   (C) Copyright 2019-2021, 天地无极
# @Contact :   xiaoxiaolong1989@foxmail.com
# @Software:   PyCharm
# @File    :   FormPlayControlToolBar.py
# @Time    :   2020/5/31 19:48
# @Desc    :
from PySide2 import QtWidgets
from PySide2.QtCore import Qt, QUrl
from PySide2.QtGui import QFont
from PySide2.QtMultimedia import QMediaPlayer
from PySide2.QtWidgets import QHBoxLayout, QVBoxLayout, QSizePolicy, QToolButton, QLabel, QSlider


class FormPlayControlToolBar(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.__initForm()
        self.__PlayAudioFile()


    def __initForm(self):
        self.mainLayout = QHBoxLayout()
        self.mainLayout.setContentsMargins(0, 0 , 0, 0)
        self.controlBarFrame = QtWidgets.QFrame()
        self.textFont = QFont("微软雅黑", 11)

        # 整体布局
        self.toolBarLayout = QHBoxLayout()
        self.toolBarLayout.setContentsMargins(20,2,20,2)

        # 1.播放控住部分布局
        self.leftControlLayout = QVBoxLayout()
        self.leftControlLayout.setContentsMargins(0, 0, 0, 0)
        self.toolBarLeftTopSpaceItem = QtWidgets.QSpacerItem(3, 20, QSizePolicy.Expanding)
        self.toolBarLeftLeftSpaceItem = QtWidgets.QSpacerItem(3, 20, QSizePolicy.Expanding)
        self.toolBarLeftRightSpaceItem = QtWidgets.QSpacerItem(3, 20, QSizePolicy.Expanding)
        self.toolBarLeftButtomSpaceItem = QtWidgets.QSpacerItem(3, 20, QSizePolicy.Expanding)
        self.prevMusicButton = QToolButton()
        self.prevMusicButton.setFixedSize(25, 25)
        self.prevMusicButton.setObjectName("prevMusicButton")
        self.prevMusicButton.setToolTip("上一首")
        self.playMusicButton = QToolButton()
        self.playMusicButton.setFixedSize(30, 30)
        self.playMusicButton.setObjectName("playMusicButton")
        self.playMusicButton.setToolTip("播放")
        self.stopMusicButton = QToolButton()
        self.stopMusicButton.setFixedSize(37, 30)
        self.stopMusicButton.setObjectName("stopMusicButton")
        self.stopMusicButton.setToolTip("停止")
        self.nextMusicButton = QToolButton()
        self.nextMusicButton.setFixedSize(25, 25)
        self.nextMusicButton.setObjectName("nextMusicButton")
        self.nextMusicButton.setToolTip("下一首")
        self.leftControlLayout.addItem(self.toolBarLeftTopSpaceItem)
        self.leftMidHBoxLayout = QHBoxLayout()
        self.leftMidHBoxLayout.setSpacing(12)
        self.leftMidHBoxLayout.addItem(self.toolBarLeftLeftSpaceItem)
        self.leftMidHBoxLayout.addWidget(self.prevMusicButton)
        self.leftMidHBoxLayout.addWidget(self.playMusicButton)
        self.leftMidHBoxLayout.addWidget(self.stopMusicButton)
        self.leftMidHBoxLayout.addWidget(self.nextMusicButton)
        self.leftMidHBoxLayout.addItem(self.toolBarLeftButtomSpaceItem)

        # 2.工具条中间部分布局
        self.midTopVBoxlayout = QVBoxLayout()
        self.midTopVBoxlayout.setContentsMargins(0, 0, 0, 0)
        self.midTopVBoxlayout.setSpacing(10)
        self.midtopHBoxLayout = QHBoxLayout()
        self.midtopHBoxLayout.setContentsMargins(0, 0, 0, 0)
        # 第一行
        self.playingSongButton = QToolButton()
        self.playingSongButton.setFont(self.textFont)
        self.playingSongButton.setFixedHeight(30)
        self.playingSongButton.setText("正在播放")
        self.playingSongButton.setObjectName("playingSongButton")
        self.playingSongButton.setFont(self.textFont)
        self.playingSongContextLabel = QLabel()
        self.playingSongContextLabel.setObjectName("playingSongContextLabel")
        self.playingSongContextLabel.setFont(self.textFont)
        self.playingSongContextLabel.setText("你是我拒绝别人的理由")
        self.midtopmidSpaceItem = QtWidgets.QSpacerItem(3, 20, QSizePolicy.Expanding)
        self.shoucangToolButton = QToolButton()
        self.shoucangToolButton.setObjectName("shoucangToolButton")
        self.shoucangToolButton.setFixedSize(25, 25)
        self.mvVideoToolButton = QToolButton()
        self.mvVideoToolButton.setObjectName("mvVideoToolButton")
        self.mvVideoToolButton.setFixedSize(25, 30)
        self.downToolButton = QToolButton()
        self.downToolButton.setObjectName("downToolButton")
        self.downToolButton.setFixedSize(25, 30)
        self.midtopHBoxLayout.addWidget(self.playingSongButton)
        self.midtopHBoxLayout.addWidget(self.playingSongContextLabel)
        self.midtopHBoxLayout.addItem(self.midtopmidSpaceItem)
        self.midtopHBoxLayout.addWidget(self.shoucangToolButton)
        self.midtopHBoxLayout.addWidget(self.mvVideoToolButton)
        self.midtopHBoxLayout.addWidget(self.downToolButton)
        #第二行
        self.midBottomHBoxLayout = QHBoxLayout()
        self.playedTimeLabel = QLabel("00:00:00")
        self.playedTimeLabel.setObjectName("playedTimeLabel")
        self.playedTimeLabel.setFont(self.textFont)
        self.horizontalSlider = QSlider(Qt.Horizontal)
        self.totalTimeLabel = QLabel("00:06:28")
        self.totalTimeLabel.setFont(self.textFont)
        self.midBottomHBoxLayout.addWidget(self.playedTimeLabel)
        self.midBottomHBoxLayout.addWidget(self.horizontalSlider)
        self.midBottomHBoxLayout.addWidget(self.totalTimeLabel)
        self.midTopVBoxlayout.addLayout(self.midtopHBoxLayout)
        self.midTopVBoxlayout.addLayout(self.midBottomHBoxLayout)

        # 右边播放列表部分
        self.rightControlLayout = QVBoxLayout()
        self.toolBarRightTopSpaceItem = QtWidgets.QSpacerItem(3, 20, QSizePolicy.Expanding)
        self.toolBarRightLeftSpaceItem = QtWidgets.QSpacerItem(3, 20, QSizePolicy.Expanding)
        self.toolBarRightRightSpaceItem = QtWidgets.QSpacerItem(3, 20, QSizePolicy.Expanding)
        self.toolBarRightButtomSpaceItem = QtWidgets.QSpacerItem(3, 20, QSizePolicy.Expanding)
        self.shunxuPlayButton = QToolButton()
        self.shunxuPlayButton.setObjectName("shunxuPlayButton")
        self.shunxuPlayButton.setToolTip("顺序播放")
        self.shunxuPlayButton.setFixedSize(25, 25)
        self.danquxunhuanPlayButton = QToolButton()
        self.danquxunhuanPlayButton.setObjectName("danquxunhuanPlayButton")
        self.danquxunhuanPlayButton.setToolTip("单曲循环")
        self.danquxunhuanPlayButton.setFixedSize(25, 25)
        self.sunjibofangPlayButton = QToolButton()
        self.sunjibofangPlayButton.setObjectName("sunjibofangPlayButton")
        self.sunjibofangPlayButton.setToolTip("随机播放")
        self.sunjibofangPlayButton.setFixedSize(25, 25)
        self.playListButton = QToolButton()
        self.playListButton.setObjectName("playListButton")
        self.playListButton.setToolTip("播放列表")
        self.playListButton.setFixedSize(25, 25)
        self.rightMidHBoxLayout = QHBoxLayout()
        self.rightMidHBoxLayout.setSpacing(10)
        self.rightMidHBoxLayout.addItem(self.toolBarRightLeftSpaceItem)
        self.rightMidHBoxLayout.addWidget(self.shunxuPlayButton)
        self.rightMidHBoxLayout.addWidget(self.danquxunhuanPlayButton)
        self.rightMidHBoxLayout.addWidget(self.sunjibofangPlayButton)
        self.rightMidHBoxLayout.addWidget(self.playListButton)
        self.rightMidHBoxLayout.addItem(self.toolBarRightRightSpaceItem)
        self.rightControlLayout.addItem(self.toolBarRightTopSpaceItem)
        self.rightControlLayout.addLayout(self.rightMidHBoxLayout)
        self.rightControlLayout.addItem(self.toolBarRightButtomSpaceItem)

        self.toolBarLayout.addLayout(self.leftMidHBoxLayout)
        self.secondLeftSpaceItem = QtWidgets.QSpacerItem(50, 20, QSizePolicy.Fixed)
        self.toolBarLayout.addItem(self.secondLeftSpaceItem)
        self.toolBarLayout.addLayout(self.midTopVBoxlayout)
        self.secondRightSpaceItem = QtWidgets.QSpacerItem(50, 20, QSizePolicy.Fixed)
        self.toolBarLayout.addItem(self.secondRightSpaceItem)
        self.toolBarLayout.addLayout(self.rightControlLayout)
        self.toolBarLayout.setStretch(0, 0)
        self.toolBarLayout.setStretch(1, 0)
        self.toolBarLayout.setStretch(2, 1)
        self.toolBarLayout.setStretch(3, 0)
        self.toolBarLayout.setStretch(4, 0)
        self.controlBarFrame.setLayout(self.toolBarLayout)
        self.mainLayout.addWidget(self.controlBarFrame)
        self.setLayout(self.mainLayout)


    def __PlayAudioFile(self):
        self.mediaPlayer = QMediaPlayer()
        self.mediaPlayer.setMedia(QUrl.fromLocalFile("E:/Test.mp3"))
        self.mediaPlayer.setVolume(50)
        self.mediaPlayer.play()