from PySide6.QtCore import Qt,QByteArray,QTextStream,QIODevice,QFile,QJsonArray,QJsonDocument,QUrl
from PySide6.QtWidgets import QWidget,QListWidget
from ui_widget import Ui_Widget

from PySide6.QtNetwork import QNetworkAccessManager,QNetworkRequest,QNetworkReply

class Widget(QWidget,Ui_Widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("uic JSON DATA")
        
        self.manager=QNetworkAccessManager(self) #object created
        
        self.buffer_data= QByteArray() #will be used to store data as it comes in from the internet
        
        self.request=QNetworkRequest() #through this we are gonna send request to the internet
        
        self.request.setUrl(QUrl("https://www.jsonplaceholder.typeicode.com/posts"))
        
        self.fetch_button.clicked.connect(self.fetch_button_clcked)
        
        
    def fetch_button_clcked(self):
        self.net_reply=self.manager.get(self.request)
        self.net_reply.readyRead.connect(self.data_ready_to_read)
        self.net_reply.finished.connect(self.data_read_finished)
       
        
    def data_ready_to_read(self):
        print("data avaliable")
        self.buffer_data.append(self.net_reply.readAll())
        
    def data_read_finished(self):
        print("data reading finished")
        doc =QJsonDocument.fromJson(self.buffer_data)     #converting buffer data to json document
        array =QJsonArray(doc.array())  #converting JSON doc into array form
        
        #now we are gonna loop through the JSON array, reading things as objects
        self.listWidget=QListWidget(self)
        for i in range (array.count()):
            object = array.at(i).toObject 
            text="[" + str(i)+ "] : " + str( object["title"]) 
            
            self.listWidget.addItem(text) # why is it not printing 
        
        