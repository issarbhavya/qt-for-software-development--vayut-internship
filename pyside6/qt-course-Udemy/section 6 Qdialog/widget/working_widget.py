from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget
from ui_widget import Ui_widget
from working_infor_widget import Info_Widget

class Widget(QWidget,Ui_widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("main widget")
        
        self.pushButton.clicked.connect(self.show_info_dialogue)
        
        self.info_dialog=Info_Widget()
        
    def show_info_dialogue(self):
        ret = self.info_dialog.exec()
        self.label.setText("occupation is : "+ self.info_dialog.text_in_occupation+" , and Choice is : "+ self.info_dialog.text_in_combobox)
        self.label.adjustSize()
        
        