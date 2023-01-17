from abc import ABC, abstractclassmethod
from enum import Enum
from PySide6 import QtCore
import os

class TrainType(Enum):
     BoundingBox = "BBox"
     Box = "Box" 
     Segment = "Seg"
     NoneType = None
class DatasetFormat(ABC):
     def __init__(self,imagePath: str,labelPath :str) -> None:
          super().__init__()
          self.imagePath=imagePath
          self.labelPath=labelPath
          currentPath = os.path.dirname(os.getcwd())
          self.datasetPath=os.path.join(currentPath,"Dataset")
          self.initDatasetDir()
     def initDatasetDir(self):
          if not os.path.exists(self.datasetPath):
               os.mkdir(self.datasetPath)
     @abstractclassmethod
     def makeDirectory(self):
          pass
class DatasetService(ABC):
     def __init__(self,imagePath: str,labelPath :str) -> None:
          super().__init__()
          self.imagePath=imagePath
          self.labelPath=labelPath
     @abstractclassmethod
     def execute(self):
          pass
     @abstractclassmethod
     def getDatasetInfo(self)->dict:
          pass
class ProjInputChecker(ABC):
     def __init__(self,imagePath: str,labelPath :str) -> None:
          super().__init__()
          self.imagePath=imagePath
          self.labelPath=labelPath
          self.generalCheck()
     def checkExists(self):
          paths = [self.imagePath,self.labelPath]
          for path in paths:
               if not QtCore.QDir(path).exists():
                    raise Exception(f"{path} is not exists")
     def checkContainImages(self):
          paths = [self.imagePath]
          filters = [ "*.png" , "*.jpg" , "*.bmp"]
          for path in paths:
               fileInfoList = QtCore.QDir(path).entryInfoList(filters, QtCore.QDir.Files|QtCore.QDir.NoDotAndDotDot)
               if not fileInfoList:
                    raise Exception(f"{path} is not contain image (png,jpg,bmp)")
     def generalCheck(self):
          self.checkExists()
          self.checkContainImages()
     @abstractclassmethod
     def check(self):
          pass
class InitFactory(ABC):
     def __init__(self,imagePath: str,labelPath :str) -> None:
          super().__init__()
          self.imagePath-imagePath
          self.labelPath=labelPath
     @abstractclassmethod
     def createProjInputChecker(self)->ProjInputChecker:
          pass
     @abstractclassmethod
     def createDatasetService(self)->DatasetService:
          pass
          