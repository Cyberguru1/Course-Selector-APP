# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaceATGlNI.ui'
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
from Custom_Widgets.Widgets import FormProgressIndicator

import QSS_Resources_rc
import QSS_Resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1137, 700)
        MainWindow.setCursor(QCursor(Qt.PointingHandCursor))
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
"#pushButtton, #startBtn, #prevBtn, #endBtn, #nextBtn, #submitBtn, #testBtn, #backrBtn\n"
"{\n"
"	border: 1px solid #cc5bce;\n"
"	border-radius: 19px;\n"
"	text-align: center;\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"	border-top-right-radius: 10px;\n"
"	border-bottom-right-radius: 10px;\n"
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
        icon2.addFile(u":/icons/Icons/globe.png", QSize(), QIcon.Normal, QIcon.Off)
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
        icon5 = QIcon()
        icon5.addFile(u":/icons/Icons/activity.png", QSize(), QIcon.Normal, QIcon.Off)
        self.select_courseBtn.setIcon(icon5)

        self.verticalLayout_5.addWidget(self.select_courseBtn)

        self.institutionBtn = QPushButton(self.frame_3)
        self.institutionBtn.setObjectName(u"institutionBtn")
        self.institutionBtn.setFont(font1)
        self.institutionBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.institutionBtn.setStyleSheet(u"	text-align: left;\n"
"	padding: 3px 5px;")
        icon6 = QIcon()
        icon6.addFile(u":/icons/Icons/book-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.institutionBtn.setIcon(icon6)

        self.verticalLayout_5.addWidget(self.institutionBtn)

        self.connectBtn = QPushButton(self.frame_3)
        self.connectBtn.setObjectName(u"connectBtn")
        self.connectBtn.setFont(font1)
        self.connectBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.connectBtn.setStyleSheet(u"	text-align: left;\n"
"	padding: 3px 5px;")
        self.connectBtn.setIcon(icon2)

        self.verticalLayout_5.addWidget(self.connectBtn)


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
        self.helpBtn = QPushButton(self.frame_4)
        self.helpBtn.setObjectName(u"helpBtn")
        self.helpBtn.setFont(font1)
        self.helpBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.helpBtn.setStyleSheet(u"	text-align: left;\n"
"	padding: 3px 5px;")
        icon7 = QIcon()
        icon7.addFile(u":/icons/Icons/help-circle.png", QSize(), QIcon.Normal, QIcon.Off)
        self.helpBtn.setIcon(icon7)

        self.verticalLayout_6.addWidget(self.helpBtn)

        self.aboutBtn = QPushButton(self.frame_4)
        self.aboutBtn.setObjectName(u"aboutBtn")
        self.aboutBtn.setFont(font1)
        self.aboutBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.aboutBtn.setStyleSheet(u"	text-align: left;\n"
"	padding: 3px 5px;")
        icon8 = QIcon()
        icon8.addFile(u":/icons/Icons/info.png", QSize(), QIcon.Normal, QIcon.Off)
        self.aboutBtn.setIcon(icon8)

        self.verticalLayout_6.addWidget(self.aboutBtn)


        self.verticalLayout_4.addWidget(self.frame_4)


        self.verticalLayout_3.addWidget(self.widget)


        self.horizontalLayout_4.addWidget(self.leftMenu)

        self.mainBodyContent = QWidget(self.mainBody)
        self.mainBodyContent.setObjectName(u"mainBodyContent")
        self.verticalLayout_10 = QVBoxLayout(self.mainBodyContent)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.mainPages = QCustomStackedWidget(self.mainBodyContent)
        self.mainPages.setObjectName(u"mainPages")
        self.homePage = QWidget()
        self.homePage.setObjectName(u"homePage")
        self.verticalLayout_25 = QVBoxLayout(self.homePage)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.label_4 = QLabel(self.homePage)
        self.label_4.setObjectName(u"label_4")
        font2 = QFont()
        font2.setPointSize(15)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_4.setFont(font2)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_25.addWidget(self.label_4, 0, Qt.AlignTop)

        self.widget_22 = QWidget(self.homePage)
        self.widget_22.setObjectName(u"widget_22")
        self.widget_22.setStyleSheet(u"background-color:  #0a1128;\n"
"border-top-left-radius: 50px;\n"
"border-bottom-right-radius: 60px;\n"
"")
        self.horizontalLayout_12 = QHBoxLayout(self.widget_22)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_5 = QLabel(self.widget_22)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font2)

        self.horizontalLayout_12.addWidget(self.label_5, 0, Qt.AlignHCenter)


        self.verticalLayout_25.addWidget(self.widget_22)

        self.frame_11 = QFrame(self.homePage)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setStyleSheet(u"background-color:  #0a1128;\n"
"border-top-left-radius: 50px;\n"
"border-bottom-right-radius: 60px;\n"
"")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_23 = QLabel(self.frame_11)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font2)

        self.horizontalLayout_17.addWidget(self.label_23, 0, Qt.AlignHCenter)


        self.verticalLayout_25.addWidget(self.frame_11, 0, Qt.AlignHCenter)

        self.widget_16 = QWidget(self.homePage)
        self.widget_16.setObjectName(u"widget_16")
        self.horizontalLayout_10 = QHBoxLayout(self.widget_16)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.widget_17 = QWidget(self.widget_16)
        self.widget_17.setObjectName(u"widget_17")
        self.widget_17.setFont(font2)
        self.widget_17.setStyleSheet(u"background-color:  #0a1128;\n"
"border-top-left-radius: 50px;\n"
"border-bottom-right-radius: 60px;\n"
"")
        self.horizontalLayout_13 = QHBoxLayout(self.widget_17)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_26 = QLabel(self.widget_17)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setPixmap(QPixmap(u":/icons/Icons/cpu.png"))

        self.horizontalLayout_13.addWidget(self.label_26, 0, Qt.AlignHCenter)

        self.label_16 = QLabel(self.widget_17)
        self.label_16.setObjectName(u"label_16")
        font3 = QFont()
        font3.setPointSize(11)
        font3.setBold(True)
        font3.setWeight(75)
        self.label_16.setFont(font3)

        self.horizontalLayout_13.addWidget(self.label_16, 0, Qt.AlignHCenter)


        self.horizontalLayout_10.addWidget(self.widget_17)

        self.widget_18 = QWidget(self.widget_16)
        self.widget_18.setObjectName(u"widget_18")
        self.widget_18.setStyleSheet(u"background-color:  #0a1128;\n"
"border-top-left-radius: 50px;\n"
"border-bottom-right-radius: 60px;\n"
"")
        self.horizontalLayout_16 = QHBoxLayout(self.widget_18)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_25 = QLabel(self.widget_18)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setPixmap(QPixmap(u":/icons/Icons/archive.png"))

        self.horizontalLayout_16.addWidget(self.label_25, 0, Qt.AlignHCenter)

        self.label_17 = QLabel(self.widget_18)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font3)

        self.horizontalLayout_16.addWidget(self.label_17, 0, Qt.AlignHCenter)


        self.horizontalLayout_10.addWidget(self.widget_18)


        self.verticalLayout_25.addWidget(self.widget_16)

        self.widget_15 = QWidget(self.homePage)
        self.widget_15.setObjectName(u"widget_15")
        self.horizontalLayout_9 = QHBoxLayout(self.widget_15)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.widget_19 = QWidget(self.widget_15)
        self.widget_19.setObjectName(u"widget_19")
        self.widget_19.setStyleSheet(u"background-color:  #0a1128;\n"
"border-top-left-radius: 50px;\n"
"border-bottom-right-radius: 60px;\n"
"")
        self.horizontalLayout_15 = QHBoxLayout(self.widget_19)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_27 = QLabel(self.widget_19)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setPixmap(QPixmap(u":/icons/Icons/cloud-lightning.png"))

        self.horizontalLayout_15.addWidget(self.label_27, 0, Qt.AlignHCenter)

        self.label_18 = QLabel(self.widget_19)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font3)

        self.horizontalLayout_15.addWidget(self.label_18, 0, Qt.AlignHCenter)


        self.horizontalLayout_9.addWidget(self.widget_19)

        self.widget_20 = QWidget(self.widget_15)
        self.widget_20.setObjectName(u"widget_20")
        self.widget_20.setStyleSheet(u"background-color:  #0a1128;\n"
"border-top-left-radius: 50px;\n"
"border-bottom-right-radius: 60px;\n"
"\n"
"")
        self.horizontalLayout_14 = QHBoxLayout(self.widget_20)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_24 = QLabel(self.widget_20)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setPixmap(QPixmap(u":/icons/Icons/search.png"))

        self.horizontalLayout_14.addWidget(self.label_24, 0, Qt.AlignHCenter)

        self.label_22 = QLabel(self.widget_20)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font3)

        self.horizontalLayout_14.addWidget(self.label_22)


        self.horizontalLayout_9.addWidget(self.widget_20)


        self.verticalLayout_25.addWidget(self.widget_15)

        self.mainPages.addWidget(self.homePage)
        self.selectPage = QWidget()
        self.selectPage.setObjectName(u"selectPage")
        self.verticalLayout_7 = QVBoxLayout(self.selectPage)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_3 = QLabel(self.selectPage)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font2)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_3, 0, Qt.AlignTop)

        self.queLabel = QLabel(self.selectPage)
        self.queLabel.setObjectName(u"queLabel")
        self.queLabel.setMinimumSize(QSize(800, 0))
        font4 = QFont()
        font4.setFamily(u"FreeSans")
        font4.setPointSize(27)
        font4.setBold(True)
        font4.setWeight(75)
        self.queLabel.setFont(font4)
        self.queLabel.setAlignment(Qt.AlignCenter)
        self.queLabel.setWordWrap(True)

        self.verticalLayout_7.addWidget(self.queLabel, 0, Qt.AlignHCenter)

        self.frame_5 = QFrame(self.selectPage)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.frame_5)

        self.ansInput = QLineEdit(self.selectPage)
        self.ansInput.setObjectName(u"ansInput")
        font5 = QFont()
        font5.setFamily(u"FreeSans")
        font5.setPointSize(19)
        self.ansInput.setFont(font5)
        self.ansInput.setToolTipDuration(-3)

        self.verticalLayout_7.addWidget(self.ansInput, 0, Qt.AlignHCenter)

        self.widget_2 = QWidget(self.selectPage)
        self.widget_2.setObjectName(u"widget_2")

        self.verticalLayout_7.addWidget(self.widget_2, 0, Qt.AlignHCenter)

        self.selectFrame = QFrame(self.selectPage)
        self.selectFrame.setObjectName(u"selectFrame")
        self.selectFrame.setMinimumSize(QSize(830, 0))
        self.selectFrame.setMaximumSize(QSize(16777215, 16777215))
        self.selectFrame.setCursor(QCursor(Qt.PointingHandCursor))
        self.selectFrame.setMouseTracking(True)
        self.selectFrame.setFrameShape(QFrame.StyledPanel)
        self.selectFrame.setFrameShadow(QFrame.Raised)
        self.selectFrame.setLineWidth(2)
        self.horizontalLayout_5 = QHBoxLayout(self.selectFrame)
        self.horizontalLayout_5.setSpacing(18)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 149)
        self.prevBtn = QPushButton(self.selectFrame)
        self.prevBtn.setObjectName(u"prevBtn")
        font6 = QFont()
        font6.setBold(True)
        font6.setItalic(False)
        font6.setWeight(75)
        self.prevBtn.setFont(font6)
        icon9 = QIcon()
        icon9.addFile(u":/icons/Icons/arrow_left.png", QSize(), QIcon.Normal, QIcon.Off)
        self.prevBtn.setIcon(icon9)
        self.prevBtn.setIconSize(QSize(32, 18))

        self.horizontalLayout_5.addWidget(self.prevBtn, 0, Qt.AlignHCenter)

        self.startBtn = QPushButton(self.selectFrame)
        self.startBtn.setObjectName(u"startBtn")
        self.startBtn.setFont(font1)
        icon10 = QIcon()
        icon10.addFile(u":/icons/Icons/rewind.png", QSize(), QIcon.Normal, QIcon.Off)
        self.startBtn.setIcon(icon10)
        self.startBtn.setIconSize(QSize(32, 18))

        self.horizontalLayout_5.addWidget(self.startBtn, 0, Qt.AlignHCenter)

        self.endBtn = QPushButton(self.selectFrame)
        self.endBtn.setObjectName(u"endBtn")
        self.endBtn.setFont(font6)
        icon11 = QIcon()
        icon11.addFile(u":/icons/Icons/fast-forward.png", QSize(), QIcon.Normal, QIcon.Off)
        self.endBtn.setIcon(icon11)
        self.endBtn.setIconSize(QSize(32, 18))

        self.horizontalLayout_5.addWidget(self.endBtn, 0, Qt.AlignHCenter)

        self.nextBtn = QPushButton(self.selectFrame)
        self.nextBtn.setObjectName(u"nextBtn")
        self.nextBtn.setFont(font1)
        icon12 = QIcon()
        icon12.addFile(u":/icons/Icons/arrow_right.png", QSize(), QIcon.Normal, QIcon.Off)
        self.nextBtn.setIcon(icon12)
        self.nextBtn.setIconSize(QSize(32, 18))

        self.horizontalLayout_5.addWidget(self.nextBtn, 0, Qt.AlignHCenter)

        self.submitBtn = QPushButton(self.selectFrame)
        self.submitBtn.setObjectName(u"submitBtn")

        self.horizontalLayout_5.addWidget(self.submitBtn)


        self.verticalLayout_7.addWidget(self.selectFrame, 0, Qt.AlignHCenter)

        self.selectProg = FormProgressIndicator(self.selectPage)
        self.selectProg.setObjectName(u"selectProg")
        self.selectProg.setMaximumSize(QSize(300, 16777215))

        self.verticalLayout_7.addWidget(self.selectProg, 0, Qt.AlignHCenter)

        self.frame_7 = QFrame(self.selectPage)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.frame_7)

        self.mainPages.addWidget(self.selectPage)
        self.institutionsPage = QWidget()
        self.institutionsPage.setObjectName(u"institutionsPage")
        self.verticalLayout_11 = QVBoxLayout(self.institutionsPage)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_2 = QLabel(self.institutionsPage)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font2)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_2, 0, Qt.AlignTop)

        self.widget_10 = QWidget(self.institutionsPage)
        self.widget_10.setObjectName(u"widget_10")

        self.verticalLayout_11.addWidget(self.widget_10)

        self.instSearch = QLineEdit(self.institutionsPage)
        self.instSearch.setObjectName(u"instSearch")
        font7 = QFont()
        font7.setPointSize(16)
        font7.setBold(True)
        font7.setWeight(75)
        self.instSearch.setFont(font7)
        self.instSearch.setAlignment(Qt.AlignCenter)
        self.instSearch.setDragEnabled(True)

        self.verticalLayout_11.addWidget(self.instSearch)

        self.frame_17 = QFrame(self.institutionsPage)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)

        self.verticalLayout_11.addWidget(self.frame_17)

        self.frame_9 = QFrame(self.institutionsPage)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)

        self.verticalLayout_11.addWidget(self.frame_9, 0, Qt.AlignVCenter)

        self.tableView = QTableView(self.institutionsPage)
        self.tableView.setObjectName(u"tableView")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tableView.sizePolicy().hasHeightForWidth())
        self.tableView.setSizePolicy(sizePolicy1)
        self.tableView.setMinimumSize(QSize(0, 600))
        self.tableView.viewport().setProperty("cursor", QCursor(Qt.PointingHandCursor))
        self.tableView.setMouseTracking(True)
        self.tableView.setStyleSheet(u"background-color: rgb(53, 56, 63);")
        self.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableView.setDefaultDropAction(Qt.CopyAction)
        self.tableView.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.tableView.setTextElideMode(Qt.ElideNone)
        self.tableView.setSortingEnabled(True)
        self.tableView.verticalHeader().setProperty("showSortIndicator", True)

        self.verticalLayout_11.addWidget(self.tableView)

        self.mainPages.addWidget(self.institutionsPage)
        self.historyPage = QWidget()
        self.historyPage.setObjectName(u"historyPage")
        self.verticalLayout_18 = QVBoxLayout(self.historyPage)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.mainPages.addWidget(self.historyPage)
        self.resultPage = QWidget()
        self.resultPage.setObjectName(u"resultPage")
        self.verticalLayout_19 = QVBoxLayout(self.resultPage)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_13 = QLabel(self.resultPage)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font2)
        self.label_13.setAlignment(Qt.AlignCenter)

        self.verticalLayout_19.addWidget(self.label_13, 0, Qt.AlignTop)

        self.frame_16 = QFrame(self.resultPage)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)

        self.verticalLayout_19.addWidget(self.frame_16)

        self.label_14 = QLabel(self.resultPage)
        self.label_14.setObjectName(u"label_14")
        font8 = QFont()
        font8.setPointSize(13)
        font8.setBold(True)
        font8.setWeight(75)
        self.label_14.setFont(font8)

        self.verticalLayout_19.addWidget(self.label_14)

        self.frame_14 = QFrame(self.resultPage)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)

        self.verticalLayout_19.addWidget(self.frame_14)

        self.widget_12 = QWidget(self.resultPage)
        self.widget_12.setObjectName(u"widget_12")
        self.verticalLayout_24 = QVBoxLayout(self.widget_12)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.frame_15 = QFrame(self.widget_12)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)

        self.verticalLayout_24.addWidget(self.frame_15)

        self.course5Label = QLabel(self.widget_12)
        self.course5Label.setObjectName(u"course5Label")
        self.course5Label.setFont(font8)
        self.course5Label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_24.addWidget(self.course5Label, 0, Qt.AlignTop)

        self.resultEntry = QTextBrowser(self.widget_12)
        self.resultEntry.setObjectName(u"resultEntry")

        self.verticalLayout_24.addWidget(self.resultEntry)


        self.verticalLayout_19.addWidget(self.widget_12)

        self.frame_10 = QFrame(self.resultPage)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.backrBtn = QPushButton(self.frame_10)
        self.backrBtn.setObjectName(u"backrBtn")
        self.backrBtn.setFont(font8)
        icon13 = QIcon()
        icon13.addFile(u":/icons/Icons/arrow-left.png", QSize(), QIcon.Normal, QIcon.Off)
        self.backrBtn.setIcon(icon13)
        self.backrBtn.setIconSize(QSize(32, 18))

        self.horizontalLayout_6.addWidget(self.backrBtn, 0, Qt.AlignHCenter)


        self.verticalLayout_19.addWidget(self.frame_10)

        self.frame_8 = QFrame(self.resultPage)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)

        self.verticalLayout_19.addWidget(self.frame_8)

        self.mainPages.addWidget(self.resultPage)
        self.helpPage = QWidget()
        self.helpPage.setObjectName(u"helpPage")
        self.verticalLayout_26 = QVBoxLayout(self.helpPage)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.label_7 = QLabel(self.helpPage)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font2)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_26.addWidget(self.label_7, 0, Qt.AlignTop)

        self.widget_23 = QWidget(self.helpPage)
        self.widget_23.setObjectName(u"widget_23")
        self.horizontalLayout_18 = QHBoxLayout(self.widget_23)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_28 = QLabel(self.widget_23)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setWordWrap(True)

        self.horizontalLayout_18.addWidget(self.label_28)


        self.verticalLayout_26.addWidget(self.widget_23)

        self.frame_13 = QFrame(self.helpPage)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)

        self.verticalLayout_26.addWidget(self.frame_13)

        self.frame_12 = QFrame(self.helpPage)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)

        self.verticalLayout_26.addWidget(self.frame_12)

        self.mainPages.addWidget(self.helpPage)
        self.aboutPage = QWidget()
        self.aboutPage.setObjectName(u"aboutPage")
        self.verticalLayout_16 = QVBoxLayout(self.aboutPage)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_8 = QLabel(self.aboutPage)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font2)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.label_8, 0, Qt.AlignTop)

        self.widget_8 = QWidget(self.aboutPage)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setMaximumSize(QSize(300, 300))
        self.widget_8.setFont(font1)
        self.widget_8.setStyleSheet(u"background-color:  #0a1128;\n"
"border-top-left-radius: 50px;\n"
"border-bottom-right-radius: 60px;\n"
"")
        self.verticalLayout_17 = QVBoxLayout(self.widget_8)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_19 = QLabel(self.widget_8)
        self.label_19.setObjectName(u"label_19")

        self.verticalLayout_17.addWidget(self.label_19, 0, Qt.AlignHCenter)

        self.label_20 = QLabel(self.widget_8)
        self.label_20.setObjectName(u"label_20")

        self.verticalLayout_17.addWidget(self.label_20, 0, Qt.AlignHCenter)

        self.label_21 = QLabel(self.widget_8)
        self.label_21.setObjectName(u"label_21")

        self.verticalLayout_17.addWidget(self.label_21, 0, Qt.AlignHCenter)


        self.verticalLayout_16.addWidget(self.widget_8, 0, Qt.AlignHCenter)

        self.widget_9 = QWidget(self.aboutPage)
        self.widget_9.setObjectName(u"widget_9")

        self.verticalLayout_16.addWidget(self.widget_9)

        self.mainPages.addWidget(self.aboutPage)
        self.notificationsPage = QWidget()
        self.notificationsPage.setObjectName(u"notificationsPage")
        self.verticalLayout_8 = QVBoxLayout(self.notificationsPage)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_6 = QLabel(self.notificationsPage)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font2)
        self.label_6.setMouseTracking(True)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_6, 0, Qt.AlignTop)

        self.label_9 = QLabel(self.notificationsPage)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font8)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_9, 0, Qt.AlignHCenter)

        self.mainPages.addWidget(self.notificationsPage)
        self.connPage = QWidget()
        self.connPage.setObjectName(u"connPage")
        self.verticalLayout_2 = QVBoxLayout(self.connPage)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_10 = QLabel(self.connPage)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font2)
        self.label_10.setLayoutDirection(Qt.LeftToRight)
        self.label_10.setTextFormat(Qt.AutoText)
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_10, 0, Qt.AlignTop)

        self.widget_3 = QWidget(self.connPage)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.pushButton_2 = QPushButton(self.widget_3)
        self.pushButton_2.setObjectName(u"pushButton_2")
        font9 = QFont()
        font9.setPointSize(20)
        font9.setBold(True)
        font9.setWeight(75)
        self.pushButton_2.setFont(font9)
        icon14 = QIcon()
        icon14.addFile(u":/icons/Icons/arrow-up.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon14)
        self.pushButton_2.setIconSize(QSize(40, 125))

        self.horizontalLayout_7.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.widget_3)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setFont(font9)
        icon15 = QIcon()
        icon15.addFile(u":/icons/Icons/arrow-down.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon15)
        self.pushButton.setIconSize(QSize(40, 125))

        self.horizontalLayout_7.addWidget(self.pushButton)


        self.verticalLayout_2.addWidget(self.widget_3, 0, Qt.AlignHCenter)

        self.widget_4 = QWidget(self.connPage)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_8 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.upLabel = QLabel(self.widget_4)
        self.upLabel.setObjectName(u"upLabel")
        self.upLabel.setFont(font2)

        self.horizontalLayout_8.addWidget(self.upLabel, 0, Qt.AlignLeft)

        self.label_12 = QLabel(self.widget_4)
        self.label_12.setObjectName(u"label_12")
        font10 = QFont()
        font10.setPointSize(14)
        font10.setBold(True)
        font10.setWeight(75)
        self.label_12.setFont(font10)

        self.horizontalLayout_8.addWidget(self.label_12)

        self.label_11 = QLabel(self.widget_4)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_8.addWidget(self.label_11)

        self.downLabel = QLabel(self.widget_4)
        self.downLabel.setObjectName(u"downLabel")
        self.downLabel.setFont(font2)

        self.horizontalLayout_8.addWidget(self.downLabel, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.widget_4, 0, Qt.AlignHCenter)

        self.frame_6 = QFrame(self.connPage)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_6)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.testBtn = QPushButton(self.frame_6)
        self.testBtn.setObjectName(u"testBtn")
        self.testBtn.setFont(font2)
        icon16 = QIcon()
        icon16.addFile(u":/icons/Icons/wifi.png", QSize(), QIcon.Normal, QIcon.Off)
        self.testBtn.setIcon(icon16)
        self.testBtn.setIconSize(QSize(32, 18))

        self.verticalLayout_9.addWidget(self.testBtn, 0, Qt.AlignHCenter)


        self.verticalLayout_2.addWidget(self.frame_6)

        self.connRes = QLabel(self.connPage)
        self.connRes.setObjectName(u"connRes")
        self.connRes.setFont(font10)

        self.verticalLayout_2.addWidget(self.connRes, 0, Qt.AlignHCenter)

        self.mainPages.addWidget(self.connPage)

        self.verticalLayout_10.addWidget(self.mainPages)

        self.widget_21 = QWidget(self.mainBodyContent)
        self.widget_21.setObjectName(u"widget_21")
        self.horizontalLayout_11 = QHBoxLayout(self.widget_21)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_15 = QLabel(self.widget_21)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_11.addWidget(self.label_15, 0, Qt.AlignHCenter)


        self.verticalLayout_10.addWidget(self.widget_21)


        self.horizontalLayout_4.addWidget(self.mainBodyContent)

        self.rightMenu = QCustomSlideMenu(self.mainBody)
        self.rightMenu.setObjectName(u"rightMenu")
        self.rightMenu.setMinimumSize(QSize(0, 0))
        self.verticalLayout_12 = QVBoxLayout(self.rightMenu)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.uniName = QLabel(self.rightMenu)
        self.uniName.setObjectName(u"uniName")
        self.uniName.setFont(font2)
        self.uniName.setAlignment(Qt.AlignCenter)
        self.uniName.setWordWrap(True)

        self.verticalLayout_12.addWidget(self.uniName, 0, Qt.AlignTop)

        self.widget_7 = QWidget(self.rightMenu)
        self.widget_7.setObjectName(u"widget_7")
        self.verticalLayout_13 = QVBoxLayout(self.widget_7)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.utmeLabel = QLabel(self.widget_7)
        self.utmeLabel.setObjectName(u"utmeLabel")
        font11 = QFont()
        font11.setPointSize(12)
        font11.setBold(True)
        font11.setWeight(75)
        self.utmeLabel.setFont(font11)
        self.utmeLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.utmeLabel, 0, Qt.AlignTop)

        self.utmeEntry = QTextBrowser(self.widget_7)
        self.utmeEntry.setObjectName(u"utmeEntry")

        self.verticalLayout_13.addWidget(self.utmeEntry, 0, Qt.AlignTop)


        self.verticalLayout_12.addWidget(self.widget_7)

        self.widget_6 = QWidget(self.rightMenu)
        self.widget_6.setObjectName(u"widget_6")
        self.verticalLayout_14 = QVBoxLayout(self.widget_6)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.deLabel = QLabel(self.widget_6)
        self.deLabel.setObjectName(u"deLabel")
        self.deLabel.setFont(font11)
        self.deLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.deLabel, 0, Qt.AlignTop)

        self.deEntry = QTextBrowser(self.widget_6)
        self.deEntry.setObjectName(u"deEntry")

        self.verticalLayout_14.addWidget(self.deEntry)


        self.verticalLayout_12.addWidget(self.widget_6)

        self.widget_5 = QWidget(self.rightMenu)
        self.widget_5.setObjectName(u"widget_5")
        self.verticalLayout_15 = QVBoxLayout(self.widget_5)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.jambLabel = QLabel(self.widget_5)
        self.jambLabel.setObjectName(u"jambLabel")
        self.jambLabel.setFont(font11)
        self.jambLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.jambLabel, 0, Qt.AlignTop)

        self.jambEntry = QTextBrowser(self.widget_5)
        self.jambEntry.setObjectName(u"jambEntry")

        self.verticalLayout_15.addWidget(self.jambEntry)


        self.verticalLayout_12.addWidget(self.widget_5)


        self.horizontalLayout_4.addWidget(self.rightMenu)


        self.verticalLayout.addWidget(self.mainBody)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.mainPages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.menuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Show Menu", None))
