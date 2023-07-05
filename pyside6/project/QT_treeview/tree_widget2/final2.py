import sys
import random
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QTreeWidget, QTreeWidgetItem, QPushButton, QVBoxLayout, QWidget

# Create the application
app = QApplication(sys.argv)

# Create the main window
window = QMainWindow()
window.setWindowTitle("Tree Widget Example")
window.resize(700, 500)

# Create a widget to hold the Tree Widget and Button
main_widget = QWidget()
layout = QVBoxLayout(main_widget)

# Create the tree widget
tree_widget = QTreeWidget()
tree_widget.setColumnCount(6)
tree_widget.setHeaderLabels(["ID", "Name", "Batch Number", "Cost", "Order ID", "Delivered"])

# Define company names for each parent item
company_names = {
    "Drone Propeller": ["ABC Corporation", "XYZ Inc."],
    "Motors": ["Motor Co.", "Robo Motors"],
    "GPS Tracker": ["Navigation Systems", "GeoTrack Ltd."],
    "Battery": ["Power Solutions", "Energy Tech"],
    "Camera": ["Vision Imaging", "Lens Tech"]
}

# Add parent items with random data
for index, (parent_name, child_names) in enumerate(company_names.items()):
    # enumerate :iterate over a sequence while also keeping track of an index for each item in the sequence
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

        if index == 1 or index== 4:  # Add subchildren for the 2nd  and 5th parent row
            # Add subchild items with order ID and delivered status
            for i in range(2):
                subchild_item = QTreeWidgetItem(child_item)
                subchild_item.setText(4, str(random.randint(1001, 2000)))  # Order ID
                subchild_item.setText(5, random.choice(["Yes", "No"]))  # Delivered status

# Create a QPushButton
button = QPushButton("display !")

# Optional: Connect a function to the button's clicked signal
def on_button_clicked():
    # Iterate over the top-level items in the tree widget
    top_level_count = tree_widget.topLevelItemCount()
    for i in range(top_level_count):
        top_level_item = tree_widget.topLevelItem(i)
        print("\n")
        print(f"ID: {top_level_item.text(0)}")
        print(f"Parent Name: {top_level_item.text(1)}")
        
        
        # Iterate over the child items of each top-level item
        child_count = top_level_item.childCount()
        print("\n")
        for j in range(child_count):
            child_item = top_level_item.child(j)
            print(f"     Batch Number: {child_item.text(2)}")
            print(f"     Cost: {child_item.text(3)}")
            
            # Iterate over the subchild items of each child item
            subchild_count = child_item.childCount()
            print("\n")
            for k in range(subchild_count):
                subchild_item = child_item.child(k)
                print(f"              Order ID: {subchild_item.text(4)}")
                print(f"              Delivered: {subchild_item.text(5)}")



button.clicked.connect(on_button_clicked)

# Add the Tree Widget and Button to the layout
layout.addWidget(tree_widget)
layout.addWidget(button)

# Set the main widget as the central widget
window.setCentralWidget(main_widget)

# Show the main window
window.show()

# Start the event loop
sys.exit(app.exec())
