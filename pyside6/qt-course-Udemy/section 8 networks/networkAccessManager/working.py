from PySide6.QtCore import Qt,QByteArray,QTextStream,QUrl,QIODevice,QFile
from PySide6.QtWidgets import QWidget
from ui_widget import Ui_Widget

from PySide6.QtNetwork import QNetworkAccessManager,QNetworkRequest,QNetworkReply



class Widget(QWidget,Ui_Widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("uic networkaccessmanager")
        
        # we get data in parts from the website like, we arew not gonna 
        # get data completely all at once, so this catches parts of it 
        
        self.manager=QNetworkAccessManager(self) #object created
        
        self.m_buffer_data= QByteArray() #will be used to store data as it comes in from the internet
        
        self.request=QNetworkRequest() #through this we are gonna send request to the internet
        
        self.request.setUrl(QUrl("https://www.github.com")) #requested url is sent 
        
        self.net_reply=self.manager.get(self.request)
        
        #below are signals that tell us how to get data from the net
        
        
        self.net_reply.readyRead.connect(self.data_ready_to_read)
        self.net_reply.finished.connect(self.data_read_finished)
       
        
    def data_ready_to_read(self):
        print("data avaliable")
        self.m_buffer_data.append(self.net_reply.readAll())
        
    def data_read_finished(self):
        print("data reading finished")
        # if (self.net_reply.error()):
        #     print("error might occur")
        # else:
        #     self.textEdit.setText(str(self.m_buffer_data))
        self.textEdit.setText(str(self.m_buffer_data))