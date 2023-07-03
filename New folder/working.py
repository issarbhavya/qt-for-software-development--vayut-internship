from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget
from ui_interface import Ui_MainWindow

class Widget(QWidget,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("uic converted")