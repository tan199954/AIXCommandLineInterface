from PySide6 import QtCore,QtNetwork
import numpy as np
from Exceptions.QSocketExceptions import QTcpSocketErrorOccurred
from TCPSocketImageBuilder import TCPSocketImageBuilder

class TCPSocketImageProcessor(QtCore.QObject):
    imageReceived = QtCore.Signal(np.ndarray)
    def __init__(self,ip:str,port:int) -> None:
        self.ip=ip
        self.port=port
        self.socket=QtNetwork.QTcpSocket()
        self.imageBuilder=TCPSocketImageBuilder()
        self.socket.readyRead.connect(self.__onReadyRead)
        self.imageBuilder.imageBuilt.connect(self.imageReceived.emit)
    def __onReadyRead(self):
        data = self.socket.readAll()
        self.imageBuilder.buildImageFromData(data)
    def run(self):
        self.socket.connectToHost(QtNetwork.QHostAddress(self.ip),self.port) 
        if(not self.socket.waitForConnected(3000)):
            self.__onConnectionFailed()
    def exportResult(self,stringData:str):
        self.socket.write(stringData.encode())
    def __onConnectionFailed(self):
        QtCore.QCoreApplication.quit()
        raise QTcpSocketErrorOccurred(f"Error connecting to server: {self.socket.errorString()}")
        