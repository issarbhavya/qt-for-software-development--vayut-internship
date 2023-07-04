from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget,QListWidgetItem
from ui_widget import Ui_Form

class Widget(QWidget,Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("uic converted")
        
        self.display_button.clicked.connect(self.display_button_pressed)
        self.add_button.clicked.connect(self.add_button_pressed)
            
    def display_button_pressed(self):
        for i in range(self.listWidget.count()):
            
            item=self.listWidget.item(i)
            print("item is", item)
            
            data=item.data(Qt.DisplayRole)
            print(data)
       
    def add_button_pressed(self):
        self.listWidget.addItem(QListWidgetItem("hello"))
