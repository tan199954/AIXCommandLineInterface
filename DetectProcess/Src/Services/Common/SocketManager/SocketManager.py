import socket

class SocketManager:
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