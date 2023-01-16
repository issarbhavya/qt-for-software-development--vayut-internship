from PyQt5.QtWidgets import *
from PyQt5 import uic

class MyGUI(QMainWindow):
    
    def __init__(self):
        super(MyGUI,self).__init__()
        uic.loadUi("new_gui.ui",self)
        self.show()
        
        self.pushbutton1.clicked.connect(self.login)
        self.button_for_printing.clicked.connect(lambda: self.print_it(self.text_message_to_print.toPlainText()))
        
    def print_it(self,msg):
        message=QMessageBox()
        message.move(700,500)
        message.setText(msg)
        message.exec_()
        
        
    def login(self):
        if(self.login_id_entered.text()== "bhavya issar" and self.password_entered.text()== "1234"):
            self.button_for_printing.setEnabled(True)
            self.text_message_to_print.setEnabled(True)
        else:
            message=QMessageBox()
            message.setText("wrong credentials !!")
            message.exec_()


def main():
    app=QApplication([])
    window=MyGUI()
    window.setWindowTitle("Bhavya's 1st attempt to make GUI")
    app.exec_()


if __name__=="__main__":
    main()