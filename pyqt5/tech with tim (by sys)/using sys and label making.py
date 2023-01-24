from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow
#instead of qmainwindow we can also use qwidget

import sys

def clicked1():
    print("button has been pressed")


def window1():
    
    app=QApplication(sys.argv)
    wnd=QMainWindow()
    wnd.setGeometry(200,100,300,300)
    wnd.setWindowTitle("gui from sys")
    
    label=QtWidgets.QLabel(wnd)
    label.setText("made gui using sys")
    label.move(200,90)
    
    b1=QtWidgets.QPushButton(wnd)
    b1.setText("press me ")
    b1.move(50,50)
    b1.clicked.connect(clicked1)
    
    
    wnd.show()
    sys.exit(app.exec_())
    
window1()     