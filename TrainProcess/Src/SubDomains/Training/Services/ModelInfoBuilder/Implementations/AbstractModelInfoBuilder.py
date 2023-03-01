from abc import abstractproperty
from ..Interfaces.IModelInfoBuilder import IModelInfoBuilder, ModelInfo
from ..LossCoefficientFinder.AbstractLossCoefficientFinder import AbstractYOLOLossCoefficientFinder
from ..MapCoefficientFinder.AbstractMAPCoefficientFinder import AbstractYOLOMAPCoefficientFinder


class AbstractYOLOModelInfoBuilder(IModelInfoBuilder):
     IOU_DEFAULT=0.7
     @abstractproperty
     def lossCoefficientFinder(self)->AbstractYOLOLossCoefficientFinder:
          pass
     @abstractproperty
     def mAPCoefficientFinder(self)->AbstractYOLOMAPCoefficientFinder:
          pass
     def __init__(self) -> None:
          super().__init__()
          self.currentLoss=None
     def setIOU(self,newIOU)->'AbstractYOLOModelInfoBuilder':
          self.iOU=newIOU
          return self
     def setMAP(self,newMAP)->'AbstractYOLOModelInfoBuilder':
          self.mAP=newMAP
          return self
     def setLoss(self,newLoss)->'AbstractYOLOModelInfoBuilder':
          self.loss=newLoss
          return self
     def build(self)->ModelInfo:
          return ModelInfo(self.loss,self.iOU,self.mAP)
     def buildFromStr(self,stringData:str)->ModelInfo:
          loss = self.lossCoefficientFinder.getLossFrStr(stringData)
          if loss is not None:
               self.currentLoss=loss
          if self.currentLoss is None:
               return
          loss = self.currentLoss
          iOU=self.IOU_DEFAULT
          mAP=self.mAPCoefficientFinder.getMAPFrStr(stringData)
          if mAP is None:
               return
          self.currentLoss = None
          return ModelInfo(loss,iOU,mAP)
     