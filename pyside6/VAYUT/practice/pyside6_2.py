from PySide6.QtWidgets import (
    QTreeWidget, QTreeWidgetItem, QPushButton, QLabel, QDialog,
    QVBoxLayout, QApplication, QLineEdit, QRadioButton,QWidget,QTreeView
)
from PySide6.QtWidgets import QWidget
from custombuttonStack import helloworldButton
from PySide6.QtCore import Slot
import sys

class TreeWidgetWithWidgetItems(QDialog):
    def __init__(self):
        super(TreeWidgetWithWidgetItems, self).__init__()
        self.init_ui()

    def init_ui(self):
        # Creating the required widgets
        self.vboxLayout = QVBoxLayout()
        self.treeWidget = QTreeWidget()

        self.custom_widget=QWidget()


        self.label = QLabel("I'm going to inform you about the buttons")

        # Adding the widgets to the layout
        self.vboxLayout.addWidget(self.treeWidget)
        self.vboxLayout.addWidget(self.label)

        # Setting up the QTreeWidget
        self.treeWidget.setHeaderLabel("TreeWidget with Buttons")
        self.treeWidget.setColumnCount(1)  # Set the column count to 1
        self.topLevelItem = QTreeWidgetItem()

        # Creating top-level and child widgets
        self.topLevelButton = QPushButton("Top Level Button")
        self.childButton_1 = QPushButton("Child 1")
        self.childButton_2 = QPushButton("Child 2")
        self.custom_widget = helloworldButton("suresh")
        self.childLineEdit = QLineEdit()
        self.childLineEdit.setPlaceholderText("Add Text Here")

        # Adding child items to the top level item
        self.childItems = []
        for i in range(4):
            self.childItems.append(QTreeWidgetItem())
            print("\n\n\ni is :", i)
            self.topLevelItem.addChild(self.childItems[i])
            print("/n childitems[i] is", self.childItems[i] )
        


        # Adding widgets to the QTreeWidget
        self.treeWidget.addTopLevelItem(self.topLevelItem)
        self.treeWidget.setItemWidget(self.childItems[0], 0, self.childButton_1)
        self.treeWidget.setItemWidget(self.childItems[1], 0, self.childButton_2)
        self.treeWidget.setItemWidget(self.childItems[3], 0, self.childLineEdit)
        self.treeWidget.setItemWidget(self.childItems[2], 0, self.custom_widget)


        # Connecting the widgets with corresponding slots
        self.topLevelButton.clicked.connect(self.top_button_clicked)
        self.childButton_1.clicked.connect(self.child_button_1_clicked)
        self.childButton_2.clicked.connect(self.child_button_2_clicked)
        self.childLineEdit.textEdited.connect(self.child_lineedit_edited)

        # Setting the layout
        self.setWindowTitle("QTreeWidget with Button Example")
        self.setLayout(self.vboxLayout)

    @Slot()
    def top_button_clicked(self):
        self.label.setText("Top Level Button was Clicked")

    @Slot()
    def child_button_1_clicked(self):
        self.label.setText("Child button 1 was clicked")
        radio_button = QRadioButton("Radio Button")
        # self.childButton_1.addChild(radio_button)
        self.treeWidget.setItemWidget(self.childItems[0], 1, radio_button)

    @Slot()
    def child_button_2_clicked(self):
        self.label.setText("Child button 2 was clicked")

    @Slot(str)
    def child_lineedit_edited(self, edited_text):
        self.label.setText(str(edited_text))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    treeWidgetDialog = TreeWidgetWithWidgetItems()
    treeWidgetDialog.show()
    sys.exit(app.exec())
