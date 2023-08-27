# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfacePNSCYa.ui'
##
## Created by: Qt User Interface Compiler version 5.15.10
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore

from Custom_Widgets.Widgets import QCustomStackedWidget
from Custom_Widgets.Widgets import QCustomSlideMenu

import QSS_Resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1076, 659)
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
        self.notificationsBtn = QPushButton(self.frame)
        self.notificationsBtn.setObjectName(u"notificationsBtn")
        self.notificationsBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/Icons/bell.png", QSize(), QIcon.Normal, QIcon.Off)
        self.notificationsBtn.setIcon(icon1)
        self.notificationsBtn.setIconSize(QSize(16, 16))

        self.horizontalLayout_3.addWidget(self.notificationsBtn)

        self.connBtn = QPushButton(self.frame)
        self.connBtn.setObjectName(u"connBtn")
        self.connBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/Icons/activity.png", QSize(), QIcon.Normal, QIcon.Off)
        self.connBtn.setIcon(icon2)
        self.connBtn.setIconSize(QSize(16, 16))

        self.horizontalLayout_3.addWidget(self.connBtn)

        self.acctBtn = QPushButton(self.frame)
        self.acctBtn.setObjectName(u"acctBtn")
        self.acctBtn.setMinimumSize(QSize(38, 38))
        self.acctBtn.setMaximumSize(QSize(38, 38))
        self.acctBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.acctBtn.setStyleSheet(u"#acctBtn{\n"
"	border: 1px solid #cc5bce;\n"
"	border-radius: 19px;\n"
"	text-align: center;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icons/Icons/user.png", QSize(), QIcon.Normal, QIcon.Off)
        self.acctBtn.setIcon(icon3)
        self.acctBtn.setIconSize(QSize(32, 32))

        self.horizontalLayout_3.addWidget(self.acctBtn)


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
        self.leftMenu = QCustomSlideMenu(self.mainBody)
        self.leftMenu.setObjectName(u"leftMenu")
        self.leftMenu.setMinimumSize(QSize(200, 0))
        self.verticalLayout_3 = QVBoxLayout(self.leftMenu)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 20)
        self.widget = QCustomSlideMenu(self.leftMenu)
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
        self.homeBtn = QPushButton(self.frame_3)
        self.homeBtn.setObjectName(u"homeBtn")
        font1 = QFont()
        font1.setBold(True)
        font1.setWeight(75)
        self.homeBtn.setFont(font1)
        self.homeBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.homeBtn.setStyleSheet(u"	text-align: left;\n"
"	padding: 3px 5px;")
        icon4 = QIcon()
        icon4.addFile(u":/icons/Icons/home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.homeBtn.setIcon(icon4)

        self.verticalLayout_5.addWidget(self.homeBtn)

        self.select_courseBtn = QPushButton(self.frame_3)
        self.select_courseBtn.setObjectName(u"select_courseBtn")
        self.select_courseBtn.setFont(font1)
        self.select_courseBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.select_courseBtn.setStyleSheet(u"	text-align: left;\n"
"	padding: 3px 5px;")
        self.select_courseBtn.setIcon(icon2)

        self.verticalLayout_5.addWidget(self.select_courseBtn)

        self.institutionBtn = QPushButton(self.frame_3)
        self.institutionBtn.setObjectName(u"institutionBtn")
        self.institutionBtn.setFont(font1)
        self.institutionBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.institutionBtn.setStyleSheet(u"	text-align: left;\n"
"	padding: 3px 5px;")
        icon5 = QIcon()
        icon5.addFile(u":/icons/Icons/book-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.institutionBtn.setIcon(icon5)

        self.verticalLayout_5.addWidget(self.institutionBtn)

        self.historyBtn = QPushButton(self.frame_3)
        self.historyBtn.setObjectName(u"historyBtn")
        self.historyBtn.setFont(font1)
        self.historyBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.historyBtn.setStyleSheet(u"	text-align: left;\n"
"	padding: 3px 5px;")
        icon6 = QIcon()
        icon6.addFile(u":/icons/Icons/globe.png", QSize(), QIcon.Normal, QIcon.Off)
        self.historyBtn.setIcon(icon6)

        self.verticalLayout_5.addWidget(self.historyBtn)


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
        self.settingsBtn = QPushButton(self.frame_4)
        self.settingsBtn.setObjectName(u"settingsBtn")
        self.settingsBtn.setFont(font1)
        self.settingsBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.settingsBtn.setStyleSheet(u"	text-align: left;\n"
"	padding: 3px 5px;")
        icon7 = QIcon()
        icon7.addFile(u":/icons/Icons/settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsBtn.setIcon(icon7)

        self.verticalLayout_6.addWidget(self.settingsBtn)

        self.helpBtn = QPushButton(self.frame_4)
        self.helpBtn.setObjectName(u"helpBtn")
        self.helpBtn.setFont(font1)
        self.helpBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.helpBtn.setStyleSheet(u"	text-align: left;\n"
"	padding: 3px 5px;")
        icon8 = QIcon()
        icon8.addFile(u":/icons/Icons/help-circle.png", QSize(), QIcon.Normal, QIcon.Off)
        self.helpBtn.setIcon(icon8)

        self.verticalLayout_6.addWidget(self.helpBtn)

        self.aboutBtn = QPushButton(self.frame_4)
        self.aboutBtn.setObjectName(u"aboutBtn")
        self.aboutBtn.setFont(font1)
        self.aboutBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.aboutBtn.setStyleSheet(u"	text-align: left;\n"
"	padding: 3px 5px;")
        icon9 = QIcon()
        icon9.addFile(u":/icons/Icons/info.png", QSize(), QIcon.Normal, QIcon.Off)
        self.aboutBtn.setIcon(icon9)

        self.verticalLayout_6.addWidget(self.aboutBtn)


        self.verticalLayout_4.addWidget(self.frame_4)


        self.verticalLayout_3.addWidget(self.widget)


        self.horizontalLayout_4.addWidget(self.leftMenu)

        self.mainBodyContent = QWidget(self.mainBody)
        self.mainBodyContent.setObjectName(u"mainBodyContent")
        self.verticalLayout_2 = QVBoxLayout(self.mainBodyContent)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.mainPages = QCustomStackedWidget(self.mainBodyContent)
        self.mainPages.setObjectName(u"mainPages")
        self.homePage = QWidget()
        self.homePage.setObjectName(u"homePage")
        self.label_4 = QLabel(self.homePage)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(225, 90, 166, 91))
        font2 = QFont()
        font2.setPointSize(15)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_4.setFont(font2)
        self.lineEdit = QLineEdit(self.homePage)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(150, 240, 391, 30))
        self.mainPages.addWidget(self.homePage)
        self.selectPage = QWidget()
        self.selectPage.setObjectName(u"selectPage")
        self.label_3 = QLabel(self.selectPage)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(180, 195, 166, 91))
        self.label_3.setFont(font2)
        self.mainPages.addWidget(self.selectPage)
        self.institutionsPage = QWidget()
        self.institutionsPage.setObjectName(u"institutionsPage")
        self.label_2 = QLabel(self.institutionsPage)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(195, 180, 166, 91))
        self.label_2.setFont(font2)
        self.mainPages.addWidget(self.institutionsPage)
        self.historyPage = QWidget()
        self.historyPage.setObjectName(u"historyPage")
        self.label_5 = QLabel(self.historyPage)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(330, 270, 166, 91))
        self.label_5.setFont(font2)
        self.mainPages.addWidget(self.historyPage)
        self.settingsPage = QWidget()
        self.settingsPage.setObjectName(u"settingsPage")
        self.label_6 = QLabel(self.settingsPage)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(330, 255, 166, 91))
        self.label_6.setFont(font2)
        self.mainPages.addWidget(self.settingsPage)
        self.helpPage = QWidget()
        self.helpPage.setObjectName(u"helpPage")
        self.label_7 = QLabel(self.helpPage)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(240, 210, 166, 91))
        self.label_7.setFont(font2)
        self.mainPages.addWidget(self.helpPage)
        self.aboutPage = QWidget()
        self.aboutPage.setObjectName(u"aboutPage")
        self.label_8 = QLabel(self.aboutPage)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(270, 195, 166, 91))
        self.label_8.setFont(font2)
        self.mainPages.addWidget(self.aboutPage)
        self.notificationsPage = QWidget()
        self.notificationsPage.setObjectName(u"notificationsPage")
        self.label_9 = QLabel(self.notificationsPage)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(255, 195, 166, 91))
        self.label_9.setFont(font2)
        self.mainPages.addWidget(self.notificationsPage)
        self.connPage = QWidget()
        self.connPage.setObjectName(u"connPage")
        self.label_10 = QLabel(self.connPage)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(225, 180, 166, 91))
        self.label_10.setFont(font2)
        self.mainPages.addWidget(self.connPage)

        self.verticalLayout_2.addWidget(self.mainPages)


        self.horizontalLayout_4.addWidget(self.mainBodyContent)

        self.rightMenu = QWidget(self.mainBody)
        self.rightMenu.setObjectName(u"rightMenu")

        self.horizontalLayout_4.addWidget(self.rightMenu)


        self.verticalLayout.addWidget(self.mainBody)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.mainPages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.menuBtn.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Course Selector App", None))
        self.notificationsBtn.setText("")
        self.connBtn.setText("")
        self.acctBtn.setText("")
        self.homeBtn.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.select_courseBtn.setText(QCoreApplication.translate("MainWindow", u"Select Course", None))
        self.institutionBtn.setText(QCoreApplication.translate("MainWindow", u"Institutions", None))
        self.historyBtn.setText(QCoreApplication.translate("MainWindow", u"History", None))
        self.settingsBtn.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.helpBtn.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.aboutBtn.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Home screen Page", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"User input", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Select Course Page", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Institution Page", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Home Page", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"settings Page", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Help Page", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"About Page", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Notification Page", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Connection Page", None))
    # retranslateUi

