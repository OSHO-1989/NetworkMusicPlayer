# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FormLocalMusicList.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_FormLocalMusicList(object):
    def setupUi(self, FormLocalMusicList):
        if not FormLocalMusicList.objectName():
            FormLocalMusicList.setObjectName(u"FormLocalMusicList")
        FormLocalMusicList.resize(918, 652)
        self.verticalLayout_2 = QVBoxLayout(FormLocalMusicList)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.leftPictureLabel = QLabel(FormLocalMusicList)
        self.leftPictureLabel.setObjectName(u"leftPictureLabel")
        self.leftPictureLabel.setMinimumSize(QSize(200, 200))
        self.leftPictureLabel.setMaximumSize(QSize(200, 200))

        self.horizontalLayout_2.addWidget(self.leftPictureLabel)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.explainTitleLabel = QLabel(FormLocalMusicList)
        self.explainTitleLabel.setObjectName(u"explainTitleLabel")
        font = QFont()
        font.setFamily(u"\u5fae\u8f6f\u96c5\u9ed1")
        font.setPointSize(24)
        self.explainTitleLabel.setFont(font)

        self.verticalLayout.addWidget(self.explainTitleLabel)

        self.explainContextTextEdit = QTextEdit(FormLocalMusicList)
        self.explainContextTextEdit.setObjectName(u"explainContextTextEdit")
        font1 = QFont()
        font1.setFamily(u"\u5fae\u8f6f\u96c5\u9ed1")
        font1.setPointSize(13)
        self.explainContextTextEdit.setFont(font1)
        self.explainContextTextEdit.setAutoFillBackground(True)
        self.explainContextTextEdit.setStyleSheet(u"QTextEdit#explainContextTextEdit\n"
"{\n"
"	background-color: rgb(0, 0, 0);\n"
"}")
        self.explainContextTextEdit.setReadOnly(True)

        self.verticalLayout.addWidget(self.explainContextTextEdit)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.playAllButton = QToolButton(FormLocalMusicList)
        self.playAllButton.setObjectName(u"playAllButton")
        self.playAllButton.setFont(font1)

        self.horizontalLayout.addWidget(self.playAllButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.horizontalLayout_2.addLayout(self.verticalLayout)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.musicTableView = QTableView(FormLocalMusicList)
        self.musicTableView.setObjectName(u"musicTableView")

        self.verticalLayout_2.addWidget(self.musicTableView)

        self.verticalLayout_2.setStretch(1, 1)

        self.retranslateUi(FormLocalMusicList)

        QMetaObject.connectSlotsByName(FormLocalMusicList)
    # setupUi

    def retranslateUi(self, FormLocalMusicList):
        FormLocalMusicList.setWindowTitle(QCoreApplication.translate("FormLocalMusicList", u"Form", None))
        self.leftPictureLabel.setText(QCoreApplication.translate("FormLocalMusicList", u"TextLabel", None))
        self.explainTitleLabel.setText(QCoreApplication.translate("FormLocalMusicList", u"TextLabel", None))
        self.explainContextTextEdit.setHtml(QCoreApplication.translate("FormLocalMusicList", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'\u5fae\u8f6f\u96c5\u9ed1'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'SimSun'; font-size:9pt; background-color:#1e1e1e;\"><br /></p></body></html>", None))
        self.playAllButton.setText(QCoreApplication.translate("FormLocalMusicList", u"\u5168\u90e8\u64ad\u653e", None))
    # retranslateUi

