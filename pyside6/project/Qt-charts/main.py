import os
import sys

from ui_interface import *

# from Custom_Widgets.Widgets import *

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui =Ui_MainWindow()
        
        # loadJsonStyle(self,self.ui)
        self.ui.setupUi(self)
        
        
        
        self.ui.percentage_bar_button.clicked.connect(self.percentage_bar_button_clicked)
        self.ui.temperature_record_button.clicked.connect(self.temperature_records_clicked)
        self.ui.nested_donut_button.clicked.connect(self.nested_donuts_clicked)
        self.ui.line_chart_button.clicked.connect(self.line_chart_clicked)
        self.ui.bar_chart_button.clicked.connect(self.bar_chart_clicked)

        self.ui.pushButton_9.clicked.connect(self.close_app)
        
        
    def percentage_bar_button_clicked(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.percentage_bar_chart)
    def temperature_records_clicked(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.temperature_records)
    def nested_donuts_clicked(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.nested_donuts)
    def line_chart_clicked(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.line_chart)
    def bar_chart_clicked(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.bar_chart)
    def close_app(self):
        app.quit()












        self.show()
        
if __name__ == "__main__":
    app= QApplication(sys.argv)
    
    window= MainWindow()
    window.show()
    sys.exit(app.exec_())
    
    
    