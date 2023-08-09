
from typing import Optional
from PySide6.QtWidgets import (
    QTreeWidget, QTreeWidgetItem, QPushButton, QLabel, QDialog,
    QVBoxLayout, QApplication, QLineEdit, QRadioButton,QAbstractButton,QWidget,QHBoxLayout
)
from PySide6.QtCore import Slot
import sys


class label_plus_button(QWidget):
    
    def __init__(self,text) -> None:
        super(label_plus_button, self).__init__()
        self.custom_layout= QHBoxLayout()
        self.add_button= QPushButton("+")
        self.add_button.setFixedSize(20, 20)
        self.button_name_text=str(text)+str("_button")
        self.add_button.setObjectName(self.button_name_text)
        self.label_added=QLabel(text)
        self.label_added.setStyleSheet("border: 2px solid grey;")
        self.custom_layout.addWidget(self.add_button)
        self.custom_layout.addWidget(self.label_added)
        self.setLayout(self.custom_layout)
        self.return_function()
        
        #self.button_name_text.clicked.connect(self.add_button_clicked)

    def add_button_clicked(self):
        pass



    def return_function(self):
        print("\n\n\nyou reached here ")
        return self

