import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel
from PySide6.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class GraphWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.figure = Figure()  # Create a Figure instance
        self.canvas = FigureCanvas(self.figure)  # Create a FigureCanvas instance and pass the Figure
        layout = QVBoxLayout()  # Create a QVBoxLayout to hold the FigureCanvas
        layout.addWidget(self.canvas)  # Add the FigureCanvas to the layout
        self.setLayout(layout)  # Set the layout for the GraphWidget

    def plot_graph(self, x_data, y_data):
        ax = self.figure.add_subplot(111)  # Add a subplot to the Figure
        ax.plot(x_data, y_data)  # Plot the data on the subplot
        self.canvas.draw()  # Redraw the FigureCanvas


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.graph_widget = GraphWidget()  # Create an instance of the GraphWidget
        self.label_widget = QWidget()  # Create an instance of the label widget

        # Example data
        x_data = [1, 2, 3, 4, 5]
        y_data = [2, 8, 6, 3, 10]

        self.graph_widget.plot_graph(x_data, y_data)  # Plot the example data on the GraphWidget

        # Create labels
        company_label = QLabel("Company Name: Your Company")
        software_label = QLabel("Software Name: Your Software")
        drone_label = QLabel("Drone ID: DRN001")

        # Set labels alignment to center
        # company_label.setAlignment(Qt.AlignCenter)
        # software_label.setAlignment(Qt.AlignCenter)
        # drone_label.setAlignment(Qt.AlignCenter)

        # Create layout for label widget
        label_layout = QVBoxLayout()
        label_layout.addWidget(company_label)
        label_layout.addWidget(software_label)
        label_layout.addWidget(drone_label)
        self.label_widget.setLayout(label_layout)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.label_widget)
        main_layout.addWidget(self.graph_widget)

        main_widget = QWidget()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())