#endif // QT_CONFIG(tooltip)
        self.menuBtn.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Course Selector App", None))
#if QT_CONFIG(tooltip)
        self.notificationsBtn.setToolTip(QCoreApplication.translate("MainWindow", u"View Notifications", None))
#endif // QT_CONFIG(tooltip)
        self.notificationsBtn.setText("")
#if QT_CONFIG(tooltip)
        self.connBtn.setToolTip(QCoreApplication.translate("MainWindow", u"View Connection Speed", None))
#endif // QT_CONFIG(tooltip)
        self.connBtn.setText("")
#if QT_CONFIG(tooltip)
        self.acctBtn.setToolTip(QCoreApplication.translate("MainWindow", u"User Profile", None))
#endif // QT_CONFIG(tooltip)
        self.acctBtn.setText("")
#if QT_CONFIG(tooltip)
        self.homeBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Home Page", None))
#endif // QT_CONFIG(tooltip)
        self.homeBtn.setText(QCoreApplication.translate("MainWindow", u"Home", None))
#if QT_CONFIG(tooltip)
        self.select_courseBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Select Course Page", None))
#endif // QT_CONFIG(tooltip)
        self.select_courseBtn.setText(QCoreApplication.translate("MainWindow", u"Select Course", None))
#if QT_CONFIG(tooltip)
        self.institutionBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Search for institutions and courses", None))
