from InitProcess.Src.Core import TrainType
from InitProcess.Src.Infrastructure.ImplInitFactory import BBoxInitFactory,BoxInitFactory,SegInitFactory,InitFactory

class InitAbstractFactory:
     def __init__(self,imagePath: str,labelPath :str,trainType:TrainType) -> None:
          self.imagePath=imagePath
          self.labelPath=labelPath
          self.trainType =trainType
     def getFactory(self)->InitFactory:
          if self.trainType == TrainType.BoundingBox:
               return BBoxInitFactory(self.imagePath,self.labelPath)
          if self.trainType == TrainType.Box:
               return BoxInitFactory(self.imagePath,self.labelPath)
          return SegInitFactory(self.imagePath,self.labelPath)
          