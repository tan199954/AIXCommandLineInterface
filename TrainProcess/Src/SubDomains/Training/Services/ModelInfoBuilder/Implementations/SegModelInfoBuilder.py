from ..Interfaces.IModelInfoBuilder import IModelInfoBuilder, ModelInfo
from .SegLossCoefficientFinder import SegLossCoefficientFinder
from .SegMAPCoefficientFinder import SegMAPCoefficientFinder


class SegModelInfoBuilder(IModelInfoBuilder):
     IOU_DEFAULT=0.7
     def __init__(self) -> None:
          super().__init__()
          self.currentLoss=None
     def setIOU(self,newIOU)->'SegModelInfoBuilder':
          self.iOU=newIOU
          return self
     def setMAP(self,newMAP)->'SegModelInfoBuilder':
          self.mAP=newMAP
          return self
     def setLoss(self,newLoss)->'SegModelInfoBuilder':
          self.loss=newLoss
          return self
     def build(self)->ModelInfo:
          return ModelInfo(self.loss,self.iOU,self.mAP)
     def buildFromStr(self,stringData:str)->ModelInfo:
          if self.currentLoss is None:
               self.currentLoss = SegLossCoefficientFinder().getLossFrStr(stringData)
               return
          loss = self.currentLoss
          iOU=self.IOU_DEFAULT
          mAP=SegMAPCoefficientFinder.getMAPFrStr(stringData)
          if mAP is None:
               return
          self.currentLoss = None
          return ModelInfo(loss,iOU,mAP)