#endif // QT_CONFIG(tooltip)
        self.institutionBtn.setText(QCoreApplication.translate("MainWindow", u"Institutions", None))
#if QT_CONFIG(tooltip)
        self.connectBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Check internet connection", None))
#endif // QT_CONFIG(tooltip)
        self.connectBtn.setText(QCoreApplication.translate("MainWindow", u"Connection", None))
#if QT_CONFIG(tooltip)
        self.helpBtn.setToolTip(QCoreApplication.translate("MainWindow", u"View Help", None))
#endif // QT_CONFIG(tooltip)
        self.helpBtn.setText(QCoreApplication.translate("MainWindow", u"Help", None))
#if QT_CONFIG(tooltip)
        self.aboutBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Show About", None))
#endif // QT_CONFIG(tooltip)
        self.aboutBtn.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Home screen Page", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"AI-Enabled Course Selector APP", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Features", None))
        self.label_26.setText("")
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Chat-Gpt As AI Back-End", None))
        self.label_25.setText("")
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Over 1014 Institution Database ", None))
        self.label_27.setText("")
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Supports Online And Offline Mode", None))
        self.label_24.setText("")
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Easy Search Feature", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Select Course Page", None))
#if QT_CONFIG(tooltip)
        self.queLabel.setToolTip(QCoreApplication.translate("MainWindow", u"Question", None))
