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
       
        
        # Creating top-level and child items
        self.topLevelItem = QStandardItem("Top Level Item")
        self.childItem1 = QStandardItem("Child 1")
        self.childItem2 = QStandardItem()
        self.childItem3 = QStandardItem()
        self.childItem4 = QStandardItem()

        # Creating buttons and line edit
        self.topLevelButton = QPushButton("Top Level Button")
        self.childButton1 = QPushButton("Child Button 1")
        self.childButton2 = QPushButton("Child Button 2")
        self.custom_widget = label_plus_button("SBC")
        self.childLineEdit = QLineEdit()
        self.childLineEdit.setPlaceholderText("Add Text Here")

        # Adding child items to the top level item
        self.topLevelItem.appendRow([self.childItem1])
        self.topLevelItem.appendRow([self.childItem2])
        self.topLevelItem.appendRow([self.childItem4])
        self.topLevelItem.appendRow([self.childItem3])
        
        # Adding subchild item to childItem3
        subchildItem = QStandardItem()
        self.childItem3.appendRow([subchildItem])

        # Creating the custom widget for subchild item
        subchildWidget = label_plus_button("mcu")

        # Adding items to the model
        self.model.appendRow([self.topLevelItem])

        # # Setting delegates for specific columns
        # delegate = QStyledItemDelegate(self.treeView)
        # self.treeView.setItemDelegate(delegate)

        # Setting widgets as editors for specific items
        self.ui.treeView.setIndexWidget(self.childItem1.index(), self.childButton1)
        self.ui.treeView.setIndexWidget(self.childItem2.index(), self.childButton2)
        self.ui.treeView.setIndexWidget(self.childItem4.index(), self.custom_widget)
        self.ui.treeView.setIndexWidget(self.childItem3.index(), self.childLineEdit)
        self.ui.treeView.setIndexWidget(subchildItem.index(), subchildWidget)


        # Setting the layout
        self.ui.treeView.expandAll()
        



        self.show()
        
if __name__ == "__main__":
    app= QApplication(sys.argv)
    
    window= MainWindow()
    window.show()
    sys.exit(app.exec_())
    
    
    