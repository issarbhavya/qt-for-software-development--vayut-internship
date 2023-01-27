from PySide6.QtWidgets import QTabWidget,QVBoxLayout, QLineEdit, QLabel, QApplication, QWidget,QPushButton,QHBoxLayout
import sys
class class1(QWidget):
    def __init__(self):
        super().__init__()  
        self.setWindowTitle("learning tabs")
        
        tab_widget=QTabWidget()
        
        
        widget1=QWidget()
        label1=QLabel("enter the information below : ")
        line_text=QLineEdit()
        layout1=QHBoxLayout()
        layout1.addWidget(label1)
        layout1.addWidget(line_text)
        widget1.setLayout(layout1)
        
        
        widget2=QWidget()
        b1=QPushButton("b1")
        b2=QPushButton("b2")
        layout2=QVBoxLayout()
        layout2.addWidget(b1)
        layout2.addWidget(b2)
        #b1.clicked.connect(b1_was_clicked)
        widget2.setLayout(layout2)
        
        
        
        tab_widget.addTab(widget1,"this is tab 1")
        tab_widget.addTab(widget2,"this is tab 2")
        
        main_layout=QVBoxLayout()
        main_layout.addWidget(tab_widget)
        
        self.setLayout(main_layout)
        
        
        
app=QApplication(sys.argv)
window=class1()
window.setGeometry(100,100,200,200)

window.show()
app.exec()  