#endif // QT_CONFIG(tooltip)
        self.queLabel.setText(QCoreApplication.translate("MainWindow", u"Would you like to detonate Mars !?", None))
#if QT_CONFIG(tooltip)
        self.ansInput.setToolTip(QCoreApplication.translate("MainWindow", u"Enter you answer", None))
#endif // QT_CONFIG(tooltip)
        self.ansInput.setText("")
        self.ansInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Answer.....", None))
#if QT_CONFIG(tooltip)
        self.prevBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Go to prev question", None))
#endif // QT_CONFIG(tooltip)
        self.prevBtn.setText(QCoreApplication.translate("MainWindow", u"Prev", None))
#if QT_CONFIG(tooltip)
        self.startBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Go to the beginning", None))
#endif // QT_CONFIG(tooltip)
        self.startBtn.setText(QCoreApplication.translate("MainWindow", u"Start", None))
#if QT_CONFIG(tooltip)
        self.endBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Go to last question", None))
#endif // QT_CONFIG(tooltip)
        self.endBtn.setText(QCoreApplication.translate("MainWindow", u"End", None))
#if QT_CONFIG(tooltip)
        self.nextBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Go to next question", None))
#endif // QT_CONFIG(tooltip)
        self.nextBtn.setText(QCoreApplication.translate("MainWindow", u"Next", None))
