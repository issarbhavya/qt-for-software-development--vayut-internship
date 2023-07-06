from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget,QTreeWidgetItem
from ui_widget import Ui_Widget

class Widget(QWidget,Ui_Widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("uic converted")
        
        self.treeWidget.setColumnCount(2)
        
        # setting header data names
        self.treeWidget.setHeaderLabels( ["id","name"] )
        
        # adding data 
        treeitem1=QTreeWidgetItem(self.treeWidget)
        treeitem1.setText(0,"bhavya")
        treeitem1.setText(1,"issar")
        
        treeitem2=QTreeWidgetItem(self.treeWidget)
        treeitem2.setText(0,"hello")
        treeitem2.setText(1,"rusha")
        
        # this is a floating item
        treeitem3=QTreeWidgetItem()
        treeitem3.setText(0,"whats up")
        treeitem3.setText(1,"my girl")
       
        #now we will add the floating item as a child of the parent tree widget 
        treeitem2.addChild(treeitem3)
        
        
        self.display_button.clicked.connect(self.display_button_pressed)

    
    def display_button_pressed(self):
        top_level_item_count=self.treeWidget.topLevelItemCount()
        for i in range(top_level_item_count):
            item=self.treeWidget.topLevelItem(i)
            if(item):
                print("id : ",item.data(0,Qt.DisplayRole), "| name : ",item.data(1,Qt.DisplayRole))
                child_count=item.childCount()
                if(not(child_count==0)):
                    for j in range(child_count):
                        child=item.child(j)
                        print("---id : ",child.data(0,Qt.DisplayRole), "| name : ",child.data(1,Qt.DisplayRole))


        
        