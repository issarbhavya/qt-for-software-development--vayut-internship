import os
import sys
from PySide6.QtGui import QStandardItem, QStandardItemModel


from ui_widget import *



class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui =Ui_MainWindow()
        # self.ui.resize(700, 300)
        
        self.ui.model =QStandardItemModel()
        self.ui.treeView= QTreeView()
        
        self.ui.treeView.setModel(self.model)
        self.ui.populate_model()

        self.ui.setupUi(self)
        self.populate_model()
        
    def populate_model(self):
        



        self.show()
        
if __name__ == "__main__":
    app= QApplication(sys.argv)
    
    window= MainWindow()
    window.show()
    sys.exit(app.exec_())
    
    
    