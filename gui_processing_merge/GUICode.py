# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GUI.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_IO(object):
    def setupUi(self, IO):
        if not IO.objectName():
            IO.setObjectName(u"IO")
        IO.resize(800, 600)
        self.centralwidget = QWidget(IO)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(145, 145, 145);")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(145, 145, 145);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(self.frame)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMinimumSize(QSize(762, 0))
        self.tabWidget.setStyleSheet(u"QTabWidget::pane {\n"
"    border: 3px solid black;\n"
"    background: white;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    padding: 2px;\n"
"    width: 200%;\n"
"    \n"
"    border: 2px solid black;\n"
"    border-bottom-color: rgb(44, 53, 72);\n"
"    border-top-left-radius: 5px;\n"
"    border-top-right-radius: 5px;\n"
"    \n"
"    background-color: rgb(35, 40, 49);        \n"
"    color: white;\n"
"}\n"
"\n"
"QTabBar::tab:selected, QTabBar::tab:hover {    \n"
"    background-color: black;\n"
"    border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"    margin-top: 3px;\n"
"}")
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Triangular)
        self.tabWidget.setIconSize(QSize(16, 16))
        self.tabWidget.setElideMode(Qt.ElideMiddle)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_2 = QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_2 = QFrame(self.tab)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"")

        self.horizontalLayout_4.addWidget(self.label_2)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.tab)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
#         self.label_3 = QLabel(self.frame_5)
#         self.label_3.setObjectName(u"label_3")
#         self.label_3.setStyleSheet(u"QLabel{\n"
# "	border: 3px solid rgb(0, 0, 0);\n"
# "	color: black;\n"
# "	padding: 5px;\n"
# "}")

        # self.horizontalLayout_5.addWidget(self.label_3)


        self.verticalLayout_4.addWidget(self.frame_5)

        self.frame_7 = QFrame(self.frame_3)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.videoPath = QLineEdit(self.frame_7)
        self.videoPath.setObjectName(u"videoPath")
        self.videoPath.setStyleSheet(u"QLineEdit{\n"
"	border: 3px solid rgb(0, 0, 0);\n"
"	color: black;\n"
"	padding: 3px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border: 5px solid rgb(0, 0, 0);\n"
"	color: rgb(57, 57, 57);\n"
"	padding: 3px;\n"
"	\n"
"}")
        self.videoPath.setCursorPosition(10)

        self.horizontalLayout_2.addWidget(self.videoPath)

        self.btnChooseVideo = QPushButton(self.frame_7)
        self.btnChooseVideo.setObjectName(u"btnChooseVideo")
        self.btnChooseVideo.setMinimumSize(QSize(100, 10))
        self.btnChooseVideo.setStyleSheet(u"QPushButton{\n"
"	border: 3px solid rgb(0, 0, 0);\n"
"	color: black;\n"
"	padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border: 5px solid rgb(0, 0, 0);\n"
"	color: rgb(57, 57, 57);\n"
"	padding: 5px;\n"
"	\n"
"}")

        self.horizontalLayout_2.addWidget(self.btnChooseVideo)

        # self.btnPlayVideo = QPushButton(self.fr)
        self.verticalLayout_4.addWidget(self.frame_7)


        self.verticalLayout_2.addWidget(self.frame_3)


        self.frame_6 = QFrame(self.tab)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(16777215, 50))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.BtnStartprocess = QPushButton(self.frame_6)
        self.BtnStartprocess.setObjectName(u"BtnStartprocess")
        self.BtnStartprocess.setMaximumSize(QSize(698, 16777215))
        self.BtnStartprocess.setStyleSheet(u"QPushButton{\n"
"	border: 3px solid rgb(0, 0, 0);\n"
"	color: black;\n"
"	padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border: 5px solid rgb(0, 0, 0);\n"
"	color: rgb(57, 57, 57);\n"
"	padding: 3px;\n"
"	\n"
"}")

        self.horizontalLayout_3.addWidget(self.BtnStartprocess)


        self.verticalLayout_2.addWidget(self.frame_6)

        self.frame_16 = QFrame(self.tab)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMaximumSize(QSize(16777215, 50))
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.btnPlayVideo = QPushButton(self.frame_16)
        self.btnPlayVideo.setObjectName(u"btnPlayVideo")
        self.btnPlayVideo.setMaximumSize(QSize(698, 16777215))
        self.btnPlayVideo.setStyleSheet(u"QPushButton{\n"
                                        "	border: 3px solid rgb(0, 0, 0);\n"
                                        "	color: black;\n"
                                        "	padding: 5px;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover{\n"
                                        "	border: 5px solid rgb(0, 0, 0);\n"
                                        "	color: rgb(57, 57, 57);\n"
                                        "	padding: 3px;\n"
                                        "	\n"
                                        "}")

        self.horizontalLayout_11.addWidget(self.btnPlayVideo)

        self.verticalLayout_2.addWidget(self.frame_16)

        self.frame_4 = QFrame(self.tab)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(True)
        font1.setWeight(75)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"QLabel {\n"
