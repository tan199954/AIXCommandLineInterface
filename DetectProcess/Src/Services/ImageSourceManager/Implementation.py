import numpy as np
import sys
import cv2
from PySide6 import QtNetwork
from ...Exceptions.TcpException import TcpServerError
from ..SocketManager.SocketManager import TcpSocketManager
from .TCPSocketImageBuilder import TCPSocketImageBuilder
from .ImageBuildingAccepter import ImageBuildingAccepter
from .Interfaces import IImageSourceManager

class AbstractTcpImageSourceManager(IImageSourceManager):
    IMAGE_BUILDING_START_KEY='ExternalScript\n'
    def __init__(self,source:dict,tcpSocketManager:TcpSocketManager) -> None:
        super().__init__()
        self.continueGeneratingImages=False
        self.image=None
        self.ip=source["ip"]
        self.port=source["port"]
        self.tcpSocketManager=tcpSocketManager
        self.imageBuilder=TCPSocketImageBuilder()
        self.imageBuildingAccepter=ImageBuildingAccepter()
        self.imageBuilder.imageBuilt.connect(self.__onImageBuilt)
        self.__connectSocketSignal()
    def isContinueGeneratingImages(self)->bool:
        return self.continueGeneratingImages
    def getImage(self)->np.ndarray:
        """
        Return np.ndarray if image is built successfuly\n
        Else return None
        """
        return self.image
    def __connectSocketSignal(self):
        
        self.tcpSocketManager.getSocket().readyRead.connect(self.__onReadyRead)
        self.tcpSocketManager.getSocket().disconnected.connect(self.__onDisconnected)
        self.tcpSocketManager.getSocket().connected.connect(self.__onConnected)
    def __onConnected(self):
        self.tcpSocketManager.getSocket().write(self.IMAGE_BUILDING_START_KEY.encode())
        self.__startGeneratingImages()
    def __onReadyRead(self):
        data = self.tcpSocketManager.getSocket().readAll()
        if not self.imageBuildingAccepter.isAccept():
            self.imageBuildingAccepter.updateAcceptanceStatusByData(data)
            return
        lastUnusedData=self.imageBuildingAccepter.getLatestUnusedData()
        if lastUnusedData:
            self.imageBuilder.latestUnusedData=lastUnusedData
        self.imageBuilder.buildImageFromData(data)
    def __onDisconnected(self):
        self.__stopGeneratingImages()
        sys.stdout.write(f"Client disconnected: from adress: {self.server.serverAddress()}, ip: {self.server.serverPort()}\n")
        sys.stdout.flush()
    def __stopGeneratingImages(self):
        self.continueGeneratingImages=False
        self.image = None
    def __startGeneratingImages(self):
        self.continueGeneratingImages=True
    def __onImageBuilt(self,image:np.ndarray):
        self.image=image
    
    
class TcpServerImageSoureManager(AbstractTcpImageSourceManager):
    def __init__(self, source: dict, tcpSocketManager:TcpSocketManager) -> None:
        super().__init__(source, tcpSocketManager)
        self.server = QtNetwork.QTcpServer()
        self.server.newConnection.connect(self.__onNewConnection)
        self.__openServer()
    def __openServer(self):
        if not self.server.listen(QtNetwork.QHostAddress(self.ip),self.port):
            raise TcpServerError(f"Could not start server IP: {str(QtNetwork.QHostAddress(self._ip))} ,port: {self._port}\n")
    def __onNewConnection(self):
        socket = self.server.nextPendingConnection()
        if socket.state() == QtNetwork.QTcpSocket.ConnectedState:
            sys.stdout.write(f"New connection established: {socket.peerAddress()}\n")
            sys.stdout.flush()
        self.tcpSocketManager.setSocket(socket)
        self.__connectSocketSignal()
        self.__onConnected()
    def __del__(self):
        self.server.close()
        self.server.deleteLater()



class TcpClientImageSoureManager(AbstractTcpImageSourceManager):
    def __init__(self, source: dict, tcpSocketManager:TcpSocketManager) -> None:
        super().__init__(source, tcpSocketManager)
        self.__connectToServer()
    def __connectToServer(self):
        self.tcpSocketManager.getSocket().connectToHost(QtNetwork.QHostAddress(self.ip),self.port)
        if(not self.tcpSocketManager.getSocket().waitForConnected(3000)):
            raise TcpServerError(f"Error connecting to server: {self.tcpSocketManager.getSocket().errorString()}")
    def __del__(self):
        self.tcpSocketManager.getSocket().disconnectFromHost()



     
class FileImageSourceManager(IImageSourceManager):
     def __init__(self,source:str) -> None:
         super().__init__()
         self.image=cv2.imread(source)
         self.continueGeneratingImages = True
     def isContinueGeneratingImages(self)->bool:
         return self.continueGeneratingImages
     def getImage(self)->np.ndarray:
         image=self.image
         self.__stopGeneratingImages()
         return image
     def __stopGeneratingImages(self):
         self.image = None
         self.continueGeneratingImages=False