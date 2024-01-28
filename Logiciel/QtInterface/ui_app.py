# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'app.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1100, 800)
        MainWindow.setAcceptDrops(True)
        icon = QIcon()
        icon.addFile(u":/logo/assets/logo/logo_3d_inc.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setIconSize(QSize(24, 24))
        MainWindow.setAnimated(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.menu = QFrame(self.centralwidget)
        self.menu.setObjectName(u"menu")
        self.menu.setMinimumSize(QSize(70, 0))
        self.menu.setMaximumSize(QSize(70, 16777215))
        self.menu.setStyleSheet(u"#menu {\n"
"	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(116, 182, 202, 255), stop:1 rgba(40, 58, 66, 255));\n"
"}\n"
"\n"
"#menu QPushButton {\n"
"    border:none;\n"
"    padding: 15px;\n"
"    color: #fff;\n"
"}\n"
"\n"
"#menu QPushButton:hover {\n"
"    background: #203b4850;\n"
"}")
        self.menu.setFrameShape(QFrame.StyledPanel)
        self.menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.menu)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.home_btn = QPushButton(self.menu)
        self.home_btn.setObjectName(u"home_btn")
        self.home_btn.setMinimumSize(QSize(70, 0))
        self.home_btn.setMaximumSize(QSize(70, 16777215))
        self.home_btn.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/logo/assets/logo/logo_white_inc.png", QSize(), QIcon.Normal, QIcon.Off)
        self.home_btn.setIcon(icon1)
        self.home_btn.setIconSize(QSize(35, 35))

        self.verticalLayout.addWidget(self.home_btn)

        self.export_btn = QPushButton(self.menu)
        self.export_btn.setObjectName(u"export_btn")
        self.export_btn.setMinimumSize(QSize(70, 0))
        self.export_btn.setMaximumSize(QSize(70, 16777215))
        self.export_btn.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/assets/icons/export.png", QSize(), QIcon.Normal, QIcon.Off)
        self.export_btn.setIcon(icon2)
        self.export_btn.setIconSize(QSize(35, 35))

        self.verticalLayout.addWidget(self.export_btn)

        self.import_btn = QPushButton(self.menu)
        self.import_btn.setObjectName(u"import_btn")
        self.import_btn.setMinimumSize(QSize(70, 0))
        self.import_btn.setMaximumSize(QSize(70, 16777215))
        self.import_btn.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/icons/assets/icons/import.png", QSize(), QIcon.Normal, QIcon.Off)
        self.import_btn.setIcon(icon3)
        self.import_btn.setIconSize(QSize(35, 35))

        self.verticalLayout.addWidget(self.import_btn)

        self.verticalSpacer = QSpacerItem(20, 543, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.config_btn = QPushButton(self.menu)
        self.config_btn.setObjectName(u"config_btn")
        self.config_btn.setMinimumSize(QSize(70, 0))
        self.config_btn.setMaximumSize(QSize(70, 16777215))
        self.config_btn.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u":/icons/assets/icons/settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.config_btn.setIcon(icon4)
        self.config_btn.setIconSize(QSize(35, 35))

        self.verticalLayout.addWidget(self.config_btn)


        self.horizontalLayout.addWidget(self.menu)

        self.main = QStackedWidget(self.centralwidget)
        self.main.setObjectName(u"main")
        self.main.setStyleSheet(u"QPushButton {\n"
"    color: #fff;\n"
"    border-radius: 3px!important;\n"
"    background-color: #429cb7;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #405258;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #2b727e;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	border: 2px solid #429cb7;\n"
"}")
        self.main.setFrameShape(QFrame.StyledPanel)
        self.main.setFrameShadow(QFrame.Raised)
        self.mainPage1 = QWidget()
        self.mainPage1.setObjectName(u"mainPage1")
        self.mainPage1.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.mainPage1)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(20, 20, 20, 20)
        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_11)

        self.label_11 = QLabel(self.mainPage1)
        self.label_11.setObjectName(u"label_11")
        font = QFont()
        font.setFamily(u"Inter")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet(u"")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_11)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_12)

        self.wifi_verticalFrame = QFrame(self.mainPage1)
        self.wifi_verticalFrame.setObjectName(u"wifi_verticalFrame")
        self.wifi_verticalLayout_1 = QVBoxLayout(self.wifi_verticalFrame)
        self.wifi_verticalLayout_1.setSpacing(0)
        self.wifi_verticalLayout_1.setObjectName(u"wifi_verticalLayout_1")
        self.wifi_verticalLayout_1.setContentsMargins(-1, 1, -1, -1)
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, -1, -1)
        self.label_wifi1_1 = QLabel(self.wifi_verticalFrame)
        self.label_wifi1_1.setObjectName(u"label_wifi1_1")
        self.label_wifi1_1.setMinimumSize(QSize(35, 35))
        self.label_wifi1_1.setMaximumSize(QSize(35, 35))
        self.label_wifi1_1.setPixmap(QPixmap(u":/icons/assets/icons/wifi.png"))
        self.label_wifi1_1.setScaledContents(True)
        self.label_wifi1_1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_16.addWidget(self.label_wifi1_1)


        self.wifi_verticalLayout_1.addLayout(self.horizontalLayout_16)

        self.label_wifi1_2 = QLabel(self.wifi_verticalFrame)
        self.label_wifi1_2.setObjectName(u"label_wifi1_2")
        font1 = QFont()
        font1.setFamily(u"Inter")
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setWeight(50)
        self.label_wifi1_2.setFont(font1)
        self.label_wifi1_2.setStyleSheet(u"color: #b74242;")
        self.label_wifi1_2.setAlignment(Qt.AlignCenter)

        self.wifi_verticalLayout_1.addWidget(self.label_wifi1_2)

        self.label_wifi1_3 = QLabel(self.wifi_verticalFrame)
        self.label_wifi1_3.setObjectName(u"label_wifi1_3")
        self.label_wifi1_3.setFont(font1)
        self.label_wifi1_3.setStyleSheet(u"color: #b74242;")
        self.label_wifi1_3.setAlignment(Qt.AlignCenter)

        self.wifi_verticalLayout_1.addWidget(self.label_wifi1_3)


        self.verticalLayout_2.addWidget(self.wifi_verticalFrame)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.label_logo = QLabel(self.mainPage1)
        self.label_logo.setObjectName(u"label_logo")
        self.label_logo.setMaximumSize(QSize(100, 101))
        self.label_logo.setPixmap(QPixmap(u":/logo/assets/logo/logo_3d_inc.png"))
        self.label_logo.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_logo)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.main.addWidget(self.mainPage1)
        self.mainPage2 = QWidget()
        self.mainPage2.setObjectName(u"mainPage2")
        self.mainPage2.setStyleSheet(u"")
        self.verticalLayout_3 = QVBoxLayout(self.mainPage2)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(20, 20, 20, 20)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.teacher_comboBox = QComboBox(self.mainPage2)
        self.teacher_comboBox.addItem("")
        self.teacher_comboBox.setObjectName(u"teacher_comboBox")
        self.teacher_comboBox.setMinimumSize(QSize(0, 33))
        font2 = QFont()
        font2.setFamily(u"Inter")
        font2.setPointSize(10)
        self.teacher_comboBox.setFont(font2)

        self.horizontalLayout_3.addWidget(self.teacher_comboBox)

        self.promo_comboBox = QComboBox(self.mainPage2)
        self.promo_comboBox.addItem("")
        self.promo_comboBox.setObjectName(u"promo_comboBox")
        self.promo_comboBox.setMinimumSize(QSize(0, 33))
        self.promo_comboBox.setFont(font2)

        self.horizontalLayout_3.addWidget(self.promo_comboBox)

        self.groupe_comboBox = QComboBox(self.mainPage2)
        self.groupe_comboBox.addItem("")
        self.groupe_comboBox.setObjectName(u"groupe_comboBox")
        self.groupe_comboBox.setMinimumSize(QSize(0, 33))
        self.groupe_comboBox.setFont(font2)

        self.horizontalLayout_3.addWidget(self.groupe_comboBox)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.verticalFrame = QFrame(self.mainPage2)
        self.verticalFrame.setObjectName(u"verticalFrame")
        self.verticalFrame.setStyleSheet(u"/*#verticalFrame {border: 2px solid; border-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(116, 182, 202, 255), stop:1 rgba(40, 58, 66, 255));}*/\n"
"#verticalFrame {border: 2px solid; border-color: #2b727e;}")
        self.verticalLayout_7 = QVBoxLayout(self.verticalFrame)
        self.verticalLayout_7.setSpacing(10)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(7, 7, 7, 10)
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.date_label = QLabel(self.verticalFrame)
        self.date_label.setObjectName(u"date_label")
        self.date_label.setFont(font2)

        self.horizontalLayout_9.addWidget(self.date_label)

        self.info_label = QLabel(self.verticalFrame)
        self.info_label.setObjectName(u"info_label")
        self.info_label.setMinimumSize(QSize(30, 30))
        self.info_label.setMaximumSize(QSize(30, 30))
        self.info_label.setFont(font2)
        self.info_label.setPixmap(QPixmap(u":/icons/assets/icons/info.png"))
        self.info_label.setScaledContents(True)

        self.horizontalLayout_9.addWidget(self.info_label)


        self.verticalLayout_7.addLayout(self.horizontalLayout_9)

        self.teacher_label = QLabel(self.verticalFrame)
        self.teacher_label.setObjectName(u"teacher_label")
        self.teacher_label.setFont(font2)

        self.verticalLayout_7.addWidget(self.teacher_label)

        self.promo_label = QLabel(self.verticalFrame)
        self.promo_label.setObjectName(u"promo_label")
        self.promo_label.setFont(font2)

        self.verticalLayout_7.addWidget(self.promo_label)

        self.group_label = QLabel(self.verticalFrame)
        self.group_label.setObjectName(u"group_label")
        self.group_label.setFont(font2)

        self.verticalLayout_7.addWidget(self.group_label)


        self.verticalLayout_3.addWidget(self.verticalFrame)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setSpacing(10)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(-1, 0, -1, -1)
        self.general_status = QLabel(self.mainPage2)
        self.general_status.setObjectName(u"general_status")
        self.general_status.setFont(font2)

        self.verticalLayout_8.addWidget(self.general_status)

        self.api_status = QLabel(self.mainPage2)
        self.api_status.setObjectName(u"api_status")
        self.api_status.setFont(font2)

        self.verticalLayout_8.addWidget(self.api_status)

        self.pdf_generation_status = QLabel(self.mainPage2)
        self.pdf_generation_status.setObjectName(u"pdf_generation_status")
        self.pdf_generation_status.setFont(font2)

        self.verticalLayout_8.addWidget(self.pdf_generation_status)

        self.mail_sending_status = QLabel(self.mainPage2)
        self.mail_sending_status.setObjectName(u"mail_sending_status")
        self.mail_sending_status.setFont(font2)

        self.verticalLayout_8.addWidget(self.mail_sending_status)


        self.verticalLayout_3.addLayout(self.verticalLayout_8)

        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_13)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.checkBox = QCheckBox(self.mainPage2)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setEnabled(False)
        self.checkBox.setFont(font2)
        self.checkBox.setStyleSheet(u"QCheckBox::indicator::checked {\n"
"	background-color : #429cb7;\n"
"}")

        self.horizontalLayout_4.addWidget(self.checkBox)

        self.generate_btn = QPushButton(self.mainPage2)
        self.generate_btn.setObjectName(u"generate_btn")
        self.generate_btn.setMinimumSize(QSize(150, 33))
        self.generate_btn.setFont(font2)
        self.generate_btn.setStyleSheet(u"")

        self.horizontalLayout_4.addWidget(self.generate_btn)

        self.send_btn = QPushButton(self.mainPage2)
        self.send_btn.setObjectName(u"send_btn")
        self.send_btn.setEnabled(False)
        self.send_btn.setMinimumSize(QSize(150, 33))
        self.send_btn.setFont(font2)

        self.horizontalLayout_4.addWidget(self.send_btn)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.main.addWidget(self.mainPage2)
        self.mainPage3 = QWidget()
        self.mainPage3.setObjectName(u"mainPage3")
        self.verticalLayout_4 = QVBoxLayout(self.mainPage3)
        self.verticalLayout_4.setSpacing(20)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(20, 20, 20, 20)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(10)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(10)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, -1, -1, -1)
        self.import_file = QPushButton(self.mainPage3)
        self.import_file.setObjectName(u"import_file")
        self.import_file.setMinimumSize(QSize(200, 33))
        self.import_file.setFont(font2)
        self.import_file.setAcceptDrops(False)

        self.verticalLayout_6.addWidget(self.import_file)

        self.import_success_label = QLabel(self.mainPage3)
        self.import_success_label.setObjectName(u"import_success_label")
        font3 = QFont()
        font3.setFamily(u"Inter")
        font3.setPointSize(8)
        self.import_success_label.setFont(font3)
        self.import_success_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_6.addWidget(self.import_success_label)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_4)

        self.tableTitle_1 = QLabel(self.mainPage3)
        self.tableTitle_1.setObjectName(u"tableTitle_1")
        self.tableTitle_1.setFont(font2)

        self.verticalLayout_6.addWidget(self.tableTitle_1)

        self.tableTitle_4 = QLabel(self.mainPage3)
        self.tableTitle_4.setObjectName(u"tableTitle_4")
        self.tableTitle_4.setFont(font2)

        self.verticalLayout_6.addWidget(self.tableTitle_4)

        self.tableTitle_2 = QLabel(self.mainPage3)
        self.tableTitle_2.setObjectName(u"tableTitle_2")
        self.tableTitle_2.setFont(font2)

        self.verticalLayout_6.addWidget(self.tableTitle_2)

        self.tableTitle_3 = QLabel(self.mainPage3)
        self.tableTitle_3.setObjectName(u"tableTitle_3")
        self.tableTitle_3.setFont(font2)

        self.verticalLayout_6.addWidget(self.tableTitle_3)

        self.Stat_label_1 = QLabel(self.mainPage3)
        self.Stat_label_1.setObjectName(u"Stat_label_1")
        self.Stat_label_1.setFont(font2)

        self.verticalLayout_6.addWidget(self.Stat_label_1)

        self.Stat_label_2 = QLabel(self.mainPage3)
        self.Stat_label_2.setObjectName(u"Stat_label_2")
        self.Stat_label_2.setFont(font2)

        self.verticalLayout_6.addWidget(self.Stat_label_2)

        self.Stat_label_3 = QLabel(self.mainPage3)
        self.Stat_label_3.setObjectName(u"Stat_label_3")
        self.Stat_label_3.setFont(font2)

        self.verticalLayout_6.addWidget(self.Stat_label_3)


        self.horizontalLayout_6.addLayout(self.verticalLayout_6)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setSpacing(10)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.pageTitle = QLabel(self.mainPage3)
        self.pageTitle.setObjectName(u"pageTitle")
        font4 = QFont()
        font4.setFamily(u"Inter")
        font4.setPointSize(12)
        self.pageTitle.setFont(font4)

        self.horizontalLayout_10.addWidget(self.pageTitle)

        self.previous_btn = QPushButton(self.mainPage3)
        self.previous_btn.setObjectName(u"previous_btn")
        self.previous_btn.setMinimumSize(QSize(33, 33))
        self.previous_btn.setMaximumSize(QSize(33, 33))
        icon5 = QIcon()
        icon5.addFile(u":/icons/assets/icons/previous.png", QSize(), QIcon.Normal, QIcon.Off)
        self.previous_btn.setIcon(icon5)

        self.horizontalLayout_10.addWidget(self.previous_btn)

        self.next_btn = QPushButton(self.mainPage3)
        self.next_btn.setObjectName(u"next_btn")
        self.next_btn.setMinimumSize(QSize(33, 33))
        self.next_btn.setMaximumSize(QSize(33, 33))
        icon6 = QIcon()
        icon6.addFile(u":/icons/assets/icons/next.png", QSize(), QIcon.Normal, QIcon.Off)
        self.next_btn.setIcon(icon6)
        self.next_btn.setIconSize(QSize(25, 16))

        self.horizontalLayout_10.addWidget(self.next_btn)


        self.verticalLayout_5.addLayout(self.horizontalLayout_10)

        self.tableWidget = QTableWidget(self.mainPage3)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")
        font5 = QFont()
        font5.setFamily(u"Inter")
        self.tableWidget.setFont(font5)
        self.tableWidget.setStyleSheet(u"QTableWidget::item{ selection-background-color: transparent;selection-color: unset;}")
        self.tableWidget.setGridStyle(Qt.DashDotDotLine)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setCornerButtonEnabled(False)
        self.tableWidget.setColumnCount(4)

        self.verticalLayout_5.addWidget(self.tableWidget)


        self.horizontalLayout_6.addLayout(self.verticalLayout_5)


        self.verticalLayout_4.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.loading_label_2 = QLabel(self.mainPage3)
        self.loading_label_2.setObjectName(u"loading_label_2")
        self.loading_label_2.setMinimumSize(QSize(200, 0))
        self.loading_label_2.setFont(font4)
        self.loading_label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.loading_label_2)

        self.saveScan_btn = QPushButton(self.mainPage3)
        self.saveScan_btn.setObjectName(u"saveScan_btn")
        self.saveScan_btn.setEnabled(True)
        self.saveScan_btn.setMinimumSize(QSize(155, 33))
        self.saveScan_btn.setFont(font2)

        self.horizontalLayout_5.addWidget(self.saveScan_btn)

        self.saveToDB_btn = QPushButton(self.mainPage3)
        self.saveToDB_btn.setObjectName(u"saveToDB_btn")
        self.saveToDB_btn.setMinimumSize(QSize(185, 33))
        self.saveToDB_btn.setFont(font2)

        self.horizontalLayout_5.addWidget(self.saveToDB_btn)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.main.addWidget(self.mainPage3)
        self.mainPage_35 = QWidget()
        self.mainPage_35.setObjectName(u"mainPage_35")
        self.verticalLayout_23 = QVBoxLayout(self.mainPage_35)
        self.verticalLayout_23.setSpacing(10)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(20, 20, 20, 20)
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_10)

        self.check_btn_return = QPushButton(self.mainPage_35)
        self.check_btn_return.setObjectName(u"check_btn_return")
        self.check_btn_return.setMinimumSize(QSize(33, 33))
        self.check_btn_return.setMaximumSize(QSize(33, 33))
        self.check_btn_return.setFont(font2)
        self.check_btn_return.setStyleSheet(u"QPushButton {background-color: #b74242!important;}\n"
"\n"
":hover {background-color: #7e2b2b!important;}")
        icon7 = QIcon()
        icon7.addFile(u":/icons/assets/icons/close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.check_btn_return.setIcon(icon7)
        self.check_btn_return.setIconSize(QSize(25, 25))

        self.horizontalLayout_11.addWidget(self.check_btn_return)


        self.verticalLayout_23.addLayout(self.horizontalLayout_11)

        self.proofImage_label = QLabel(self.mainPage_35)
        self.proofImage_label.setObjectName(u"proofImage_label")
        self.proofImage_label.setFont(font2)
        self.proofImage_label.setScaledContents(True)

        self.verticalLayout_23.addWidget(self.proofImage_label)

        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.proofStudent_label = QLabel(self.mainPage_35)
        self.proofStudent_label.setObjectName(u"proofStudent_label")
        self.proofStudent_label.setFont(font2)

        self.verticalLayout_22.addWidget(self.proofStudent_label)

        self.proofSign_label = QLabel(self.mainPage_35)
        self.proofSign_label.setObjectName(u"proofSign_label")
        self.proofSign_label.setFont(font2)

        self.verticalLayout_22.addWidget(self.proofSign_label)

        self.proofSure_label = QLabel(self.mainPage_35)
        self.proofSure_label.setObjectName(u"proofSure_label")
        self.proofSure_label.setFont(font2)

        self.verticalLayout_22.addWidget(self.proofSure_label)


        self.verticalLayout_23.addLayout(self.verticalLayout_22)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_23.addItem(self.verticalSpacer_10)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_9)

        self.check_btn_refuse = QPushButton(self.mainPage_35)
        self.check_btn_refuse.setObjectName(u"check_btn_refuse")
        self.check_btn_refuse.setMinimumSize(QSize(150, 33))
        self.check_btn_refuse.setMaximumSize(QSize(150, 33))
        self.check_btn_refuse.setFont(font2)
        self.check_btn_refuse.setStyleSheet(u"QPushButton {background-color: #b74242!important;}\n"
"\n"
":hover {background-color: #7e2b2b!important;}")

        self.horizontalLayout_8.addWidget(self.check_btn_refuse)

        self.check_btn_ok = QPushButton(self.mainPage_35)
        self.check_btn_ok.setObjectName(u"check_btn_ok")
        self.check_btn_ok.setMinimumSize(QSize(150, 33))
        self.check_btn_ok.setMaximumSize(QSize(150, 33))
        self.check_btn_ok.setFont(font2)

        self.horizontalLayout_8.addWidget(self.check_btn_ok)


        self.verticalLayout_23.addLayout(self.horizontalLayout_8)

        self.main.addWidget(self.mainPage_35)
        self.mainPage4 = QWidget()
        self.mainPage4.setObjectName(u"mainPage4")
        self.verticalLayout_9 = QVBoxLayout(self.mainPage4)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.config_tabWidget = QTabWidget(self.mainPage4)
        self.config_tabWidget.setObjectName(u"config_tabWidget")
        self.config_tabWidget.setStyleSheet(u"QSlider::handle:horizontal {\n"
"    background-color: #429cb7;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: #2b727e;\n"
"}")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tab_2.setFont(font2)
        self.verticalLayout_16 = QVBoxLayout(self.tab_2)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.groupBox_2 = QGroupBox(self.tab_2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_17 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(-1, 15, -1, -1)
        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName(u"gridLayout")
        self.low_slider = QSlider(self.groupBox_2)
        self.low_slider.setObjectName(u"low_slider")
        self.low_slider.setValue(30)
        self.low_slider.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.low_slider, 0, 1, 1, 1)

        self.low_label = QLabel(self.groupBox_2)
        self.low_label.setObjectName(u"low_label")
        self.low_label.setFont(font2)

        self.gridLayout.addWidget(self.low_label, 0, 2, 1, 1)

        self.low_label_2 = QLabel(self.groupBox_2)
        self.low_label_2.setObjectName(u"low_label_2")
        self.low_label_2.setFont(font2)

        self.gridLayout.addWidget(self.low_label_2, 0, 3, 1, 1)

        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(20, 20))
        self.label_4.setMaximumSize(QSize(20, 20))
        font6 = QFont()
        font6.setFamily(u"Inter")
        font6.setPointSize(10)
        font6.setBold(True)
        font6.setWeight(75)
        self.label_4.setFont(font6)
        self.label_4.setStyleSheet(u"border : 1px solid #2b727e;\n"
"font-weight : bold;\n"
"color: white;\n"
"background-color: #429cb7;\n"
"border-top-left-radius : 5px;\n"
"border-top-right-radius : 5px;\n"
"border-bottom-left-radius : 5px;\n"
"border-bottom-right-radius : 5px;")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_4, 0, 4, 1, 1)

        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font2)

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font2)

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.high_slider = QSlider(self.groupBox_2)
        self.high_slider.setObjectName(u"high_slider")
        self.high_slider.setValue(80)
        self.high_slider.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.high_slider, 1, 1, 1, 1)

        self.high_label = QLabel(self.groupBox_2)
        self.high_label.setObjectName(u"high_label")
        self.high_label.setFont(font2)

        self.gridLayout.addWidget(self.high_label, 1, 2, 1, 1)

        self.high_label_2 = QLabel(self.groupBox_2)
        self.high_label_2.setObjectName(u"high_label_2")
        self.high_label_2.setFont(font2)

        self.gridLayout.addWidget(self.high_label_2, 1, 3, 1, 1)

        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(20, 20))
        self.label_5.setMaximumSize(QSize(20, 18))
        self.label_5.setFont(font6)
        self.label_5.setStyleSheet(u"border : 1px solid #2b727e;\n"
"font-weight : bold;\n"
"color: white;\n"
"background-color: #429cb7;\n"
"border-top-left-radius : 5px;\n"
"border-top-right-radius : 5px;\n"
"border-bottom-left-radius : 5px;\n"
"border-bottom-right-radius : 5px;")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_5, 1, 4, 1, 1)


        self.verticalLayout_17.addLayout(self.gridLayout)

        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font2)

        self.verticalLayout_17.addWidget(self.label_6)


        self.verticalLayout_16.addWidget(self.groupBox_2)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_16.addItem(self.verticalSpacer_8)

        self.config_tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tab_3.setFont(font2)
        self.verticalLayout_14 = QVBoxLayout(self.tab_3)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.groupBox = QGroupBox(self.tab_3)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_15 = QVBoxLayout(self.groupBox)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(-1, 15, -1, -1)
        self.theme_combobox = QComboBox(self.groupBox)
        self.theme_combobox.addItem("")
        self.theme_combobox.addItem("")
        self.theme_combobox.addItem("")
        self.theme_combobox.setObjectName(u"theme_combobox")
        self.theme_combobox.setEnabled(True)
        self.theme_combobox.setMinimumSize(QSize(150, 33))
        self.theme_combobox.setMaximumSize(QSize(150, 33))
        self.theme_combobox.setFont(font2)

        self.verticalLayout_15.addWidget(self.theme_combobox)


        self.verticalLayout_14.addWidget(self.groupBox)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer_7)

        self.config_tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.tab_4.setFont(font2)
        self.verticalLayout_11 = QVBoxLayout(self.tab_4)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setSpacing(10)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(-1, 0, -1, -1)
        self.aPropo_label_1 = QLabel(self.tab_4)
        self.aPropo_label_1.setObjectName(u"aPropo_label_1")
        self.aPropo_label_1.setFont(font2)
        self.aPropo_label_1.setWordWrap(True)

        self.verticalLayout_10.addWidget(self.aPropo_label_1)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setSpacing(10)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setSpacing(10)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(-1, -1, 0, -1)
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_13.addItem(self.horizontalSpacer_4)


        self.horizontalLayout_12.addLayout(self.verticalLayout_13)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setSpacing(20)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, -1, -1)
        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_5)

        self.miage_label_2 = QLabel(self.tab_4)
        self.miage_label_2.setObjectName(u"miage_label_2")
        self.miage_label_2.setMinimumSize(QSize(231, 80))
        self.miage_label_2.setMaximumSize(QSize(231, 80))
        self.miage_label_2.setPixmap(QPixmap(u":/img/assets/uca.png"))
        self.miage_label_2.setScaledContents(True)

        self.verticalLayout_12.addWidget(self.miage_label_2)

        self.miage_label = QLabel(self.tab_4)
        self.miage_label.setObjectName(u"miage_label")
        self.miage_label.setMinimumSize(QSize(231, 53))
        self.miage_label.setMaximumSize(QSize(231, 53))
        self.miage_label.setLayoutDirection(Qt.LeftToRight)
        self.miage_label.setPixmap(QPixmap(u":/img/assets/miage.png"))
        self.miage_label.setScaledContents(True)
        self.miage_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.miage_label)


        self.horizontalLayout_12.addLayout(self.verticalLayout_12)


        self.verticalLayout_10.addLayout(self.horizontalLayout_12)


        self.verticalLayout_11.addLayout(self.verticalLayout_10)

        self.config_tabWidget.addTab(self.tab_4, "")

        self.verticalLayout_9.addWidget(self.config_tabWidget)

        self.main.addWidget(self.mainPage4)

        self.horizontalLayout.addWidget(self.main)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.main.setCurrentIndex(0)
        self.config_tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"SignatureChecker", None))
        self.home_btn.setText("")
        self.export_btn.setText("")
        self.import_btn.setText("")
        self.config_btn.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Bienvenue sur SignatureChecker.", None))
        self.label_wifi1_1.setText("")
        self.label_wifi1_2.setText(QCoreApplication.translate("MainWindow", u"R\u00e9seau d\u00e9connect\u00e9", None))
        self.label_wifi1_3.setText(QCoreApplication.translate("MainWindow", u"Certaines fonctionnalit\u00e9s ne sont pas disponibles", None))
        self.label_logo.setText("")
        self.teacher_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Enseignant...", None))

        self.promo_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Promotion...", None))

        self.groupe_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Groupe de TD/TP...", None))

        self.date_label.setText(QCoreApplication.translate("MainWindow", u"Les feuilles de pr\u00e9sences du # au # vont \u00eatre g\u00e9n\u00e9r\u00e9es avec les param\u00e8tres suivants :", None))
        self.info_label.setText("")
        self.teacher_label.setText(QCoreApplication.translate("MainWindow", u"Enseignant : Tous les enseignants", None))
        self.promo_label.setText(QCoreApplication.translate("MainWindow", u"Promotion : Toutes les promotions", None))
        self.group_label.setText(QCoreApplication.translate("MainWindow", u"Groupe : Tous les groupes", None))
        self.general_status.setText("")
        self.api_status.setText("")
        self.pdf_generation_status.setText("")
        self.mail_sending_status.setText("")
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Inclure les s\u00e9ances expir\u00e9es", None))
        self.generate_btn.setText(QCoreApplication.translate("MainWindow", u"G\u00c9N\u00c9RER PDF", None))
        self.send_btn.setText(QCoreApplication.translate("MainWindow", u"ENVOYER PDF", None))
        self.import_file.setText(QCoreApplication.translate("MainWindow", u"IMPORTER UN  PDF", None))
        self.import_success_label.setText("")
        self.tableTitle_1.setText(QCoreApplication.translate("MainWindow", u"NOM ENSEIGNANT,", None))
        self.tableTitle_4.setText(QCoreApplication.translate("MainWindow", u"PROMO", None))
        self.tableTitle_2.setText(QCoreApplication.translate("MainWindow", u"COURS,", None))
        self.tableTitle_3.setText(QCoreApplication.translate("MainWindow", u"DATE ET HEURE", None))
        self.Stat_label_1.setText(QCoreApplication.translate("MainWindow", u"A sign\u00e9", None))
        self.Stat_label_2.setText(QCoreApplication.translate("MainWindow", u"N'a pas sign\u00e9", None))
        self.Stat_label_3.setText(QCoreApplication.translate("MainWindow", u"\u00c0 v\u00e9rifier", None))
        self.pageTitle.setText(QCoreApplication.translate("MainWindow", u"Feuille N\u00b0 #", None))
        self.previous_btn.setText("")
        self.next_btn.setText("")
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u00c9tudiant", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"A sign\u00e9", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Fiabilit\u00e9", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"V\u00e9rifier", None));
        self.loading_label_2.setText("")
        self.saveScan_btn.setText(QCoreApplication.translate("MainWindow", u"EXPORTER EN XLSX", None))
        self.saveToDB_btn.setText(QCoreApplication.translate("MainWindow", u"EXPORTER VERS LA BDD", None))
        self.check_btn_return.setText("")
        self.proofImage_label.setText(QCoreApplication.translate("MainWindow", u"IMAGE", None))
        self.proofStudent_label.setText(QCoreApplication.translate("MainWindow", u"Etudiant", None))
        self.proofSign_label.setText(QCoreApplication.translate("MainWindow", u"A sign\u00e9", None))
        self.proofSure_label.setText(QCoreApplication.translate("MainWindow", u"Fiabili\u00e9", None))
        self.check_btn_refuse.setText(QCoreApplication.translate("MainWindow", u"REFUSER", None))
        self.check_btn_ok.setText(QCoreApplication.translate("MainWindow", u"VALIDER", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Tol\u00e9rance pour l'acceptation d'une signature", None))
        self.low_label.setText(QCoreApplication.translate("MainWindow", u"30", None))
        self.low_label_2.setText(QCoreApplication.translate("MainWindow", u"%", None))
#if QT_CONFIG(tooltip)
        self.label_4.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\"><span style=\" font-family:'Courier New'; font-size:10pt;\">Refuse toute signature avec une fiabilit\u00e9 inf\u00e9rieur \u00e0 la valeur choisis. </span></p><p align=\"justify\"><span style=\" font-family:'Courier New'; font-size:10pt;\">Exemple si 30 est choisis, toutes signatures avec une fiabilit\u00e9 de moin de 30% sera rejet\u00e9</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"?", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Refuser si fiabilit\u00e9 inf\u00e9rieure \u00e0", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Accepter si sup\u00e9rieure ou \u00e9gale \u00e0", None))
        self.high_label.setText(QCoreApplication.translate("MainWindow", u"80", None))
        self.high_label_2.setText(QCoreApplication.translate("MainWindow", u"%", None))
#if QT_CONFIG(tooltip)
        self.label_5.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\"><span style=\" font-family:'Courier New'; font-size:10pt;\">Accepte toute signature avec une fiabilit\u00e9 sup\u00e9rieur \u00e0 la valeur choisis. </span></p><p align=\"justify\"><span style=\" font-family:'Courier New'; font-size:10pt;\">Exemple si 80 est choisis, toutes signatures avec une fiabilit\u00e9 de plus 80% ou plus sera accept\u00e9.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"?", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\">Toutes signatures entre ces deux valeurs seront signal\u00e9es comme <span style=\" font-weight:600;\">douteuses</span> et devront donc \u00eatre verifi\u00e9es.</p></body></html>", None))
        self.config_tabWidget.setTabText(self.config_tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tol\u00e9rance", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Th\u00e8me", None))
        self.theme_combobox.setItemText(0, QCoreApplication.translate("MainWindow", u"Auto", None))
        self.theme_combobox.setItemText(1, QCoreApplication.translate("MainWindow", u"Sombre", None))
        self.theme_combobox.setItemText(2, QCoreApplication.translate("MainWindow", u"Classique ", None))

        self.config_tabWidget.setTabText(self.config_tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Autre", None))
        self.aPropo_label_1.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Inter'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">SignatureChecker</span> 3.0 est un logiciel con\u00e7u pour optimiser le contr\u00f4le des pr\u00e9sences \u00e0 l'<span style=\" font-weight:600;\">Universit\u00e9 C\u00f4te d'Azur</span>. Il permet la cr\u00e9ation rapide et efficace de feuilles d'\u00e9margement et utilise la reconnaissance optique des caract\u00e8res pour analyser avec pr\u00e9cision et fiabilit\u00e9 les signatures pour d\u00e9terminer les pr\u00e9sences et absences. Cette solution offre un gain de temps consid\u00e9rable et une vue claire "
                        "et pr\u00e9cise de l'assiduit\u00e9 des \u00e9tudiants.</p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"p15\"></a>Auteurs :<a name=\"p16\"></a> <a name=\"19\"></a>Admessiev Ayoub, <a name=\"20\"></a>Sahli <a name=\"21\"></a>Mootez, <a name=\"22\"></a>Aarji Yahya, <a name=\"23\"></a>Toure Lamine, <a name=\"24\"></a>Hakobyan Arman.<a name=\"p17\"></a> \u00c9tudiant en Master 1 <a name=\"25\"></a>MIAGE.</p></body></html>", None))
        self.miage_label_2.setText("")
        self.miage_label.setText("")
        self.config_tabWidget.setTabText(self.config_tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"\u00c0 propos", None))
    # retranslateUi

