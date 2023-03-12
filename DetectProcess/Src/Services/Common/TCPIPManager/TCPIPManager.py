import socket
import ipaddress

class TCPIPManager:
    MIN_PORT_NUM=0
    MAX_PORT_NUM=65535
    @staticmethod
    def isListeningServer(ipAddress, port):
          s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
          try:
               s.connect((ipAddress, port))
               s.shutdown(socket.SHUT_RDWR)
               return True
          except:
               return False
          finally:
               s.close()
    @staticmethod
    def isIpv4Format(ipAdress:str)->bool:
          try:
               ipaddress.IPv4Address(ipAdress)
               return True
          except ipaddress.AddressValueError:
               return False
    @classmethod
    def isValidPortRange(cls,port:int)->bool:
          if not isinstance(port,int):
               return False
          return port >= cls.MIN_PORT_NUM and port <= cls.MAX_PORT_NUM