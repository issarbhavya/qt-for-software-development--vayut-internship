from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont


def main():
    
#step 1: set prop. for windows
    app=QApplication([])
    window=QWidget()
    
    window.setGeometry(100,100,200,300)
    window.setWindowTitle("Bhavya's 1st attempt to make GUI")
    
    
#step 2:add UI elements (main part)

    # here we are learning to add button
    
    # we can do that manually by giving positions
    # but still we will use 
    # "QVBoxLayout" ,it stands for q vertical box layout
    # by this we are gonna stack elements on top of each other
    # "QHBoxLayout" ,elements will be placed Horizontally
    
    
    layout= QVBoxLayout()
    
    #functions are created
    label = QLabel("press button my lord !!")
    
    #doubt: why my label isn't changing position
    #according to my command move
    label.move(100,100)
        #i am creating a text edit box to write anything inside it
    textbox=QTextEdit()
    button= QPushButton("I am the button to be pressed")
    #always remember to add all your created interface to our layout
    
    #they are added to our layout
    layout.addWidget(label)
    layout.addWidget(textbox)
    layout.addWidget(button)

    #now we are gonna add layout to our window 
    window.setLayout(layout)
    
    #----------------------

    #till now as no action has been installed on
    #pressing the button,it will not result in anything,but now
    
    #a way to simply create message box 
    #
    # button.clicked.connect(on_clicked2)

    #once clicked, message in textbox is transfered to the 
    #new message box created
    
    button.clicked.connect(lambda: on_clicked3(textbox.toPlainText()))

    # we use lambda as
    # "on_clicked3(textbox.toPlainText())" is a func call
    # and we don't want func call to happen unlesss 
    # the connect event is triggered
    
    
    
    
#step 3: To show window
    window.show()
    
#step 4: execute at the end
    app.exec_()



#this will print command added in terminal
#on clicking the button
def on_clicked1():
    print("hellow sir ji")


#this will create a meesage box everytime we click the button
def on_clicked2():
    message=QMessageBox()
    message.setText("hello sir ji (from box)")
    message.exec_()
    # only one message box is created at one time,we can create
    # moreonly on clicking on the first
    
def on_clicked3(msg):
    message=QMessageBox()
    message.setText(msg)
    message.exec_()
    


if __name__=="__main__":
    main()