from PySide6.QtCore import Qt,QFile,QIODevice,QTextStream
from PySide6.QtWidgets import QWidget,QFileDialog
from ui_widget import Ui_Widget

class Widget(QWidget,Ui_Widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("file working")
        
        self.write_button.clicked.connect(self.writ_button_was_clicked)
        self.read_button.clicked.connect(self.read_button_was_clicked)
        
        
    # write file
    def writ_button_was_clicked(self):
        file_name,_ = QFileDialog.getSaveFileName(self, "write File",
                                 "/home/jana/untitled.png",
                                 "Text(*.txt);;Images (*.png *.xpm *.jpg);;All files(*.*)")
        if (file_name==""):
            return
        print("path to file is :",file_name)
        
        file=QFile(file_name)
        if(not file.open(QIODevice.WriteOnly | QIODevice.Text)):
            return
        
        out=QTextStream(file)
        out << self.textEdit.toPlainText() << "\n"
        file.close()
    
    
    
    
    
    #read file       
    def read_button_was_clicked(self):
        file_content=""
        file_name,_ = QFileDialog.getOpenFileName(self, "read File",
                                 "/home/jana/untitled.png",
                                 "Text(*.txt);;Images (*.png *.xpm *.jpg);;All files(*.*)")
        if (file_name==""):
            return
        print("path to file is :",file_name)
        file=QFile(file_name)
        if(not file.open(QIODevice.ReadOnly | QIODevice.Text)):
            return
        
        in_stream=QTextStream(file)
        
        while(not in_stream.atEnd()):
            line=in_stream.readLine()
            
            file_content += line
            file_content += "\n"
            
        file.close()
        self.textEdit.clear()
        self.textEdit.setText(file_content)
            
        
        