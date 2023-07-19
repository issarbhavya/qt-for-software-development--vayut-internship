from typing import Optional
from PySide6.QtWidgets import (
    QTreeWidget, QTreeWidgetItem, QPushButton, QLabel, QDialog,
    QVBoxLayout, QApplication, QLineEdit, QRadioButton,QAbstractButton,QWidget,QHBoxLayout
)
from PySide6.QtCore import Slot
import sys

from custom_widget import populate_treeview

class new_hbox(QWidget):
    
    def __init__(self,text) -> None:
        super(new_hbox, self).__init__()
        
        
        
        
    