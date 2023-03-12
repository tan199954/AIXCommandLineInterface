import numpy as np
import sys
from PySide6 import QtCore, QtNetwork
from ...Exceptions.TcpException import TcpServerError


class WSLDetectingScriptsCommunicator(QtCore.QObject):
    """
    This class create TCP server to communicate with WSL
    """
    resultReceived=QtCore.Signal(str)
    def __init__(self, ip:str,port:int,parent: QtCore.QObject = None) -> None:
        super().__init__(parent)
        self._ip=ip
        self._port=port
        self.server = QtNetwork.QTcpServer()  
        self.socket = QtNetwork.QTcpSocket()     
        self.server.newConnection.connect(self.__onNewConnection)
        self.__openServer()
    def __openServer(self):
        if not self.server.listen(QtNetwork.QHostAddress(self._ip),self._port):
            raise TcpServerError(f"WSL could not start server IP: {str(QtNetwork.QHostAddress(self._ip))} ,port: {self._port}\n")
    def __onNewConnection(self):
        self.socket = self.server.nextPendingConnection()
        if self.socket.state() == QtNetwork.QTcpSocket.ConnectedState:
            sys.stdout.write(f"WSL new connection established: {self.socket.peerAddress()}\n")
            sys.stdout.flush()
        self.socket.readyRead.connect(self.__onReadyRead)
        self.socket.disconnected.connect(self.__onDisconnected)
    def __onReadyRead(self):
        data = self.socket.readAll()
        self.resultReceived.emit(data.data().decode())
    def __onDisconnected(self):
        sys.stdout.write(f"WSL client disconnected: from adress: {self.server.serverAddress()}, ip: {self.server.serverPort()}\n")
        sys.stdout.flush()
    def __getSed(self,colByte,sedNum):
        if 1024 < colByte - sedNum:
            return 1024
        return colByte - sedNum          
    def writeImage(self,image:np.ndarray):
        if not self.socket.state() == QtNetwork.QTcpSocket.ConnectedState:
            return
        height, width, channels = image.shape
        widthBytes = width.to_bytes(4, 'big')[::-1]
        heightBytes = height.to_bytes(4, 'big')[::-1]
        channelsBytes = channels.to_bytes(4, 'big')[::-1]
        shapeBytes = widthBytes + heightBytes + channelsBytes
        self.socket.write(shapeBytes)
        #send image data
        SIZE_OF_BYTE = 1
        colByte = width*channels * SIZE_OF_BYTE
        for i in range(0,height,1):
            data = image[i].tobytes()
            sedNum = 0
            while (sedNum < colByte):
                sed = self.__getSed(colByte,sedNum)
                buf = data[sedNum:sedNum+sed]
                sendSize = self.socket.write(buf)
                if (sendSize == -1):
                    break
                sedNum += sendSize  
    def __del__(self):
        self.server.close()
        self.server.deleteLater()