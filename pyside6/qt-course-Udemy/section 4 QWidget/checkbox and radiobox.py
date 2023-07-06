from PySide6.QtWidgets import QApplication,QCheckBox, QWidget,QPushButton,QSlider,QVBoxLayout,QGridLayout,QGroupBox
import sys
class class1(QWidget):
    def __init__(self):
        super().__init__()

        my_os=QGroupBox("choose your os")
        
        windows=QCheckBox("windows")
        linux=QCheckBox("linux")
        mac=QCheckBox("mac")
        
        windows.toggled.connect(self.windows_checked)
        linux.toggled.connect(self.linux_checked)
        mac.toggled.connect(self.mac_checked)
        
        my_os_layout=QVBoxLayout()
        my_os_layout.addWidget(windows)
        my_os_layout.addWidget(linux)
        my_os_layout.addWidget(mac)
        
        my_os.setLayout(my_os_layout)
        
        my_layout=QVBoxLayout()
        my_layout.addWidget(my_os)
        
        self.setLayout(my_layout)
        
        
        
        
    def windows_checked(self,checked):
        if(checked):
            print("windows was checked")
        else:
            print("unchecked")
    def linux_checked(self,checked):
        if(checked):
            print("linux was checked")
        else:
            print("unchecked")
    def mac_checked(self,checked):
        if(checked):
            print("mac was checked")
        else:
            print("unchecked")
            
app=QApplication(sys.argv)
window=class1()
window.setGeometry(100,100,200,200)

window.show()
app.exec()  