#if QT_CONFIG(tooltip)
        self.submitBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Submit to get result", None))
#endif // QT_CONFIG(tooltip)
        self.submitBtn.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
#if QT_CONFIG(tooltip)
        self.selectProg.setToolTip(QCoreApplication.translate("MainWindow", u"Current Progress", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Institution Page", None))
#if QT_CONFIG(tooltip)
        self.instSearch.setToolTip(QCoreApplication.translate("MainWindow", u"search for course or institution", None))
#endif // QT_CONFIG(tooltip)
        self.instSearch.setInputMask("")
        self.instSearch.setText("")
        self.instSearch.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search....", None))
#if QT_CONFIG(tooltip)
        self.tableView.setToolTip(QCoreApplication.translate("MainWindow", u"Institutions and courses, click on any cell to see requirements", None))
#endif // QT_CONFIG(tooltip)
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Result Page", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"This are the recommended courses by Chat-gpt :", None))
        self.course5Label.setText(QCoreApplication.translate("MainWindow", u"COURSES", None))
        self.backrBtn.setText(QCoreApplication.translate("MainWindow", u"BACK", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Help Page", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Welcome to the Help Page of our app! Here, we will provide detailed information on how to navigate and use the different features of our application.\n"
"\n"
"HOME PAGE:\n"
"The Home Page serves as an introduction to the app's features and functionalities. You can explore the various options and features available by clicking on the corresponding icons or buttons.\n"
"\n"
"SELECT COURSE PAGE:\n"
"\n"
"    On the Select Course Page, you will find a series of questions related to course selection.\n"
"    Click the \"Next\" button to move to the next question. You can answer each question one by one.\n"
"    To go back to a previous question, click the \"Prev\" button.\n"
"    If you want to jump to the first question, use the \"Begin\" button.\n"
"    If you're at the last question, click the \"End\" button.\n"
"    After answering all the questions, a \"Submit\" button will appear. Click it to submit your answers.\n"
"    Your answers will be sent to ChatGPT for processing, and you'll receive a response.\n"
"\n"
""
                        "INSTITUTIONS:\n"
"In the Institutions section, you will find a list of educational institutions. When you click on an institution, a side menu will appear, displaying requirements for both UTME (Unified Tertiary Matriculation Examination) and DE (Direct Entry) students. It also provides information on JAMB combinations for courses.\n"
"\n"
"CONNECTION:\n"
"The Connection feature helps you test your internet connection. It ensures that your device is properly connected to the internet.\n"
"\n"
"HELP:\n"
"You are currently on the Help Page, where you can find detailed instructions on how to use our app effectively.\n"
"\n"
"ABOUT:\n"
"The About Page provides information about our application, including its purpose, development team, and any additional details about the app's functionality and mission.\n"
"\n"
"We hope this Help Page assists you in navigating and utilizing our app's features. If you have any further questions or need assistance, please feel free to contact our support team for help. Enjoy using o"
                        "ur app!", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"About Page", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"COURSE SELECTOR APP v1.0", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"GROUP 10 PROJECT", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"COPYRIGHT 2023", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Notification Page", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"No New Notification !", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Connection Page", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"UP ", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"DOWN", None))
#if QT_CONFIG(tooltip)
        self.upLabel.setToolTip(QCoreApplication.translate("MainWindow", u"Show Up speed", None))
#endif // QT_CONFIG(tooltip)
        self.upLabel.setText(QCoreApplication.translate("MainWindow", u"   Mbps", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"  --------", None))
        self.label_11.setText("")
#if QT_CONFIG(tooltip)
        self.downLabel.setToolTip(QCoreApplication.translate("MainWindow", u"Shows Down speed", None))
#endif // QT_CONFIG(tooltip)
        self.downLabel.setText(QCoreApplication.translate("MainWindow", u"  Mbps", None))
#if QT_CONFIG(tooltip)
        self.testBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Click to check connection", None))
#endif // QT_CONFIG(tooltip)
        self.testBtn.setText(QCoreApplication.translate("MainWindow", u"Test", None))
        self.connRes.setText(QCoreApplication.translate("MainWindow", u"Connection Test Result", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Copyright \u00a9 2023", None))
#if QT_CONFIG(tooltip)
        self.uniName.setToolTip(QCoreApplication.translate("MainWindow", u"University name", None))
#endif // QT_CONFIG(tooltip)
        self.uniName.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
#if QT_CONFIG(tooltip)
        self.utmeLabel.setToolTip(QCoreApplication.translate("MainWindow", u"utme candidate requirments", None))
#endif // QT_CONFIG(tooltip)
        self.utmeLabel.setText(QCoreApplication.translate("MainWindow", u"UTME REQUIREMENTS", None))
#if QT_CONFIG(tooltip)
        self.deLabel.setToolTip(QCoreApplication.translate("MainWindow", u"Direct entry candidate requirements", None))
#endif // QT_CONFIG(tooltip)
        self.deLabel.setText(QCoreApplication.translate("MainWindow", u"DE REQUIREMENTS", None))
#if QT_CONFIG(tooltip)
        self.jambLabel.setToolTip(QCoreApplication.translate("MainWindow", u"subjects to register in jamb", None))
#endif // QT_CONFIG(tooltip)
        self.jambLabel.setText(QCoreApplication.translate("MainWindow", u"JAMB SUBJECTS", None))
    # retranslateUi

