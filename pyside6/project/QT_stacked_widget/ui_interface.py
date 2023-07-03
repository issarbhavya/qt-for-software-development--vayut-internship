# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfacegfMIIF.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStackedWidget, QStatusBar, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(819, 465)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QPushButton {\n"
"    background-color: #4CAF50; /* Green background color */\n"
"    color: white; /* Text color */\n"
"    padding: 10px 20px; /* Padding around the button text */\n"
"    border: none; /* No border */\n"
"    border-radius: 5px; /* Rounded corners */\n"
"    font-size: 13px; /* Font size */\n"
"}\n"
"\n"
"QLabel {\n"
"    color: #333333; /* Text color */\n"
"    font-size: 12px; /* Font size */\n"
"    font-weight: bold; /* Font weight */\n"
"}\n"
"\n"
"")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.left_menu_widget = QWidget(self.centralwidget)
        self.left_menu_widget.setObjectName(u"left_menu_widget")
        self.left_menu_widget.setStyleSheet(u"QFrame {\n"
"    border: 1px solid #000000; /* 1px solid black border for all frames */\n"
"}")
        self.verticalLayout = QVBoxLayout(self.left_menu_widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_3 = QFrame(self.left_menu_widget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u" font-size: 16px; font-weight: bold;")

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.left_menu_widget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.percentage_bar_button = QPushButton(self.frame_4)
        self.percentage_bar_button.setObjectName(u"percentage_bar_button")
        self.percentage_bar_button.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/icons/icons/chart-column-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.percentage_bar_button.setIcon(icon)

        self.verticalLayout_2.addWidget(self.percentage_bar_button)

        self.temperature_record_button = QPushButton(self.frame_4)
        self.temperature_record_button.setObjectName(u"temperature_record_button")
        self.temperature_record_button.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/temp-svgrepo-com.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.temperature_record_button.setIcon(icon1)

        self.verticalLayout_2.addWidget(self.temperature_record_button)

        self.nested_donut_button = QPushButton(self.frame_4)
        self.nested_donut_button.setObjectName(u"nested_donut_button")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/pie-chart-svgrepo-com.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.nested_donut_button.setIcon(icon2)

        self.verticalLayout_2.addWidget(self.nested_donut_button)

        self.line_chart_button = QPushButton(self.frame_4)
        self.line_chart_button.setObjectName(u"line_chart_button")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/chart-line-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.line_chart_button.setIcon(icon3)

        self.verticalLayout_2.addWidget(self.line_chart_button)

        self.bar_chart_button = QPushButton(self.frame_4)
        self.bar_chart_button.setObjectName(u"bar_chart_button")
        self.bar_chart_button.setIcon(icon)

        self.verticalLayout_2.addWidget(self.bar_chart_button)


        self.verticalLayout.addWidget(self.frame_4)


        self.horizontalLayout.addWidget(self.left_menu_widget)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_7 = QFrame(self.frame_2)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.frame_10 = QFrame(self.frame_7)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pushButton_6 = QPushButton(self.frame_10)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.horizontalLayout_5.addWidget(self.pushButton_6)


        self.horizontalLayout_4.addWidget(self.frame_10)

        self.frame_12 = QFrame(self.frame_7)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_7 = QLabel(self.frame_12)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_6.addWidget(self.label_7)


        self.horizontalLayout_4.addWidget(self.frame_12)

        self.frame_11 = QFrame(self.frame_7)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.pushButton_9 = QPushButton(self.frame_11)
        self.pushButton_9.setObjectName(u"pushButton_9")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/cross-svgrepo-com.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_9.setIcon(icon4)

        self.horizontalLayout_7.addWidget(self.pushButton_9)


        self.horizontalLayout_4.addWidget(self.frame_11)


        self.verticalLayout_4.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.frame_2)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_8)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.stackedWidget = QStackedWidget(self.frame_8)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"QFrame#frame_16#fame_17#fame_24#fame_25 {\n"
