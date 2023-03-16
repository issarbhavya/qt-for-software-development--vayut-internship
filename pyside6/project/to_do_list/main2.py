import sys

from PySide6 import QtWidgets
from working2 import Widget

app=QtWidgets.QApplication(sys.argv)

window=Widget()
window.show()

app.exec()