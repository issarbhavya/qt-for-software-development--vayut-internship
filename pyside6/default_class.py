from PySide6.QtWidgets import QApplication, QWidget,QPushButton,QSlider,QHBoxLayout
import sys
class class1(QWidget):
    def __init__(self):
        super().__init__()

        
        
app=QApplication(sys.argv)
window=class1()
window.setGeometry(100,100,200,200)

window.show()
app.exec()  