import os
import sys
from PySide6.QtGui import QStandardItem, QStandardItemModel


from ui_widget import *

from custombuttonStack import label_plus_button

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui =Ui_MainWindow()
        # self.ui.resize(700, 300)
        
        # self.ui.model =QStandardItemModel()
        # self.ui.treeView= QTreeView()
        
        # self.ui.treeView.setModel(self.ui.model)

        self.ui.setupUi(self)
        
        
        self.setup_tree_view()
        
    def setup_tree_view(self):
        # Create the model
        self.model = QStandardItemModel()
        self.ui.treeView.setModel(self.model)

        # Set the header labels for each column
        self.model.setHorizontalHeaderLabels(['System Designer', 'Comms', 'Sensors', 'Actuators'])
        
        
        # #############
        self.topLevelItem = QStandardItem()
        self.root_element= label_plus_button("NYATVA")

        self.model.appendRow([self.topLevelItem])


        # Create the root item (Robots)
        parent_item = QStandardItem('Robots')
        self.model.appendRow(parent_item)

        # Create the child items (SBC)
        sbc_item = QStandardItem('SBC')
        parent_item.appendRow(sbc_item)

        # Create the grandchild items (MCU)
        mcu_item = QStandardItem('MCU')
        sbc_item.appendRow(mcu_item)

        # Create the sub-grandchild items (Sub-MCU)
        sub_mcu_item = QStandardItem('Sub-MCU')
        mcu_item.appendRow(sub_mcu_item)
        
        self.ui.treeView.setColumnWidth(0,200)

        # Expand the root item and parent items
        self.ui.treeView.expandAll()
        



        self.show()
        
if __name__ == "__main__":
    app= QApplication(sys.argv)
    
    window= MainWindow()
    window.show()
    sys.exit(app.exec_())
    
    
    