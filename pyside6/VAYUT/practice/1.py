import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtWidgets import QApplication, QMainWindow, QTreeView


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.tree_view = QTreeView()
        self.setCentralWidget(self.tree_view)

        self.setup_tree_view()

    def setup_tree_view(self):
        # Create the model
        model = QStandardItemModel()
        self.tree_view.setModel(model)

        # Set the header labels for each column
        model.setHorizontalHeaderLabels(['Robot Name', 'SBC', 'MCU', 'Sub-MCU'])

        # Create the root item
        root_item = QStandardItem('Naytva')
        model.appendRow(root_item)

        # Create the parent item (Robots)
        parent_item = QStandardItem('Robots')
        root_item.appendRow(parent_item)

        # Create the child items (SBC)
        sbc_item = QStandardItem('SBC')
        parent_item.appendRow(sbc_item)

        # Create the grandchild items (MCU)
        mcu_item = QStandardItem('MCU')
        sbc_item.appendRow(mcu_item)

        # Create the sub-grandchild items (Sub-MCU)
        sub_mcu_item = QStandardItem('Sub-MCU')
        mcu_item.appendRow(sub_mcu_item)

        # Expand the root item and parent items
        self.tree_view.expandAll()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
