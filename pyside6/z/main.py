import os
import sys
from PySide6.QtGui import QStandardItem, QStandardItemModel


from ui_widget import *

from custom_widget import populate_treeview

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
        # self.ui.treeView.setColumnWidth(400,400)


        # Set the header labels for each column
        self.model.setHorizontalHeaderLabels(['System Designer', 'Comms', 'Sensors', 'Actuators'])
       
        
        # Creating top-level and child items
        self.topLevelItem = QStandardItem()

        self.custom_widget = populate_treeview("NYATVA")

        self.model.appendRow([self.topLevelItem])

        self.ui.treeView.setIndexWidget(self.topLevelItem.index(), self.custom_widget)



        # Setting the layout
        self.ui.treeView.expandAll()
        



        self.show()
        
if __name__ == "__main__":
    app= QApplication(sys.argv)
    
    window= MainWindow()
    window.show()
    sys.exit(app.exec_())
    
    
    