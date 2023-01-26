from PySide6.QtWidgets import QApplication, QWidget, QMainWindow,QPushButton
import sys

app=QApplication(sys.argv)

#window = QWidget()
    #the above line will create a window too

window = QMainWindow()
window.setGeometry(0,0,300,300)
window.setWindowTitle("my 2nd gui")
#also used to create a window

button= QPushButton("press me")

#here we have directly added the text to put on the button

window.setCentralWidget(button)

window.show()

app.exec()