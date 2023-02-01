from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget
from ui_login_password import Ui_Form

class Widget(QWidget,Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("uic converted")
        self.pushButton.clicked.connect(self.button_was_pressed)
            
    def button_was_pressed (self):
        print ("The entered login id is",self.lineEdit.text(),"and the password is",self.lineEdit_2.text())
        if(self.lineEdit.text()=="bi" and self.lineEdit_2.text()=="1234"):
            self.textEdit.setEnabled(True)
            self.pushButton_2.setEnabled(True)
            self.label_3.setText("")
            
        