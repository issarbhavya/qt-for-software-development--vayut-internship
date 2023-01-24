from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow
import sys

class my_window(QMainWindow):
    
    def __init__(self):
        super(my_window,self).__init__()
        self.setGeometry(100,100,300,300)
        self.setWindowTitle("gui from sys")
        self.in_our_gui()
        
    def in_our_gui(self):
        self.label=QtWidgets.QLabel(self)
        self.label.setText("please press the button below :")
        self.update_label()
        self.label.move(50,50)
        
        self.b1=QtWidgets.QPushButton(self)
        self.b1.setText("press me")
        self.b1.move(50,80)
        self.b1.clicked.connect(self.on_clicked)
        
    def on_clicked(self):
        self.label.setText("the below button was pressed")
        self.update_label()
        
    def update_label(self):
        self.label.adjustSize()


def window():
    
    app=QApplication(sys.argv)
    wnd=my_window()
    
    wnd.show()
    sys.exit(app.exec_())
    
window()     