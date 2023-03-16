from PySide6 import QtCore
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget,QListWidget,QListWidgetItem,QMessageBox
from ui_widget import Ui_Widget

import sqlite3



class Widget(QWidget,Ui_Widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Daily Task Planner")
        
        #self.db = sqlite3.connect("task.db.sqlite3")

        self.calendarWidget.selectionChanged.connect(self.calender_date_changed)
        
        self.calender_date_changed()
        
        self.save_changes_button.clicked.connect(self.save_changes_button_was_clicked)
        self.add_new_button.clicked.connect(self.add_button_was_clicked)
        self.save_new_button.clicked.connect(self.save_new_button_was_clicked)
                           
    def calender_date_changed(self):
        print("date changed")
        self.date_selected=self.calendarWidget.selectedDate()
        self.date_selected=self.date_selected.toPython()
        print(self.date_selected)
        self.update_task_list(self.date_selected)
        
 
        
    def update_task_list(self,date):
        
        self.tasklistWidget.clear()  
        
        # we need to connect to the database,only then we can query the data      
        db = sqlite3.connect("task.db.sqlite3")
        
        # creating cursor to query the database
        cursor= db.cursor()
        
        #creating the query 
        query="SELECT task,completed FROM Tasks WHERE date = ?"
        
        #to store date, row is used to get query
        row=(date,)
        
        
        self.results= cursor.execute(query,row).fetchall()

        # since there can be more than one task for a particular date,
        # so a for loop is required to access all
        for self.res in self.results:
            
            # the res here contains the data in tuple form, containing
            # "task" and "completed" at index 0 nd 1 respectively     
            item=QListWidgetItem(  str( self.res[0]) )
            
            
            item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
                    # flags are like properties, in the above line i have changed the properties by set property to :
                    # 1. the previous prop and   2.items must be user checkable 
                    
            if(self.res[1]=="YES"):          
                item.setCheckState(QtCore.Qt.Checked)
            
            if(self.res[1]=="NO"): 
                item.setCheckState(QtCore.Qt.Unchecked)  
                
                    
            self.tasklistWidget.addItem(item)
        
        db.close()
            
            
    def save_changes_button_was_clicked(self):
        print("Saving Changes...")
        db = sqlite3.connect("task.db.sqlite3", timeout=10)
        cursor= db.cursor()
        
        self.date_selected=self.calendarWidget.selectedDate()
        self.date_selected=self.date_selected.toPython()
        
        for i in range(self.tasklistWidget.count()):
            
            item= self.tasklistWidget.item(i)
            task=item.text()
            #print(f"task is : {task}")
            if( item.checkState()==QtCore.Qt.Checked):
                #print(f"at index {i} , item is checked")
                query="UPDATE Tasks SET completed = 'YES' WHERE task=? AND date=?"
            
            else:
                #print(f"at index {i} , item is unchecked")
                query="UPDATE Tasks SET completed = 'NO' WHERE task=? AND date=?"
                
            row=(task,self.date_selected,)
            #print(row)
            cursor.execute(query,row)
        
        db.commit()
        #as we are making some changes to the database thus we need to commit the data
        
        db.close()
        print('Saved.')
        
        # message prompt
        message_box=QMessageBox()
        message_box.setText("your changes are saved")
        message_box.setStandardButtons(QMessageBox.Ok)
        message_box.exec_()

    
    def add_button_was_clicked(self):
        
        # for app looks
        self.new_task_lineEdit.setEnabled(True)
        self.add_new_task_label.setEnabled(True)

        self.new_task_lineEdit.clear()
        
        self.new_task_lineEdit.setFocus()

        
    def save_new_button_was_clicked(self):
        
        db = sqlite3.connect("task.db.sqlite3", timeout=10)
        cursor= db.cursor()
        
        self.date_selected=self.calendarWidget.selectedDate()
        self.date_selected=self.date_selected.toPython()
        
        new_task=str(self.new_task_lineEdit.text())
        if(new_task==""):
            new_task="default text"
        
        query="INSERT INTO Tasks(task,completed,date) VALUES (?,?,?)"
        row=(new_task,"NO",self.date_selected)
        
        cursor.execute(query,row)
        db.commit()
        db.close()
        
        self.new_task_lineEdit.setText("default text")

        self.new_task_lineEdit.setEnabled(False)
        self.add_new_task_label.setEnabled(False)
        
        #for instantly updating the tasklist
        self.update_task_list(self.date_selected)
        
        # # message prompt
        # message_box=QMessageBox()
        # message_box.setText(f"new task : '{new_task}' \nIs added to the date :{self.date_selected}")
        # message_box.setStandardButtons(QMessageBox.Ok)
        # message_box.exec_()
            
            
        
        
            
        
        
        
        
        
        