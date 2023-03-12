from PySide6 import QtNetwork

class TcpSocketManager:
    def __init__(self) -> None:
        self.socket=QtNetwork.QTcpSocket()
    def setSocket(self,newSocket:QtNetwork.QTcpSocket):
        self.socket=newSocket
    def getSocket(self)->QtNetwork.QTcpSocket:
        return self.socket