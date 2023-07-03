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
tree_widget.setColumnCount(4)
tree_widget.setHeaderLabels(["ID", "Name", "Batch Number", "Cost"])

# Define company names for each parent item
company_names = {
    "Drone Propeller": ["ABC Corporation", "XYZ Inc."],
    "Motors": ["Motor Co.", "Robo Motors"],
    "GPS Tracker": ["Navigation Systems", "GeoTrack Ltd."],
}

# Add parent items with random data
for parent_name, child_names in company_names.items():
    parent_item = QTreeWidgetItem(tree_widget)
    parent_item.setText(0, str(random.randint(1, 100)))  # Random ID
    parent_item.setText(1, parent_name)  # Parent name

    # Add child items with random data for each parent
    for child_name in child_names:
        child_item = QTreeWidgetItem(parent_item)
        child_item.setText(0, str(random.randint(101, 200)))  # Random child ID
        child_item.setText(1, child_name)  # Child name

        batch_number = random.randint(1, 10)
        cost = random.uniform(10.0, 100.0)
        child_item.setText(2, str(batch_number))  # Batch Number
        child_item.setText(3, f"${cost:.2f}")  # Cost

# Set the tree widget as the central widget
window.setCentralWidget(tree_widget)

# Show the main window
window.show()

# Start the event loop
sys.exit(app.exec())
