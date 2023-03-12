from PySide6 import QtCore
from typing import Union
class ImageBuildingAccepter:
    ACCEPT_KEY="deltax"
    def __init__(self) -> None:
        self.accept=False
        self.latestUnusedData=None
    def isAccept(self)->bool:
        return self.accept
    def updateAcceptanceStatusByData(self,data:QtCore.QByteArray):
          subData = data[:len(self.ACCEPT_KEY.encode())]
          if (subData.data().decode() == self.ACCEPT_KEY):
               self.accept = True
          nextImageData =  data[len(self.ACCEPT_KEY.encode()):]
          self.__setLatestUnusedData(nextImageData)
    def getLatestUnusedData(self)->Union[QtCore.QByteArray,None]:
         """
         Return latestUnusedData if it not empty\n
         Else return None
         """
         latestUnusedData=self.latestUnusedData
         self.latestUnusedData=None
         return latestUnusedData
    def __setLatestUnusedData(self,newLatestUnusedData:QtCore.QByteArray):
         if newLatestUnusedData.isEmpty():
              self.latestUnusedData=None
         else:
              self.latestUnusedData=newLatestUnusedData