from .Interfaces import IImageSourceManager
import numpy as np
import cv2
from PySide6 import QtNetwork

class TcpServerImageSoureManager(IImageSourceManager):
     def __init__(self,source:dict,socket:QtNetwork.QTcpSocket) -> None:
         super().__init__()
         self.continueGeneratingImages=False
         self.image=None
         self.ip=source["ip"]
         self.port=source["port"]
         self.socket=socket
         self.socket.disconnected.connect(self.__stopGeneratingImages)
     def isContinueGeneratingImages(self)->bool:
         return self.continueGeneratingImages
     def getImage(self)->np.ndarray:
         return self.image
     def __stopGeneratingImages(self):
         self.continueGeneratingImages=False
         self.image = None
     def __startGeneratingImages(self):
         self.continueGeneratingImages=True


class TcpClientImageSoureManager(IImageSourceManager):
     def __init__(self,source:dict,socket:QtNetwork.QTcpSocket) -> None:
         super().__init__()
         self.continueGeneratingImages=False
         self.image=None
         self.ip=source["ip"]
         self.port=source["port"]
         self.socket=socket
         self.socket.disconnected.connect(self.__stopGeneratingImages)
     def isContinueGeneratingImages(self)->bool:
         return self.continueGeneratingImages
     def getImage(self)->np.ndarray:
         return self.image
     def __stopGeneratingImages(self):
         self.continueGeneratingImages=False
         self.image = None
     def __startGeneratingImages(self):
         self.continueGeneratingImages=True

     
class FilePathImageSourceManager(IImageSourceManager):
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