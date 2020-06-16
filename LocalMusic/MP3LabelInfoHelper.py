#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Author  :   心道不止（OSHO）
# @License :   (C) Copyright 2019-2021, 天地无极
# @Contact :   xiaoxiaolong1989@foxmail.com
# @Software:   PyCharm
# @File    :   MP3LabelInfoHelper.py
# @Time    :   2020/6/14 18:57
# @Desc    :
from mutagen.mp3 import MP3
import os

class MP3LabelInfoHelper():
    '''获取歌曲信息'''
    def __init__(self, path):
        songFile = MP3(path)
        self.getTitle(songFile, path)
        self.getArtist(songFile)
        self.getAlbum(songFile)
        self.getLength(songFile)

    def getTitle(self, songFile, path):
        '''获取歌曲名
        songFile:文件对象
        path:文件地址
        '''
        try:
            self.title = str(songFile.tags['TIT2'])
        except:
            filename = os.path.basename(path)  # 从地址中获取文件名
            self.title = filename.split('.')[0]  # 去掉文件名后缀

    def getArtist(self,songFile):
        '''获取歌手名
        songFile:文件对象
        '''
        try:
            self.artist=str(songFile.tags['TPE1'])
        except:
            self.artist=''

    def getAlbum(self,songFile):
        '''获取专辑名
        songFile:文件对象
        '''
        try:
            self.album=str(songFile.tags['TALB'])
        except:
            self.album=''

    def getLength(self,songFile):
        '''获取文件播放时时长'''
        timeLength = int(songFile.info.length)
        mintime = timeLength//60  #转换为分钟
        sectime = timeLength % 60 #剩余的转换为秒
        if sectime < 10:
            sectime='0'+ str(sectime)
        else:
            sectime=str(sectime)
        self.length=str(mintime)+":"+sectime

