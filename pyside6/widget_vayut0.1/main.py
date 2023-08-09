import os
import sys
from PySide6.QtGui import QStandardItem, QStandardItemModel
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QStatusBar, QTreeView, QVBoxLayout, QWidget)


from frontend_og_ui import *

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


class Widget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self)
        self.ui =Ui_Form()
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



        
if __name__ == "__main__":
    app= QApplication(sys.argv)
    
    window= Widget()
    window.show()
    sys.exit(app.exec_())
    
    
    