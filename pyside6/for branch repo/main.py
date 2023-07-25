import sys
import random
from PySide6.QtWidgets import QApplication, QMainWindow, QTreeWidget, QTreeWidgetItem,QPushButton
from PySide6.QtGui import QStandardItem, QStandardItemModel

from ui_widget import *

from custom_widget import component, create_component_tree

struct = {
        'ROBOT1': {
            "details":{
                "name":{}
            },
            'SBC1': {
                'MCU1': {}
            }
        },
        'ROBOT2': {
            'SBC2': {
                'MCU2': {}
            }
        }
}

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui =Ui_MainWindow()
        # self.ui.resize(700, 300)
        
        self.ui.setupUi(self)
        
        
        self.setup_tree_view()
        
    def setup_tree_view(self):
        # Create the model
        self.model = QStandardItemModel()
        self.ui.treeView.setModel(self.model)
        # self.ui.treeView.setColumnWidth(0,400)


        # Set the header labels for each column
        self.model.setHorizontalHeaderLabels(['System Designer', 'Comms', 'Sensors', 'Actuators'])
        base_comp = component('NYATVA',None,self.model,self.ui.treeView)
        item = QStandardItem()
        self.model.appendRow([item])
        self.ui.treeView.setIndexWidget(item.index(),base_comp)
        # Creating top-level and child items



        # Setting the layout
        self.ui.treeView.expandAll()
        create_component_tree(base_comp,struct)

        self.ui.treeView.setColumnWidth(0,200)



# Create the tree widget

def get_designer():
    
    window= MainWindow()
    return window