#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Author  :   心道不止（OSHO）
# @License :   (C) Copyright 2019-2021, 天地无极
# @Contact :   xiaoxiaolong1989@foxmail.com
# @Software:   PyCharm
# @File    :   MusicListManager.py
# @Time    :   2020/6/11 23:22
# @Desc    :
from PySide2.QtCore import QUrl, QObject
from PySide2.QtMultimedia import QMediaPlaylist


class MusicListManager(QObject):

    def __init__(self):
        self.playlist = QMediaPlaylist()

    def addLocalMedia(self, path):
        self.playlist.addMedia(QUrl.fromLocalFile(path))

    def addNetworkMedia(self, url):
        self.playlist.addMedia(QUrl(url))

    def setPlayMode(self, PlaybackMode):
        self.playlist.setPlaybackMode(PlaybackMode)

    def musicPlayList(self):
        return self.playlist



