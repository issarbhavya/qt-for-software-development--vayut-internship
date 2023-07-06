from PySide6.QtWidgets import QSizePolicy,QTextEdit,QApplication, QWidget,QHBoxLayout,QVBoxLayout,QPushButton
import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QPalette
class class1(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("bhavya made this notepad")
        self.text_edit=QTextEdit()

        
        copy_button=QPushButton("copy")
        cut_button=QPushButton("cut")
        paste_button=QPushButton("paste")
        undo_button=QPushButton("undo")
        self.redo_button=QPushButton("redo")
        
        #copy_button.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Expanding)
        #this is used to set size on responce to expansion
        copy_button.clicked.connect(self.text_edit.copy)
        cut_button.clicked.connect(self.text_edit.cut)
        paste_button.clicked.connect(self.text_edit.paste)
        undo_button.clicked.connect(self.text_edit.undo)
        self.redo_button.clicked.connect(self.text_edit.redo)
        
        
        layout_for_mytextedit=QHBoxLayout()
        layout_for_mytextedit.addWidget(copy_button)
        layout_for_mytextedit.addWidget(cut_button)
        layout_for_mytextedit.addWidget(paste_button)
        layout_for_mytextedit.addWidget(undo_button)
        layout_for_mytextedit.addWidget(self.redo_button)
        





        main_layout=QVBoxLayout()
        

          
        main_layout.addLayout(layout_for_mytextedit)
        main_layout.addWidget(self.text_edit)

        self.setLayout(main_layout)



        
app=QApplication(sys.argv)
window=class1()
window.setGeometry(100,100,500,500)

window.show()
app.exec()  