"	color: rgb(0, 0, 0);\n"
"}")

        self.verticalLayout_3.addWidget(self.label)

        self.progressBar = QProgressBar(self.frame_4)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.verticalLayout_3.addWidget(self.progressBar)


        self.verticalLayout_2.addWidget(self.frame_4)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_5 = QVBoxLayout(self.tab_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_10 = QFrame(self.tab_2)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMaximumSize(QSize(16777215, 80))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_4 = QLabel(self.frame_10)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 60))
        self.label_4.setFont(font)

        self.horizontalLayout_6.addWidget(self.label_4)


        self.verticalLayout_5.addWidget(self.frame_10)

        self.frame_8 = QFrame(self.tab_2)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_8)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.plainTextEdit = QPlainTextEdit(self.frame_8)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.verticalLayout_7.addWidget(self.plainTextEdit)


        self.verticalLayout_5.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.tab_2)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMaximumSize(QSize(16777215, 250))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.frame_11 = QFrame(self.frame_9)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_11)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_12 = QFrame(self.frame_11)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
#         self.label_5 = QLabel(self.frame_12)
#         self.label_5.setObjectName(u"label_5")
#         self.label_5.setStyleSheet(u"QLabel{\n"
# "	border: 3px solid rgb(0, 0, 0);\n"
# "	color: black;\n"
# "	padding: 5px;\n"
# "}")

        # self.horizontalLayout_7.addWidget(self.label_5)


        self.verticalLayout_6.addWidget(self.frame_12)

        self.frame_13 = QFrame(self.frame_11)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.lineEdit_2 = QLineEdit(self.frame_13)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setStyleSheet(u"QLineEdit{\n"
"	border: 3px solid rgb(0, 0, 0);\n"
"	color: black;\n"
"	padding: 3px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border: 5px solid rgb(0, 0, 0);\n"
"	color: rgb(57, 57, 57);\n"
"	padding: 3px;\n"
"	\n"
"}")
        self.lineEdit_2.setCursorPosition(4)

        self.horizontalLayout_8.addWidget(self.lineEdit_2)

        self.btnChooseVideo_2 = QPushButton(self.frame_13)
        self.btnChooseVideo_2.setObjectName(u"btnChooseVideo_2")
        self.btnChooseVideo_2.setMinimumSize(QSize(100, 0))
        self.btnChooseVideo_2.setStyleSheet(u"QPushButton{\n"
"	border: 3px solid rgb(0, 0, 0);\n"
"	color: black;\n"
"	padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border: 5px solid rgb(0, 0, 0);\n"
"	color: rgb(57, 57, 57);\n"
"	padding: 5px;\n"
"	\n"
"}")

        self.horizontalLayout_8.addWidget(self.btnChooseVideo_2)


        self.verticalLayout_6.addWidget(self.frame_13)

        self.frame_15 = QFrame(self.frame_11)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.btnSaveLogs = QPushButton(self.frame_15)
        self.btnSaveLogs.setObjectName(u"btnSaveLogs")
        self.btnSaveLogs.setStyleSheet(u"QPushButton{\n"
"	border: 3px solid rgb(0, 0, 0);\n"
"	color: black;\n"
"	padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border: 5px solid rgb(0, 0, 0);\n"
"	color: rgb(57, 57, 57);\n"
"	padding: 5px;\n"
"	\n"
"}")

        self.horizontalLayout_10.addWidget(self.btnSaveLogs)


        self.verticalLayout_6.addWidget(self.frame_15)


        self.horizontalLayout_9.addWidget(self.frame_11)


        self.verticalLayout_5.addWidget(self.frame_9)

        self.frame_14 = QFrame(self.tab_2)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)

        self.verticalLayout_5.addWidget(self.frame_14)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout.addWidget(self.tabWidget)


        self.horizontalLayout.addWidget(self.frame)

        IO.setCentralWidget(self.centralwidget)

        self.retranslateUi(IO)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(IO)
    # setupUi

    def retranslateUi(self, IO):
        IO.setWindowTitle(QCoreApplication.translate("IO", u"IO Car Detector", None))
        self.label_2.setText(QCoreApplication.translate("IO", u"Car detector", None))
        # self.label_3.setText(QCoreApplication.translate("IO", u"Show file path", None))
        self.videoPath.setText(QCoreApplication.translate("IO", u"Video Path", None))
        self.btnChooseVideo.setText(QCoreApplication.translate("IO", u"Choose Video", None))
        self.btnPlayVideo.setText(QCoreApplication.translate("IO", u"Play Video", None))
        self.BtnStartprocess.setText(QCoreApplication.translate("IO", u"Start Processing ", None))
        self.label.setText(QCoreApplication.translate("IO", u"Progress:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("IO", u"Start", None))
        self.label_4.setText(QCoreApplication.translate("IO", u"LOGI", None))
        # self.label_5.setText(QCoreApplication.translate("IO", u"Show path where the logs should be saved ", None))
        self.lineEdit_2.setText(QCoreApplication.translate("IO", u"Logs Path", None))
        self.btnChooseVideo_2.setText(QCoreApplication.translate("IO", u"Choose Logs Path", None))
        self.btnSaveLogs.setText(QCoreApplication.translate("IO", u"Save Logs", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("IO", u"Logi", None))
    # retranslateUi

