from PyQt5.QtWidgets import *
from PyQt5 import uic

class MyGUI(QMainWindow):
    
    def __init__(self):
        super(MyGUI,self).__init__()
        uic.loadUi("login id and passsword gui.ui",self)
        self.show()
        
        self.pushbutton1.clicked.connect(self.login)
        self.button_for_printing.clicked.connect(lambda: self.print_it(self.text_message.toPlainText()))
        self.actionclose.triggered.connect(exit)
        self.actionsave.triggered.connect(lambda: self.change_text("you pressed save"))
            #we can use the same line for different shortcuts as well to pass the
            # information that the particular shortcut was triggered by just 
            # changng the word "save" with "new" ,"close", etc
            
        self.default_message_box.clicked.connect(self.message_box_learning)
     
    #the following is to print the text written in "text edit" in a message box    
    def print_it(self,msg):
        message=QMessageBox()
        message.move(700,500)
        message.setText(msg)
        message.exec_()
        
        
    #this is to learn regarding message box
    def message_box_learning(self):
        message=QMessageBox()
        message.setText("my deafult message box")
        #gonna add icons
        message.setIcon(QMessageBox.Information)
                 #other icons avaliable are : Critical,Question,Information and Warning
        
        #gonna add buttons
        message.setStandardButtons(QMessageBox.Cancel|QMessageBox.Close|QMessageBox.Retry)
            #there are pleanty of buttons avaliable,they are :
                #ok,open,save,cancel,close,yes,no,retry,ignore ,etc
  
        #select default button
        message.setDefaultButton(QMessageBox.Close)
        
        #adding deatils button,on clicking it the detailed text information will be seen
        message.setDetailedText("here you will see the detailed text")
        
        #to take action on the pressed button
        message.buttonClicked.connect(self.button_clicked_from_messagebox)
            #since this is a message box, no particular button names are there
            #nd once a button is clicked,the message box will close so,
            # "buttonClicked" is used as button name here
    
        message.exec_()
    
    
    # to know when button is pressed in the message box
    def button_clicked_from_messagebox(self,i):
        #here i is the button pressed
        print(i.text())    
            #check terminal
    
    #this is to check login credentials   
    def login(self):
        if(self.login_id_entered.text()== "bi" and self.password_entered.text()== "1234"):
            self.button_for_printing.setEnabled(True)
            self.text_message.setEnabled(True)
        else:
            message=QMessageBox()
            message.setText("wrong credentials !!")
            message.setIcon(QMessageBox.Critical)
            
            message.exec_()
            
    #using shortcut key        
    def change_text(self,msg):
        self.text_message.setText(msg)

def main():
    app=QApplication([])
    window=MyGUI()
    window.setWindowTitle("Bhavya's 1st attempt to make GUI")
    app.exec_()


if __name__=="__main__":
    main()
    
    
# INFORMATIVE :-
    # self.label_name.Text() = will return the text inside the label
    # self.label_name.setText(whatever you write or give) = will change text inside the label
    
    # self.combobox_name.Text() = will return the current text inside the combo box