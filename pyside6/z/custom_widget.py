from typing import Optional
from PySide6.QtWidgets import (
    QTreeWidget, QTreeWidgetItem, QPushButton, QLabel, QDialog,
    QVBoxLayout, QApplication, QLineEdit, QRadioButton,QAbstractButton,QWidget,QHBoxLayout
)
from PySide6.QtCore import Slot
import sys

class populate_treeview(QWidget):
    
    dict_data={}
    
    def __init__(self,text) -> None:
        super(populate_treeview, self).__init__()
        self.custom_layout= QHBoxLayout()
        
        