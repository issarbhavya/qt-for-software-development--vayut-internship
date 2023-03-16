# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget.ui'
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
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(732, 438)
        self.calendarWidget = QCalendarWidget(Widget)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setGeometry(QRect(10, 110, 411, 301))
        self.calendarWidget.setStyleSheet(u"font: 12pt;\n"
"")
        self.tasklistWidget = QListWidget(Widget)
        self.tasklistWidget.setObjectName(u"tasklistWidget")
        self.tasklistWidget.setGeometry(QRect(435, 167, 291, 221))
        self.tasklistWidget.setStyleSheet(u"font: 12pt;")
        self.save_changes_button = QPushButton(Widget)
        self.save_changes_button.setObjectName(u"save_changes_button")
        self.save_changes_button.setGeometry(QRect(450, 390, 271, 23))
        self.save_changes_button.setStyleSheet(u"font-size: 11pt;\n"
"background: #01bfff;\n"
"color:white;\n"
"border-radius:10px;")
        self.add_new_button = QPushButton(Widget)
        self.add_new_button.setObjectName(u"add_new_button")
        self.add_new_button.setGeometry(QRect(550, 110, 81, 20))
        self.add_new_button.setStyleSheet(u"font-size: 11pt;\n"
"background: #01bfff;\n"
"color:white;\n"
"border-radius:10px;")
        self.label = QLabel(Widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 731, 101))
        self.label.setStyleSheet(u"font-size: 24pt;\n"
"background: #01bfff;\n"
"color:white;\n"
"border-radius:8px;")
        self.label.setAlignment(Qt.AlignCenter)
        self.new_task_lineEdit = QLineEdit(Widget)
        self.new_task_lineEdit.setObjectName(u"new_task_lineEdit")
        self.new_task_lineEdit.setEnabled(False)
        self.new_task_lineEdit.setGeometry(QRect(532, 140, 191, 20))
        self.add_new_task_label = QLabel(Widget)
        self.add_new_task_label.setObjectName(u"add_new_task_label")
        self.add_new_task_label.setEnabled(False)
        self.add_new_task_label.setGeometry(QRect(440, 140, 91, 20))
        self.add_new_task_label.setStyleSheet(u"font:7pt;\n"
"")
        self.save_new_button = QPushButton(Widget)
        self.save_new_button.setObjectName(u"save_new_button")
        self.save_new_button.setGeometry(QRect(640, 110, 75, 21))
        self.save_new_button.setStyleSheet(u"font-size: 11pt;\n"
"background: #01bfff;\n"
"color:white;\n"
"border-radius:10px;")

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Form", None))
        self.save_changes_button.setText(QCoreApplication.translate("Widget", u"save changes", None))
        self.add_new_button.setText(QCoreApplication.translate("Widget", u"add new", None))
        self.label.setText(QCoreApplication.translate("Widget", u"DAILY TASK PLANNER", None))
        self.new_task_lineEdit.setText(QCoreApplication.translate("Widget", u"deafult text", None))
        self.add_new_task_label.setText(QCoreApplication.translate("Widget", u"add new task here : ", None))
        self.save_new_button.setText(QCoreApplication.translate("Widget", u"save new", None))
    # retranslateUi

