import sys

from PySide6 import QtWidgets
from working_loginid_password import Widget

app=QtWidgets.QApplication(sys.argv)

window=Widget()
window.show()

app.exec()