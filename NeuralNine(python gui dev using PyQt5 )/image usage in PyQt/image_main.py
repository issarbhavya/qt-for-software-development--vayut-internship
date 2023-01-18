from PyQt5.QtWidgets import *
from PyQt5 import uic

class MyGUI(QMainWindow):
    
    def __init__(self):
        super(MyGUI,self).__init__()
        uic.loadUi("image_in_gui.ui",self)
        self.show()
        
def main():
    app=QApplication([])
    window=MyGUI()
    window.setWindowTitle("Bhavya's 1st attempt to make GUI")
    app.exec_()


if __name__=="__main__":
    main()