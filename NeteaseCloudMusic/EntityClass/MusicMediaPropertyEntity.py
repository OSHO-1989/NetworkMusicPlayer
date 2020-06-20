#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Author  :   心道不止（OSHO）
# @License :   (C) Copyright 2019-2021, 天地无极
# @Contact :   xiaoxiaolong1989@foxmail.com
# @Software:   PyCharm
# @File    :   MusicMediaPropertyEntity.py
# @Time    :   2020/6/19 22:34
# @Desc    :
'''
{
  "data": [
    {
      "id": 1451661639,
      "url": "http://m7.music.126.net/20200619225157/ac7d0ae849a7ec192d47645d5913625c/ymusic/obj/w5zDlMODwrDDiGjCn8Ky/2695412238/dd40/17b8/5233/4dc5091a42810b96137c8ad92dca19c6.mp3",
      "br": 128000,
      "size": 3725997,
      "md5": "4dc5091a42810b96137c8ad92dca19c6",
      "code": 200,
      "expi": 1200,
      "type": "mp3",
      "gain": 0,
      "fee": 8,
      "uf": null,
      "payed": 0,
      "flag": 68,
      "canExtend": false,
      "freeTrialInfo": null,
      "level": "standard",
      "encodeType": "mp3"
    }
  ],
  "code": 200
}
'''
import self


class MusicMediaPropertyEntity():
    def setId(self, id):
        self.id = id

    def getId(self):
        return self.id

    def setUrl(self, url):
        self.url = url

    def getUrl(self):
        return self.url

    def setBr(self, br):
        self.br = br

    def getBr(self):
        return self.br

    def setFileSize(self, fileSize):
        self.fileSize = fileSize

    def getFileSize(self):
        return self.fileSize

    def setMd5(self, md5):
        self.md5 = md5

    def getMd5(self):
        return self.md5

    def setCode(self, code):
        self.code = code

    def getCode(self):
        return self.code

    def setExpiTime(self, expiTime):
        self.expiTime = expiTime

    def getExpiTime(self):
        return self.expiTime

    def setFileType(self, fileType):
        self.fileType = fileType

    def getFileType(self):
        return self.fileType

    def setGain(self, gain):
        self.gain = gain

    def getGain(self):
        return self.gain

    def setFee(self, fee):
        self.fee = fee

    def getFee(self):
        return self.fee

    def setUf(self, uf):
        self.uf = uf

    def getUf(self):
        return self.uf

    def setPayed(self, payed):
        self.payed = payed

    def getPayed(self):
        return self.payed

    def setFlag(self, flag):
        self.flag = flag

    def getFlag(self):
        return self.flag

    def setCanExtend(self, canExtend):
        self.canExtend = canExtend

    def getCanExtend(self):
        return self.canExtend

    def setFreeTrialInfo(self, freeTrialInfo):
        self.freeTrialInfo = freeTrialInfo

    def getFreeTrialInfo(self):
        return self.freeTrialInfo

    def setLevel(self, level):
        self.level = level

    def getLevel(self):
        return self.level

    def setEncodeType(self, encodeType):
        self.encodeType = encodeType

    def getEncodeType(self):
        return self.encodeType
