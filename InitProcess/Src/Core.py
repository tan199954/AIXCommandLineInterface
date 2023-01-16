from abc import ABC, abstractclassmethod
from enum import Enum

class TrainType(Enum):
     BoundingBox = "BBox"
     Box = "Box" 
     Segment = "Seg"
     NoneType = None
class DatasetService(ABC):
     def __init__(self,imagePath: str,labelPath :str) -> None:
          super().__init__()
          self.imagePath-imagePath
          self.labelPath=labelPath
     @abstractclassmethod
     def execute(self):
          pass
     @abstractclassmethod
     def getDatasetInfor(self)->dict:
          pass
class ProjInputChecker(ABC):
     def __init__(self,imagePath: str,labelPath :str) -> None:
          super().__init__()
          self.imagePath-imagePath
          self.labelPath=labelPath
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
          