from PySide6.QtWidgets import (
    QTreeView, QAbstractItemView, QPushButton, QLabel, QDialog,
    QVBoxLayout, QApplication, QLineEdit, QRadioButton, QWidget, QStyledItemDelegate
)
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import Qt
import sys
from custombuttonStack import label_plus_button


class TreeViewWithWidgetItems(QDialog):
    def __init__(self):
        super(TreeViewWithWidgetItems, self).__init__()
        self.init_ui()

    def init_ui(self):
        # Creating the required widgets
        self.vboxLayout = QVBoxLayout()
        self.treeView = QTreeView()

        self.custom_widget = QWidget()

        self.label = QLabel("I'm going to inform you about the buttons")

        # Adding the widgets to the layout
        self.vboxLayout.addWidget(self.treeView)
        self.vboxLayout.addWidget(self.label)

        # # Setting up the QTreeView
        self.treeView.setHeaderHidden(True)
        # self.treeView.setSelectionMode(QAbstractItemView.NoSelection)
        # self.treeView.setIndentation(20)

        # Creating the model
        self.model = QStandardItemModel()
        self.treeView.setModel(self.model)

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
        self.custom_widget = label_plus_button("suresh")
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
        subchildWidget = label_plus_button("suresh")

        # Adding items to the model
        self.model.appendRow([self.topLevelItem])

        # Setting delegates for specific columns
        delegate = QStyledItemDelegate(self.treeView)
        self.treeView.setItemDelegate(delegate)

        # Setting widgets as editors for specific items
        self.treeView.setIndexWidget(self.childItem1.index(), self.childButton1)
        self.treeView.setIndexWidget(self.childItem2.index(), self.childButton2)
        self.treeView.setIndexWidget(self.childItem4.index(), self.custom_widget)
        self.treeView.setIndexWidget(self.childItem3.index(), self.childLineEdit)
        self.treeView.setIndexWidget(subchildItem.index(), subchildWidget)


        # Setting the layout
        self.setWindowTitle("QTreeView with Button Example")
        self.setLayout(self.vboxLayout)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    treeViewDialog = TreeViewWithWidgetItems()
    treeViewDialog.show()
    sys.exit(app.exec())
