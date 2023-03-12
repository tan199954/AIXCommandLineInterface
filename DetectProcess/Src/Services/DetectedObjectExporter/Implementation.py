import sys
from PySide6 import QtNetwork
from .Interfaces import IDetectedObjectExporter
from ..SocketManager.SocketManager import TcpSocketManager

class TcpSocketExporter(IDetectedObjectExporter):
     def __init__(self,tcpSocketManager:TcpSocketManager) -> None:
          super().__init__()
          self.tcpSocketManager=tcpSocketManager
     def export(self,result:str):
          socket=self.tcpSocketManager.getSocket()
          if socket.state() == QtNetwork.QTcpSocket.ConnectedState:
               socket.write(result.encode())

class TerminalExporter(IDetectedObjectExporter):
     def export(self,result:str):
          sys.stdout.write(result)
          sys.stdout.flush()