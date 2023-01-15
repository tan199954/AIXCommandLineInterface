import os
from PySide6 import QtCore

class ImwiProjFileService:
     def __init__(self) -> None:
          currentDir = os.getcwd()
          dirName = os.path.basename(currentDir)
          self.imwiProjFilePath = os.path.join(currentDir,dirName+".imwi") 
     def isExist(self)->bool:
          imwiProjFile=QtCore.QFile(self.imwiProjFilePath)
          return imwiProjFile.exists()
     def getImwiProjFilePath(self)->str:
          return self.imwiProjFilePath