"    border: 1px solid #000000; /* 1px solid black border for all frames */\n"
"}")
        self.line_chart = QWidget()
        self.line_chart.setObjectName(u"line_chart")
        self.line_chart.setStyleSheet(u"")
        self.verticalLayout_6 = QVBoxLayout(self.line_chart)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_16 = QFrame(self.line_chart)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setStyleSheet(u"QFrame#frame_16 {\n"
"    border: 1px solid #000000; /* 1px solid black border for all frames */\n"
"}")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_16)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_9 = QLabel(self.frame_16)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_9, 0, Qt.AlignTop)


        self.verticalLayout_6.addWidget(self.frame_16)

        self.frame_17 = QFrame(self.line_chart)
        self.frame_17.setObjectName(u"frame_17")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_17.sizePolicy().hasHeightForWidth())
        self.frame_17.setSizePolicy(sizePolicy)
        self.frame_17.setStyleSheet(u"QFrame#frame_17 {\n"
"    border: 1px solid #000000; /* 1px solid black border for all frames */\n"
"}")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_17)
        self.gridLayout.setObjectName(u"gridLayout")

        self.verticalLayout_6.addWidget(self.frame_17)

        self.stackedWidget.addWidget(self.line_chart)
        self.temperature_records = QWidget()
        self.temperature_records.setObjectName(u"temperature_records")
        self.verticalLayout_9 = QVBoxLayout(self.temperature_records)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frame_18 = QFrame(self.temperature_records)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setStyleSheet(u"QFrame#frame_18 {\n"
"    border: 1px solid #000000; /* 1px solid black border for all frames */\n"
"}")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_18)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_10 = QLabel(self.frame_18)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_10, 0, Qt.AlignTop)


        self.verticalLayout_9.addWidget(self.frame_18)

        self.frame_19 = QFrame(self.temperature_records)
        self.frame_19.setObjectName(u"frame_19")
        sizePolicy.setHeightForWidth(self.frame_19.sizePolicy().hasHeightForWidth())
        self.frame_19.setSizePolicy(sizePolicy)
        self.frame_19.setStyleSheet(u"QFrame {\n"
"    border: 1px solid #000000; /* 1px solid black border for all frames */\n"
"}")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_19)
        self.gridLayout_2.setObjectName(u"gridLayout_2")

        self.verticalLayout_9.addWidget(self.frame_19)

        self.stackedWidget.addWidget(self.temperature_records)
        self.nested_donuts = QWidget()
        self.nested_donuts.setObjectName(u"nested_donuts")
        self.verticalLayout_11 = QVBoxLayout(self.nested_donuts)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame_20 = QFrame(self.nested_donuts)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setStyleSheet(u"QFrame#frame_20 {\n"
"    border: 1px solid #000000; /* 1px solid black border for all frames */\n"
"}")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_20)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_11 = QLabel(self.frame_20)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_11, 0, Qt.AlignTop)


        self.verticalLayout_11.addWidget(self.frame_20)

        self.frame_21 = QFrame(self.nested_donuts)
        self.frame_21.setObjectName(u"frame_21")
        sizePolicy.setHeightForWidth(self.frame_21.sizePolicy().hasHeightForWidth())
        self.frame_21.setSizePolicy(sizePolicy)
        self.frame_21.setStyleSheet(u"QFrame#frame_21 {\n"
"    border: 1px solid #000000; /* 1px solid black border for all frames */\n"
"}")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_21)
        self.gridLayout_3.setObjectName(u"gridLayout_3")

        self.verticalLayout_11.addWidget(self.frame_21)

        self.stackedWidget.addWidget(self.nested_donuts)
        self.percentage_bar_chart = QWidget()
        self.percentage_bar_chart.setObjectName(u"percentage_bar_chart")
        self.verticalLayout_13 = QVBoxLayout(self.percentage_bar_chart)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.frame_22 = QFrame(self.percentage_bar_chart)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setStyleSheet(u"QFrame#frame_22 {\n"
"    border: 1px solid #000000; /* 1px solid black border for all frames */\n"
"}")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_22)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_12 = QLabel(self.frame_22)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_12, 0, Qt.AlignTop)


        self.verticalLayout_13.addWidget(self.frame_22)

        self.frame_23 = QFrame(self.percentage_bar_chart)
        self.frame_23.setObjectName(u"frame_23")
        sizePolicy.setHeightForWidth(self.frame_23.sizePolicy().hasHeightForWidth())
        self.frame_23.setSizePolicy(sizePolicy)
        self.frame_23.setStyleSheet(u"QFrame#frame_23 {\n"
"    border: 1px solid #000000; /* 1px solid black border for all frames */\n"
"}")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_23)
        self.gridLayout_4.setObjectName(u"gridLayout_4")

        self.verticalLayout_13.addWidget(self.frame_23)

        self.stackedWidget.addWidget(self.percentage_bar_chart)
        self.bar_chart = QWidget()
        self.bar_chart.setObjectName(u"bar_chart")
        self.bar_chart.setStyleSheet(u"QFrame#frame_24 {\n"
"    border: 1px solid #000000; /* 1px solid black border for all frames */\n"
"}\n"
"\n"
"QFrame#frame_25 {\n"
"    border: 1px solid #000000; /* 1px solid black border for all frames */\n"
"}")
        self.verticalLayout_15 = QVBoxLayout(self.bar_chart)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.frame_24 = QFrame(self.bar_chart)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_24)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_13 = QLabel(self.frame_24)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_13, 0, Qt.AlignTop)


        self.verticalLayout_15.addWidget(self.frame_24)

        self.frame_25 = QFrame(self.bar_chart)
        self.frame_25.setObjectName(u"frame_25")
        sizePolicy.setHeightForWidth(self.frame_25.sizePolicy().hasHeightForWidth())
        self.frame_25.setSizePolicy(sizePolicy)
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_25)
        self.gridLayout_5.setObjectName(u"gridLayout_5")

        self.verticalLayout_15.addWidget(self.frame_25)

        self.stackedWidget.addWidget(self.bar_chart)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.verticalLayout_4.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.frame_2)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setStyleSheet(u"")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_2 = QLabel(self.frame_9)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"QFrame {\n"
"    border: 1px solid #000000; /* 1px solid black border for all frames */\n"
"}")

        self.horizontalLayout_8.addWidget(self.label_2)


        self.verticalLayout_4.addWidget(self.frame_9)


        self.horizontalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 819, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"QT CHARTS", None))
        self.percentage_bar_button.setText(QCoreApplication.translate("MainWindow", u"Percentage bar chart", None))
        self.temperature_record_button.setText(QCoreApplication.translate("MainWindow", u"Temperature records", None))
        self.nested_donut_button.setText(QCoreApplication.translate("MainWindow", u"Nested donuts", None))
        self.line_chart_button.setText(QCoreApplication.translate("MainWindow", u"line chart", None))
        self.bar_chart_button.setText(QCoreApplication.translate("MainWindow", u"bar chart", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"MENU", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"DASHBOARD", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"close", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"LINE CHART", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"TEMPERATURE  BAR CHART", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"NESTED DONUT CHART", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"PERCENTAGE BAR CHART", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"BAR CHARTS", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"copyright Bhavya V 1.0", None))
    # retranslateUi

