import sys
import random
from PySide6 import QtCore
from PySide6.QtCore import Qt, QModelIndex
from PySide6.QtGui import QStandardItem, QStandardItemModel
from PySide6.QtWidgets import QWidget, QApplication, QMainWindow, QTableView, QPushButton, QVBoxLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Create the model
        self.model = QStandardItemModel(4, 4)

        # Create the table view and set the model
        self.table_view = QTableView()
        self.table_view.setModel(self.model)

        # Set up the main window
        self.setWindowTitle("Tree View Example")
        self.setCentralWidget(self.table_view)

        self.resize(500, 500)

        # Create a layout for the main window
        layout = QVBoxLayout()
        layout.addWidget(self.table_view)

        # Create a QPushButton
        self.button = QPushButton("Display!")

        # Add the button to the layout
        layout.addWidget(self.button)

        # Create a widget to hold the layout
        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the main window
        self.setCentralWidget(widget)

        self.button.clicked.connect(self.display)
        self.populate_model()
        
    def populate_model(self):
        # Create top-level items
        for r in range(self.model.rowCount()):
            for c in range(self.model.columnCount()):
                item = QStandardItem(str(random.randint(0, 100)))
                item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)

                self.model.setItem(r, c, item)

    def display(self):
        for r in range(self.model.rowCount()):
            for c in range(self.model.columnCount()):
                print(self.model.data(self.model.index(r, c), Qt.DisplayRole))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
