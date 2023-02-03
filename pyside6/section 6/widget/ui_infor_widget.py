# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'infor_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QWidget)

class Ui_main_Dialog(object):
    def setupUi(self, main_Dialog):
        if not main_Dialog.objectName():
            main_Dialog.setObjectName(u"main_Dialog")
        main_Dialog.resize(400, 300)
        self.ok_button = QPushButton(main_Dialog)
        self.ok_button.setObjectName(u"ok_button")
        self.ok_button.setGeometry(QRect(30, 110, 75, 23))
        self.close_button = QPushButton(main_Dialog)
        self.close_button.setObjectName(u"close_button")
        self.close_button.setGeometry(QRect(110, 110, 75, 23))
        self.widget = QWidget(main_Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(30, 20, 201, 31))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.occupation_text = QLineEdit(self.widget)
        self.occupation_text.setObjectName(u"occupation_text")

        self.horizontalLayout.addWidget(self.occupation_text)

        self.widget1 = QWidget(main_Dialog)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(30, 60, 201, 22))
        self.horizontalLayout_2 = QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget1)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.combobox_info = QComboBox(self.widget1)
        self.combobox_info.addItem("")
        self.combobox_info.addItem("")
        self.combobox_info.addItem("")
        self.combobox_info.setObjectName(u"combobox_info")

        self.horizontalLayout_2.addWidget(self.combobox_info)


        self.retranslateUi(main_Dialog)

        QMetaObject.connectSlotsByName(main_Dialog)
    # setupUi

    def retranslateUi(self, main_Dialog):
        main_Dialog.setWindowTitle(QCoreApplication.translate("main_Dialog", u"Dialog", None))
        self.ok_button.setText(QCoreApplication.translate("main_Dialog", u"ok", None))
        self.close_button.setText(QCoreApplication.translate("main_Dialog", u"close", None))
        self.label.setText(QCoreApplication.translate("main_Dialog", u"Occupation", None))
        self.label_2.setText(QCoreApplication.translate("main_Dialog", u"fav OS", None))
        self.combobox_info.setItemText(0, QCoreApplication.translate("main_Dialog", u"windows", None))
        self.combobox_info.setItemText(1, QCoreApplication.translate("main_Dialog", u"mac", None))
        self.combobox_info.setItemText(2, QCoreApplication.translate("main_Dialog", u"linux", None))

    # retranslateUi

