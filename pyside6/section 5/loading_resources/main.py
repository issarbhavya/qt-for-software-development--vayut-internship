import sys

from PySide6 import QtWidgets
from working_main import Widget

app=QtWidgets.QApplication(sys.argv)

window=Widget()
window.show()

app.exec()