from PySide6.QtWidgets import QVBoxLayout,QComboBox,QApplication, QWidget,QPushButton,QSlider,QHBoxLayout
import sys
class class1(QWidget):
    def __init__(self):
        super().__init__()
        
        self.combo_box=QComboBox(self)
        
        self.combo_box.addItem("earth")
        self.combo_box.addItem("venus")
        self.combo_box.addItem("saturn")
        self.combo_box.addItem("mars")
        
        button_for_currentvalues=QPushButton("current value")
        button_for_currentvalues.clicked.connect(self.current_value)
        button_for_getvalues=QPushButton("get values")
        button_for_getvalues.clicked.connect(self.get_values)
        
        l1=QVBoxLayout()
        l1.addWidget(self.combo_box)
        l1.addWidget(button_for_currentvalues)
        l1.addWidget(button_for_getvalues)

        self.setLayout(l1)
        
    def current_value(self):
        print("the value is :" ,self.combo_box.currentText(), "\n\nthe urrent index is : ",self.combo_box.currentIndex(), "\n")
        
    def get_values(self):
        for i in range(self.combo_box.count()):
            print("at index : ", i, " the current value is ", self.combo_box.itemText(i))
        
        
app=QApplication(sys.argv)
window=class1()
window.setGeometry(100,100,200,200)

window.show()
app.exec()  