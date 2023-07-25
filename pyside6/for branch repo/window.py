from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLayout
from main import get_designer

class SystemDesignerPanel(QWidget):
    def __init__(self):
        super(SystemDesignerPanel, self).__init__()
        layout = QLayout(self).addWidget(get_designer())

VIEWS = [
    SystemDesignerPanel
    ]