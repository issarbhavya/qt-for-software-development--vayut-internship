from PySide6.QtGui import  QStandardItem, QStandardItemModel
from PySide6.QtWidgets import QTreeView, QPushButton, QVBoxLayout, QWidget
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Qt


# Custom Widget
class CustomWidget(QWidget):
    def __init__(self, text):
        super().__init__()

        # Create a layout for the custom widget
        layout = QVBoxLayout(self)

        # Create a button
        button = QPushButton("Click me!")

        # Add the button to the layout
        layout.addWidget(button)

        # Set the layout for the custom widget
        self.setLayout(layout)

        # # Set the text for the custom widget
        # self.setText(text)

# Create the application
app = QApplication([])

# Create the main window
window = QMainWindow()

# Create the tree view
treeView = QTreeView(window)

# Create the item model
model = QStandardItemModel()

# Create custom items
customItem1 = QStandardItem()
customItem2 = QStandardItem()

# Create custom widgets
customWidget1 = CustomWidget("Item 1")
customWidget2 = CustomWidget("Item 2")

# Set the custom widgets as the data for the custom items
customItem1.setData(customWidget1, role=Qt.DisplayRole)
customItem2.setData(customWidget2, role=Qt.DisplayRole)

# Add custom items to the model
model.appendRow(customItem1)
model.appendRow(customItem2)

# Set the model on the tree view
treeView.setModel(model)

# Show the main window
window.setCentralWidget(treeView)
window.show()

# Start the application event loop
app.exec()
