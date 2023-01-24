from PyQt5.QtWidgets import *

#def main():
    # app=QApplication([])
    # window=QWidget()
    
    # window.show()
    # app.exec_()
    
    
# the above comment line is
# enough to make a fucking
# window to take prompts as
# a part of gui



# now lets start developing a
# basic hello world gui


def main():
    
#step 1: set prop. for windows
    app=QApplication([])
    window=QWidget()
    
    window.setGeometry(100,100,300,300)
    window.setWindowTitle("Bhavya's 1st attempt to make GUI")
    
    
#step 2:add UI elements
    label=QLabel(window)
    label.setText("hello bhavya sir !!")
    label.move(150,150)
    
    
#step 3: To show window
    window.show()
    
#step 4: execute at the end
    app.exec_()



if __name__=="__main__":
    main()