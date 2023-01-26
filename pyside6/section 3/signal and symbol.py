from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QApplication, QSlider,QPushButton

def respond_slider(data):
    print(f"slider is moved to {data}")

def button_clicked(data):
        print("You clicked the button : ",data)

app= QApplication()

slider=QSlider(Qt.Horizontal)
slider.setMinimum(1)
slider.setMaximum(100)
slider.setValue(25)

button = QPushButton("Press Me")
button.move(200,200)
button.setCheckable(True)
button.clicked.connect(button_clicked)


slider.valueChanged.connect(respond_slider)
slider.show()
button.show()


app.exec()
