from typing import Optional
from PySide6.QtWidgets import (
    QTreeWidget, QTreeWidgetItem, QPushButton, QLabel, QDialog,
    QVBoxLayout, QApplication, QLineEdit, QRadioButton,QAbstractButton,QWidget,QHBoxLayout,
    QTreeView
)
from PySide6.QtCore import Slot
import sys
from PySide6.QtGui import QStandardItem, QStandardItemModel


#A dialog box with two text inputs and a button
class Dialog(QDialog):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)
        self.setWindowTitle("Add Component")
        self.resize(300, 100)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Name")
        self.layout.addWidget(self.name_input)
        self.button = QPushButton("Add")
        self.layout.addWidget(self.button)
        self.button.clicked.connect(self.accept)
        

    def get_details(self):
        return self.name_input.text()
    


class component(QWidget):
    
    dict_data={}
    
    def __init__(self,name,PARENT,MODEL_ITEM:QStandardItem,TREE:QTreeView) -> None:
        super(component, self).__init__()
        self.custom_layout= QHBoxLayout()
        self.add_button= QPushButton("+")
        self.add_button.clicked.connect(lambda: self.add_component())
        self.add_button.setFixedSize(20, 20)
        self.label_added=QLabel(name)
        self.label_added.setStyleSheet("border: 2px solid grey;")
        self.custom_layout.addWidget(self.add_button)
        self.custom_layout.addWidget(self.label_added)
        self.setLayout(self.custom_layout)
        self.return_function()
        self.MODEL_ITEM = MODEL_ITEM
        self.PARENT = PARENT
        self.TREE = TREE
        self.CHILDREN = {}

    def add_child(self, name,item,widget):
        if name in self.CHILDREN:
            raise Exception("Child already exists")
        self.CHILDREN[name] = {
            "item": item,
            "widget": widget
        }


    def add_component(self,details=None):
        print("you reached here")
        if details is None:
            dialog = Dialog(self)
            dialog.show()
            dialog.exec()
            name = dialog.get_details()
        else:
            name = details['name']
        ITEM = QStandardItem()
        custom_widget = component(name,self,ITEM,self.TREE)
        self.MODEL_ITEM.appendRow([ITEM])
        self.TREE.setIndexWidget(ITEM.index(), custom_widget)
        self.add_child(name, ITEM, custom_widget)
        # self.TREE.expandAll()
        return custom_widget

    def return_function(self):
        print("\n\n\nyou reached here ")
        return self

        
def create_component_tree(BASE,STRUCTURE:dict):
    for key in STRUCTURE:
        comp = BASE.add_component({'name':key})
        create_component_tree(comp,STRUCTURE[key])
