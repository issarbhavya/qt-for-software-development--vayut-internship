import sys
import random
from PySide6.QtWidgets import QApplication, QMainWindow, QTreeWidget, QTreeWidgetItem

# Create the application
app = QApplication(sys.argv)

# Create the main window
window = QMainWindow()
window.setWindowTitle("Tree Widget Example")
window.resize(400, 300)

# Create the tree widget
tree_widget = QTreeWidget()
tree_widget.setColumnCount(2)
tree_widget.setHeaderLabels(["ID", "Name"])

# Add three rows with random data
for i in range(3):
    item = QTreeWidgetItem(tree_widget)
    item.setText(0, str(random.randint(1, 100)))  # Random ID
    item.setText(1, f"Item {i+1}")  # Random name

    if i == 0 or i == 2:  # Add child items to first and last rows
        for j in range(2):
            child_item = QTreeWidgetItem(item)
            child_item.setText(0, str(random.randint(101, 200)))  # Random child ID
            child_item.setText(1, f"Child {j+1}")  # Random child name

# Set the tree widget as the central widget
window.setCentralWidget(tree_widget)

# Show the main window
window.show()

# Start the event loop
sys.exit(app.exec())
