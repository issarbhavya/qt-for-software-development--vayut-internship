from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QApplication, QSlider,QPushButton
import sys

def respond_slider(data):
    print(f"slider is moved to {data}")

app= QApplication(sys.argv)
window=QWidget()
layout=QVBoxLayout()

slider=QSlider(Qt.Horizontal)
slider.setMinimum(1)
slider.setMaximum(100)
slider.setValue(25)
slider.setValue(25)

button=QPushButton("press me")
button.move(200,200)

slider.valueChanged.connect(respond_slider)
slider.show()
button.show()


layout.addWidget(slider)
layout.addWidget(button)

window.setLayout(layout)

app.exec()