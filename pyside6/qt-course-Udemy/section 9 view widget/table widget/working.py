from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget,QTableWidgetItem
from ui_widget import Ui_Widget

class Widget(QWidget,Ui_Widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("uic converted")
        
        self.display_button.clicked.connect(self.display_button_pressed)
        self.add_button.clicked.connect(self.add_button_pressed)
        
    def display_button_pressed(self):
        rows=self.tableWidget.rowCount()
        coloumn=self.tableWidget.columnCount()
        
        for i in range(rows):
            for j in range(coloumn):
                item=self.tableWidget.item(i,j)
                if(item):
                    data=item.data(Qt.DisplayRole)
                    print(data)
                else:
                    print("no data avaliable")

        
    def add_button_pressed(self):
        
        self.tableWidget.insertRow(self.tableWidget.rowCount())
        self.tableWidget.insertColumn(self.tableWidget.columnCount())
        # now as the table is expanded to add item, we are gonna add the item 
        
        item= QTableWidgetItem("hello")
        self.tableWidget.setItem(self.tableWidget.rowCount()-1,self.tableWidget.columnCount()-1,item)

        
