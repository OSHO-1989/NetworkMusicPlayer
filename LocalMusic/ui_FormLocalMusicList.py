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
        font1.setPointSize(14)
        self.explainContextTextEdit.setFont(font1)
        self.explainContextTextEdit.setStyleSheet(u"QTextEdit#explainContextTextEdit\n"
"{\n"
"	\n"
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

        self.musicListWidget = QListWidget(FormLocalMusicList)
        self.musicListWidget.setObjectName(u"musicListWidget")

        self.verticalLayout_2.addWidget(self.musicListWidget)

        self.verticalLayout_2.setStretch(1, 1)

        self.retranslateUi(FormLocalMusicList)

        QMetaObject.connectSlotsByName(FormLocalMusicList)
    # setupUi

    def retranslateUi(self, FormLocalMusicList):
        FormLocalMusicList.setWindowTitle(QCoreApplication.translate("FormLocalMusicList", u"Form", None))
        self.leftPictureLabel.setText(QCoreApplication.translate("FormLocalMusicList", u"TextLabel", None))
        self.explainTitleLabel.setText(QCoreApplication.translate("FormLocalMusicList", u"TextLabel", None))
        self.playAllButton.setText(QCoreApplication.translate("FormLocalMusicList", u"\u64ad\u653e\u6240\u6709", None))
    # retranslateUi

