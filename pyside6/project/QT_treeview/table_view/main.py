import sys
import random
from PySide6 import QtCore
from PySide6.QtCore import Qt
from PySide6.QtGui import QStandardItem, QStandardItemModel
from PySide6.QtWidgets import QApplication, QMainWindow, QTableView

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create the model
        self.model = QStandardItemModel(4,4)

        # Create the tree view and set the model
        self.table_view = QTableView()
        self.table_view.setModel(self.model)

        # Set up the main window
        self.setWindowTitle("Tree View Example")
        self.setCentralWidget(self.table_view)

        self.resize(500,500)

        # Populate the model with data
        self.populate_model()

    def populate_model(self):
        # Create top-level items
        for r in range(self.model.rowCount()):
            for c in range(self.model.columnCount()):
                item= QStandardItem(str(random.randint(0,100)))
                item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)

                self.model.setItem(r,c,item)

        # # Add top-level items to the model
        # self.model.appendRow(parent1)
        # self.model.appendRow(parent2)

      

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())



