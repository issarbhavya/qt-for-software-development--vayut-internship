import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QLabel, QLineEdit, QPushButton
from PySide6.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from sqlalchemy import create_engine, Column, Integer, Float
from sqlalchemy.orm import declarative_base, sessionmaker


# SQLAlchemy setup
engine = create_engine('sqlite:///drone_data.db.sqlite3')  # Create an SQLite engine
Base = declarative_base()  # Create a base class for SQLAlchemy models


class DroneData(Base):
    __tablename__ = 'drone_data'
    time_ = Column(Integer, primary_key=True)
    speed = Column(Float)
    altitude = Column(Float)


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
        company_label = QLabel("Company Name: Your Company")  # Create a QLabel for company name
        software_label = QLabel("Software Name: Your Software")  # Create a QLabel for software name
        drone_label = QLabel("Drone ID: DRN001")  # Create a QLabel for drone ID
        speed_label = QLabel("Speed:")  # Create a QLabel for speed

        # Set labels alignment to center
        company_label.setAlignment(Qt.AlignCenter)
        software_label.setAlignment(Qt.AlignCenter)
        drone_label.setAlignment(Qt.AlignCenter)
        speed_label.setAlignment(Qt.AlignCenter)

        # Create layout for label widget
        label_layout = QVBoxLayout()  # Create a QVBoxLayout to hold the labels
        label_layout.addWidget(company_label)  # Add the company label to the layout
        label_layout.addWidget(software_label)  # Add the software label to the layout
        label_layout.addWidget(drone_label)  # Add the drone label to the layout
        label_layout.addWidget(speed_label)  # Add the speed label to the layout

        # Create text input for speed
        self.speed_input = QLineEdit()  # Create a QLineEdit for speed input
        self.speed_input.setAlignment(Qt.AlignCenter)  # Set alignment of the speed input to center
        label_layout.addWidget(self.speed_input)  # Add the speed input to the layout

        # Create button to save data
        save_button = QPushButton("Save Data")  # Create a QPushButton for saving data
        save_button.clicked.connect(self.save_data)  # Connect the button's clicked signal to save_data method
        label_layout.addWidget(save_button)  # Add the save button to the layout

        self.label_widget.setLayout(label_layout)  # Set the label layout for the label widget

        main_layout = QHBoxLayout()  # Create a QHBoxLayout to hold the main widgets
        main_layout.addWidget(self.label_widget)  # Add the label widget to the main layout
        main_layout.addWidget(self.graph_widget)  # Add the graph widget to the main layout

        main_widget = QWidget()  # Create a main widget to hold the main layout
        main_widget.setLayout(main_layout)  # Set the main layout for the main widget
        self.setCentralWidget(main_widget)  # Set the main widget as the central widget of the main window

        # Create session
        Session = sessionmaker(bind=engine)  # Create a session factory with the database engine
        self.session = Session()  # Create a session

        # Create table if not exists
        Base.metadata.create_all(engine)  # Create the table in the database if it does not exist

    def save_data(self):
        speed = self.speed_input.text()  # Get the speed value from the speed input
        self.speed_input.clear()
        if speed:
            speed_value = float(speed)  # Convert the speed value to float
            drone_data = DroneData(speed=speed_value, altitude=0)  # Create a new DroneData instance
            self.session.add(drone_data)  # Add the DroneData instance to the session
            self.session.commit()  # Commit the changes to the database
            print("Data saved successfully!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())
