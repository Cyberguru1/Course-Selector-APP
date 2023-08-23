# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaceEQPOON.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import QSS_Resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(930, 659)
        MainWindow.setStyleSheet(u"*{\n"
"	border:  none;\n"
"	background-color:  transparent;\n"
"	background:  transparent;\n"
"	padding:  0;\n"
"	margin:  0;\n"
"	color:  rgb(255, 255, 255) ;\n"
"}\n"
"\n"
"#centralwidget, #home, #mainBodyContent{\n"
"	background-color: #1b1b27;\n"
"}\n"
"\n"
"#header, #mainBody{\n"
"	background-color:  #27263c;\n"
"}\n"
"\n"
"#pushButton{\n"
"	border: 1px solid #cc5bce;\n"
"	border-radius: 19px;\n"
"	text-align: center;\n"
"}\n"
"\n"
"QPushButton{\n"
"	text-align: left;\n"
"	padding: 5px 10px;\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"}\n"
"\n"
"#home{\n"
"	border-left: 4px solid #cc5bce;\n"
"	font-weight: bold;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header = QWidget(self.centralwidget)
        self.header.setObjectName(u"header")
        self.horizontalLayout = QHBoxLayout(self.header)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.header)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.menuBtn = QPushButton(self.frame_2)
        self.menuBtn.setObjectName(u"menuBtn")
        self.menuBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/Icons/align-justify.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menuBtn.setIcon(icon)
        self.menuBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.menuBtn, 0, Qt.AlignLeft)

        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamily(u"Nimbus Roman [UKWN]")
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.label)


        self.horizontalLayout.addWidget(self.frame_2, 0, Qt.AlignLeft)

        self.frame = QFrame(self.header)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_3 = QPushButton(self.frame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/Icons/bell.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon1)
        self.pushButton_3.setIconSize(QSize(16, 16))

        self.horizontalLayout_3.addWidget(self.pushButton_3)

        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/Icons/activity.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setIconSize(QSize(16, 16))

        self.horizontalLayout_3.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(38, 38))
        self.pushButton.setMaximumSize(QSize(38, 38))
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"#pushButton {\n"
"	border: 1px solid #cc5bce;\n"
"	border-radius: 19px;\n"
"	text-align: center;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icons/Icons/user.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon3)
        self.pushButton.setIconSize(QSize(32, 32))

        self.horizontalLayout_3.addWidget(self.pushButton)


        self.horizontalLayout.addWidget(self.frame, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.header, 0, Qt.AlignTop)

        self.mainBody = QWidget(self.centralwidget)
        self.mainBody.setObjectName(u"mainBody")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainBody.sizePolicy().hasHeightForWidth())
        self.mainBody.setSizePolicy(sizePolicy)
        self.mainBody.setMinimumSize(QSize(930, 603))
        self.horizontalLayout_4 = QHBoxLayout(self.mainBody)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.leftMenu = QWidget(self.mainBody)
        self.leftMenu.setObjectName(u"leftMenu")
        self.leftMenu.setMinimumSize(QSize(200, 0))
        self.verticalLayout_3 = QVBoxLayout(self.leftMenu)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 20)
        self.widget = QWidget(self.leftMenu)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(200, 583))
        self.verticalLayout_4 = QVBoxLayout(self.widget)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(10, 0, 0, 0)
        self.frame_3 = QFrame(self.widget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.home = QPushButton(self.frame_3)
        self.home.setObjectName(u"home")
        font1 = QFont()
        font1.setBold(True)
        font1.setWeight(75)
        self.home.setFont(font1)
        self.home.setCursor(QCursor(Qt.PointingHandCursor))
        self.home.setStyleSheet(u"	text-align: left;\n"
"	padding: 3px 5px;")
        icon4 = QIcon()
        icon4.addFile(u":/icons/Icons/home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.home.setIcon(icon4)

        self.verticalLayout_5.addWidget(self.home)

        self.select_course = QPushButton(self.frame_3)
        self.select_course.setObjectName(u"select_course")
        self.select_course.setFont(font1)
        self.select_course.setCursor(QCursor(Qt.PointingHandCursor))
        self.select_course.setStyleSheet(u"	text-align: left;\n"
"	padding: 3px 5px;")
        self.select_course.setIcon(icon2)

        self.verticalLayout_5.addWidget(self.select_course)

        self.institution = QPushButton(self.frame_3)
        self.institution.setObjectName(u"institution")
        self.institution.setFont(font1)
        self.institution.setCursor(QCursor(Qt.PointingHandCursor))
        self.institution.setStyleSheet(u"	text-align: left;\n"
"	padding: 3px 5px;")
        icon5 = QIcon()
        icon5.addFile(u":/icons/Icons/book-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.institution.setIcon(icon5)

        self.verticalLayout_5.addWidget(self.institution)

        self.history = QPushButton(self.frame_3)
        self.history.setObjectName(u"history")
        self.history.setFont(font1)
        self.history.setCursor(QCursor(Qt.PointingHandCursor))
        self.history.setStyleSheet(u"	text-align: left;\n"
"	padding: 3px 5px;")
        icon6 = QIcon()
        icon6.addFile(u":/icons/Icons/globe.png", QSize(), QIcon.Normal, QIcon.Off)
        self.history.setIcon(icon6)

        self.verticalLayout_5.addWidget(self.history)


        self.verticalLayout_4.addWidget(self.frame_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.frame_4 = QFrame(self.widget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_4)
        self.verticalLayout_6.setSpacing(10)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.settings = QPushButton(self.frame_4)
        self.settings.setObjectName(u"settings")
        self.settings.setFont(font1)
        self.settings.setCursor(QCursor(Qt.PointingHandCursor))
        self.settings.setStyleSheet(u"	text-align: left;\n"
"	padding: 3px 5px;")
        icon7 = QIcon()
        icon7.addFile(u":/icons/Icons/settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settings.setIcon(icon7)

        self.verticalLayout_6.addWidget(self.settings)

        self.help = QPushButton(self.frame_4)
        self.help.setObjectName(u"help")
        self.help.setFont(font1)
        self.help.setCursor(QCursor(Qt.PointingHandCursor))
        self.help.setStyleSheet(u"	text-align: left;\n"
"	padding: 3px 5px;")
        icon8 = QIcon()
        icon8.addFile(u":/icons/Icons/help-circle.png", QSize(), QIcon.Normal, QIcon.Off)
        self.help.setIcon(icon8)

        self.verticalLayout_6.addWidget(self.help)

        self.about = QPushButton(self.frame_4)
        self.about.setObjectName(u"about")
        self.about.setFont(font1)
        self.about.setCursor(QCursor(Qt.PointingHandCursor))
        self.about.setStyleSheet(u"	text-align: left;\n"
"	padding: 3px 5px;")
        icon9 = QIcon()
        icon9.addFile(u":/icons/Icons/info.png", QSize(), QIcon.Normal, QIcon.Off)
        self.about.setIcon(icon9)

        self.verticalLayout_6.addWidget(self.about)


        self.verticalLayout_4.addWidget(self.frame_4)


        self.verticalLayout_3.addWidget(self.widget)


        self.horizontalLayout_4.addWidget(self.leftMenu)

        self.mainBodyContent = QWidget(self.mainBody)
        self.mainBodyContent.setObjectName(u"mainBodyContent")
        self.verticalLayout_2 = QVBoxLayout(self.mainBodyContent)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.stackedWidget = QStackedWidget(self.mainBodyContent)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)

        self.verticalLayout_2.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.mainBodyContent)

        self.rightMenu = QWidget(self.mainBody)
        self.rightMenu.setObjectName(u"rightMenu")

        self.horizontalLayout_4.addWidget(self.rightMenu)


        self.verticalLayout.addWidget(self.mainBody)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.menuBtn.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Course Selector App", None))
        self.pushButton_3.setText("")
        self.pushButton_2.setText("")
        self.pushButton.setText("")
        self.home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.select_course.setText(QCoreApplication.translate("MainWindow", u"Select Course", None))
        self.institution.setText(QCoreApplication.translate("MainWindow", u"Institutions", None))
        self.history.setText(QCoreApplication.translate("MainWindow", u"History", None))
        self.settings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.help.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.about.setText(QCoreApplication.translate("MainWindow", u"About", None))
    # retranslateUi

