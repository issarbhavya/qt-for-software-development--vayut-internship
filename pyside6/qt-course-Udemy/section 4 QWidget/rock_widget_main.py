from PySide6.QtWidgets import QApplication,QWidget
import sys
from rockwidget import Rock_widget

app=QApplication(sys.argv)
window=Rock_widget()
window.setGeometry(100,100,200,200)

window.show()
app.exec()  