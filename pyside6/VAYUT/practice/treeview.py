from PySide6.QtCore import Qt
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtWidgets import QApplication, QTreeView

if __name__ == "__main__":
    app = QApplication([])
    
    # Create a standard item model
    model = QStandardItemModel()
    
    # Set the column headers
    model.setHorizontalHeaderLabels(["Column 1", "Column 2", "Column 3"])
    
    # Create parent items
    parent_item_1 = QStandardItem("r1")
    parent_item_2 = QStandardItem("r2")
    
    # Add the parent items to the model
    model.appendRow(parent_item_1)
    model.appendRow(parent_item_2)
    
    # Set the parent items in column 0
    model.setItem(0, 0, parent_item_1)
    model.setItem(1, 0, parent_item_2)
    
    # Create child items
    child_item_1 = QStandardItem("Child 1")
    child_item_2 = QStandardItem("Child 2")
    child_item_3 = QStandardItem("Child 3")
    
    # Add the child items to the parent items
    # parent_item_1.appendRow([child_item_1, QStandardItem("Data 1"), QStandardItem("Data 2")])
    # parent_item_2.appendRow([child_item_2, QStandardItem("Data 3"), QStandardItem("Data 4")])
    # parent_item_2.appendRow([child_item_3, QStandardItem("Data 5"), QStandardItem("Data 6")])
    
    parent_item_1.appendRow([child_item_1, QStandardItem("Data 1"), QStandardItem("Data 2")])
    parent_item_2.appendRow([child_item_2, QStandardItem("Data 3"), QStandardItem("Data 4")])
    parent_item_2.appendRow([child_item_3, QStandardItem("Data 5"), QStandardItem("Data 6")])
    
    # Create a tree view
    tree_view = QTreeView()
    
    # Set the model for the tree view
    tree_view.setModel(model)
    
    # Expand all items
    tree_view.expandAll()
    
    # Set the column widths to fit the contents
    tree_view.resizeColumnToContents(0)
    tree_view.resizeColumnToContents(1)
    tree_view.resizeColumnToContents(2)
    
    # Show the tree view
    tree_view.show()
    
    app.exec()
