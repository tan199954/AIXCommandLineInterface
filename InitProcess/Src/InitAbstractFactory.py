from InitProcess.Src.Core import TrainType
from InitProcess.Src.Infrastructure.ImplInitFactory import BBoxInitFactory,BoxInitFactory,SegInitFactory,InitFactory

class InitAbstractFactory:
     def __init__(self,imagePath: str,labelPath :str,type:TrainType) -> None:
          self.imagePath=imagePath
          self.labelPath=labelPath
          self.type =type
     def getFactory(self)->InitFactory:
          if self.type == TrainType.BoundingBox:
               return BBoxInitFactory(self.imagePath,self.labelPath)
          if self.type == TrainType.Box:
               return BoxInitFactory(self.imagePath,self.labelPath)
          return SegInitFactory(self.imagePath,self.labelPath)
          