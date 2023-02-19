from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog
#as here i have taken dialog instead of widget, the 2nd widget that
# shows will not allow any activity on the first widget until it is closed

from ui_infor_widget import Ui_main_Dialog

class Info_Widget(QDialog,Ui_main_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("info dialogue")
        
        self.text_in_occupation=""
        self.text_in_combobox=""
        
        self.ok_button.clicked.connect(self.ok_was_pressed)
        self.close_button.clicked.connect(self.close_was_pressed)
        
    def ok_was_pressed(self):
        self.text_in_occupation=self.occupation_text.text()
        self.text_in_combobox=self.combobox_info.currentText()
        self.close()
    def close_was_pressed(self):
        print("request denied")
        self.close()
    
        
        