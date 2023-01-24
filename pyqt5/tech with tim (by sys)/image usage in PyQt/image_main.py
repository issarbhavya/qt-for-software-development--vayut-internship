from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5 import uic

class MyGUI(QMainWindow):
    
    def __init__(self):
        super(MyGUI,self).__init__()
        uic.loadUi("..\image usage in PyQt\image_in_gui.ui",self)
        self.picture_label.setPixmap(QtGui.QPixmap("cat.jpg"))
        self.show()
        self.cat_button.clicked.connect(self.cat_press)
        self.dog_button.clicked.connect(self.dog_press)

        
    def dog_press(self):
        self.picture_label.setPixmap(QtGui.QPixmap("dog.jpg"))
    
    def cat_press(self):
        self.picture_label.setPixmap(QtGui.QPixmap("cat.jpg"))

        
def main():
    app=QApplication([])
    window=MyGUI()
    window.setWindowTitle("Bhavya's 1st attempt to make GUI")
    app.exec_()
    
    


if __name__=="__main__":
    main()