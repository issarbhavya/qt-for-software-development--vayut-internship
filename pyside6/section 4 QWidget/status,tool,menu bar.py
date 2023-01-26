from PySide6.QtWidgets import QStatusBar,QToolBar,QApplication,QMainWindow
from PySide6.QtGui import QAction,QIcon
import sys
from rockwidget import Rock_widget

class Main_window(QMainWindow):
    def __init__(self,app):
        super().__init__()
        self.applcn=app 
        menu_bar=self.menuBar()
        #to create menu
        
        #to add file on menu bar
        file_menu = menu_bar.addMenu("&File")
         
        #to add actions inside file
        to_close=file_menu.addAction("close")
        to_close.triggered.connect(self.quit_func)
        
        edit_menu=menu_bar.addMenu("&edit")
        edit_menu.addAction("cut")
        edit_menu.addAction("copy")
        
        toolbar= QToolBar("my toolbar")
        self.addToolBar(toolbar)
        toolbar.addAction(to_close)#here we put the varibale which 
        #when triggered, calls the quit_func
        
        #creating an action for toolbar
        action1=QAction("action 1",self)
        action1.triggered.connect(self.give_some_action)
        
        #adding action to toolbar
        toolbar.addAction(action1)
        
        
        #adding status bar
        self.setStatusBar(QStatusBar(self))
        
        

        
    def quit_func(self):
        self.applcn.quit()
        
    def give_some_action(self):
        #on clicking we can give updates in statusbar
        self.statusBar().showMessage("done")

        print("pressed")
        
    
appl=QApplication(sys.argv)
window=Main_window(appl)
window.setGeometry(100,100,500,300)

window.show()
appl.exec() 