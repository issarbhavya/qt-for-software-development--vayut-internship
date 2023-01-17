import sys
from PyQt5 import QtWidgets, uic
 
app = QtWidgets.QApplication(sys.argv)
 
window = uic.loadUi("new_gui.ui")
window.show()
app.exec()