#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Author  :   心道不止（OSHO）
# @License :   (C) Copyright 2019-2021, 天地无极
# @Contact :   xiaoxiaolong1989@foxmail.com
# @Software:   PyCharm
# @File    :   AudioPlayManage.py
# @Time    :   2020/6/11 23:30
# @Desc    :
from PySide2.QtCore import QObject
from PySide2.QtMultimedia import QMediaPlayer


class AudioPlayManager(QObject):
    def __init__(self):
        self.player = QMediaPlayer()

    def setAudioPlayList(self, AudioList):
        self.player.setPlaylist(AudioList)

    def startPlay(self):
        self.player.play()

    def stopPlay(self):
        self.player.stop()

    def pausePlay(self):
        self.player.pause()

    def setVolume(self, volume):
        self.player.setVolume(volume)
