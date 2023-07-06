from PySide6.QtWidgets import QWidget,QPushButton,QSlider,QHBoxLayout

class Rock_widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("my rock widget")
        button1 = QPushButton("press 1")
        slider1 = QSlider()
        
        button_layout= QHBoxLayout()
        button_layout.addWidget(button1)
        
        self.setLayout(button_layout)