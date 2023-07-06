import sys
from PySide6 import QtCore
from PySide6.QtCore import Qt,QModelIndex
from PySide6.QtGui import QStandardItem, QStandardItemModel
from PySide6.QtWidgets import QApplication, QMainWindow, QTreeView

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create the model
        self.model = QStandardItemModel()

        # Create the tree view and set the model
        self.tree_view = QTreeView()
        self.tree_view.setModel(self.model)

        # Set up the main window
        self.setWindowTitle("Tree View Example")
        self.setCentralWidget(self.tree_view)

        # Populate the model with data
        self.populate_model()

    def populate_model(self):
        # Create top-level items
        parent1 = QStandardItem("Parent 1")
        parent2 = QStandardItem("Parent 2")

        # Add top-level items to the model
        self.model.appendRow(parent1)
        self.model.appendRow(parent2)

        # Create child items
        child1 = QStandardItem("Child 1")
        child2 = QStandardItem("Child 2")

        # Add child items to the parent items
        parent1.appendRow(child1)
        parent2.appendRow(child2)

# from to do list proj : item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
        child1.setFlags(child1.flags() | QtCore.Qt.ItemIsUserCheckable)
        child2.setFlags(child1.flags() | QtCore.Qt.ItemIsUserCheckable)
        parent1.setFlags(child1.flags() | QtCore.Qt.ItemIsUserCheckable)
        parent2.setFlags(child1.flags() | QtCore.Qt.ItemIsUserCheckable)


        # Set initial check states for the items
        parent1.setCheckState(Qt.Checked)
        parent2.setCheckState(Qt.Checked)
        child1.setCheckState(Qt.Unchecked)
        child2.setCheckState(Qt.Unchecked)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
