#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Author  :   心道不止（OSHO）
# @License :   (C) Copyright 2019-2021, 天地无极
# @Contact :   xiaoxiaolong1989@foxmail.com
# @Software:   PyCharm
# @File    :   main.py
# @Time    :   2020/5/16 21:40
# @Desc    :   网络音乐播放区主界面
import json
import sys

import requests as requests
from PySide2 import QtWidgets
from PySide2.QtCore import QIODevice, QFile

from FormMain import FormMain
from NeteaseCloudMusic.EntityClass.MusicMediaPropertyEntity import MusicMediaPropertyEntity


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

    # # 以下为GET请求
    # url = 'http://www.wanghu21.xyz:3000/song/url?id=1451661639'
    # requests = requests.get(url)
    # jsonObject = json.loads(requests.content)
    #
    # dataEntiy = MusicMediaPropertyEntity()
    # dataEntiy.setId(jsonObject["data"][0]["id"])
    # dataEntiy.setUrl(jsonObject["data"][0]["url"])
    # dataEntiy.setFileSize(jsonObject["data"][0]["size"])
    # dataEntiy.setMd5(jsonObject["data"][0]["md5"])
    # dataEntiy.setCode(jsonObject["data"][0]["code"])
    # dataEntiy.setExpiTime(jsonObject["data"][0]["expi"])
    # dataEntiy.setFileType(jsonObject["data"][0]["type"])
    # dataEntiy.setGain(jsonObject["data"][0]["gain"])
    # dataEntiy.setFee(jsonObject["data"][0]["fee"])
    # dataEntiy.setUf(jsonObject["data"][0]["uf"])
    # dataEntiy.setPayed(jsonObject["data"][0]["payed"])
    # dataEntiy.setFlag(jsonObject["data"][0]["flag"])
    # dataEntiy.setCanExtend(jsonObject["data"][0]["canExtend"])
    # dataEntiy.setFreeTrialInfo(jsonObject["data"][0]["freeTrialInfo"])
    # dataEntiy.setLevel(jsonObject["data"][0]["level"])
    # dataEntiy.setEncodeType(jsonObject["data"][0]["encodeType"])
    #
    # print(dataEntiy.getId())
    # print(dataEntiy.getUrl())
    # print(dataEntiy.getFileSize())
    # print(dataEntiy.getMd5())
    # print(dataEntiy.getCode())
    # print(dataEntiy.getExpiTime())
    # print(dataEntiy.getFileType())
    # print(dataEntiy.getGain())
    # print(dataEntiy.getFee())
    # print(dataEntiy.getUf())
    # print(dataEntiy.getPayed())
    # print(dataEntiy.getFlag())
    # print(dataEntiy.getCanExtend())
    # print(dataEntiy.getFreeTrialInfo())
    # print(dataEntiy.getLevel())
    # print(dataEntiy.getEncodeType())


    widget = FormMain()
    widget.setStyleSheet(str(applicationStyle))
    widget.resize(1366, 768)
    widget.setMaximumSize(1920, 1080)
    widget.show()

    sys.exit(app.exec_())
