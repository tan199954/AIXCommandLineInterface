from ..Interfaces.IModelInfoBuilder import IModelInfoBuilder
from ....Models.ModelInfo.Implementations.ModelInfo import ModelInfo

class BBoxModelInfoBuilder(IModelInfoBuilder):
    def setIOU(self,newIOU)->'BBoxModelInfoBuilder':
          self.iOU=newIOU
          return self
    def setMAP(self,newMAP)->'BBoxModelInfoBuilder':
        self.mAP=newMAP
        return self
    def setLoss(self,newLoss)->'BBoxModelInfoBuilder':
        self.loss=newLoss
        return self
    def build(self)->ModelInfo:
        return ModelInfo(self.loss,self.iOU,self.mAP)
    def buildFromStr(stringData:str)->ModelInfo:
        pass