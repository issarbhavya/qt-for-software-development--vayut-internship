from PySide6.QtWidgets import QLineEdit,QLabel,QVBoxLayout,QMessageBox ,QApplication, QWidget,QPushButton,QSlider,QHBoxLayout,QBoxLayout
from PySide6.QtCore import Qt
import sys
class class1(QWidget):
    def __init__(self):
        super().__init__()
        button1 = QPushButton("press 1")
        slider1 = QSlider(Qt.Horizontal)
        slider1.setMinimum(0)
        slider1.setMaximum(100)
        
        label=QLabel("Enter Text : ")
        label.move(10,400)
        
        self.line_text=QLineEdit()
        self.line_text.textChanged.connect(self.text_changed)
        self.line_text.editingFinished.connect(self.button1_clicked)
        
        self.label_text=QLabel("the text you entered will be shown here")
        
        button1.clicked.connect(self.button1_clicked)
        
        my_layout= QVBoxLayout()
        
        my_layout.addWidget(slider1)
        my_layout.addWidget(label)
        my_layout.addWidget(self.line_text)
        my_layout.addWidget(self.label_text)
        my_layout.addWidget(button1)

        self.setLayout(my_layout)
        
    def button1_clicked(self):
        mssg=QMessageBox()
        mssg.setText("press Ok to clear text entered")
        mssg.setIcon(QMessageBox.Information)
        mssg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        mssg.setDefaultButton(QMessageBox.Ok)
        button_clicked=mssg.exec()
        if button_clicked== QMessageBox.Ok:
            print("you selected Ok")
            #self.label_text.setText("the text you enter will be shown here") 
            # no use as , textChanged.connect will change the text here as well
            self.line_text.setText("")
            
    def text_changed(self):
        self.label_text.setText(self.line_text.text())

    
app=QApplication(sys.argv)
window=class1()
window.setGeometry(100,100,500,500)

window.show()
app.exec()  