from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget
from ui_spin_button import Ui_Form

class Widget(QWidget,Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("uic converted")
        self.spinBox.setValue(50)
        self.plus_button.clicked.connect(self.plus)
        self.minus_button.clicked.connect(self.minus)
        
        
    def plus(self):
        value = self.spinBox.value()
        self.spinBox.setValue(value + 1)

    def minus(self):
        value = self.spinBox.value()
        self.spinBox.setValue(value - 1)