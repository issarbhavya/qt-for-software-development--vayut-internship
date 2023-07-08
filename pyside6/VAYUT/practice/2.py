import sys
import random
from PySide6.QtWidgets import QApplication, QMainWindow, QTreeWidget, QTreeWidgetItem

# Create the application
app = QApplication(sys.argv)

# Create the main window
window = QMainWindow()
window.setWindowTitle("Tree Widget Example")
window.resize(700, 300)

# Create the tree widget
tree_widget = QTreeWidget()
tree_widget.setColumnCount(4)
tree_widget.setHeaderLabels(["Robots", "SBC", "MCU from SBC", "MCU from MCU"]) 

parent_item_robot = QTreeWidgetItem(tree_widget)
parent_item_robot.setText(0, "drone 1")

child_item_sbc_1 = QTreeWidgetItem(parent_item_robot)
child_item_sbc_1.setText(1, "sbc 1")

child_item_mcu_1 = QTreeWidgetItem(child_item_sbc_1)
child_item_mcu_1.setText(2, "mcu 1")

child_item_mcu_2 = QTreeWidgetItem(child_item_sbc_1)
child_item_mcu_2.setText(2, "mcu 2")

child_item_mcu_3 = QTreeWidgetItem(child_item_mcu_2)
child_item_mcu_3.setText(3, "mcu 3")

window.setCentralWidget(tree_widget)

# Show the main window
window.show()

# Start the event loop
sys.exit(app.exec())