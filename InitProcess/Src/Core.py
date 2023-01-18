from abc import ABC, abstractclassmethod
from enum import Enum
from typing import List
from PySide6 import QtCore
import os

class TrainType(Enum):
     BoundingBox = "BBox"
     Box = "Box" 
     Segment = "Seg"
     NoneType = None
class DatasetItem:
    def __init__(self,imagePath,labelPath):
        self.imagePath=imagePath
        self.labelPath=labelPath
    def getImagePath(self):
        return self.imagePath
    def getLabelPath(self):
        return self.labelPath
class DatasetDirFormat(ABC):
     def __init__(self) -> None:
          super().__init__()
          currentPath = os.path.dirname(os.getcwd())
          self.datasetPath=os.path.join(currentPath,"Dataset")
     def makeDirs(self):
          self.makeDatasetDir()
          self.makeSubDir()
     def makeDatasetDir(self):
          if not os.path.exists(self.datasetPath):
               os.mkdir(self.datasetPath)
     def makeSubDir(self):
        subDirs =self.getImageTrainValidPath()+self.getLabelTrainValidPath()
        for subDir in subDirs:
            if not os.path.exists(subDir):
                os.makedirs(subDir)
     @abstractclassmethod     
     def getImageTrainValidPath(self)->List[str]:
          pass
     @abstractclassmethod     
     def getLabelTrainValidPath(self)->List[str]:
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
class AbstractDatasetService(ABC):
     @abstractclassmethod
     def execute(self):
          pass
     @abstractclassmethod
     def getDatasetInfo(self)->dict:
          pass
class AbstractLabelPathService(ABC):
     def __init__(self,imageFilePath:str,labelPath) -> None:
          super().__init__()
          self.imageFilePath=imageFilePath
          self.labelPath=labelPath
     @abstractclassmethod
     def getLabelFilePath(self)->str:
          pass
class InitFactory(ABC):
     def __init__(self,imagePath: str,labelPath :str) -> None:
          super().__init__()
          self.imagePath=imagePath
          self.labelPath=labelPath
     @abstractclassmethod
     def createProjInputChecker(self)->ProjInputChecker:
          pass
     @abstractclassmethod
     def createDatasetService(self)->AbstractDatasetService:
          pass
          