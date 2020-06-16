#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Author  :   心道不止（OSHO）
# @License :   (C) Copyright 2019-2021, 天地无极
# @Contact :   xiaoxiaolong1989@foxmail.com
# @Software:   PyCharm
# @File    :   MusicFileInfo.py
# @Time    :   2020/6/15 22:53
# @Desc    :


class MusicFileInfo():
    def __init__(self):
        #序号
        self.index = 0
        #mp3文件路径
        self.musicPath = ""
        #唱片集
        self.collectionRecords = ""
        #艺术家
        self.artist = ""
        #时长
        self.time = ""