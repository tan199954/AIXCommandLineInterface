from ....Models.ModelInfo.Implementations.ModelInfo import ModelInfo
from ..Interfaces.IModelInfoBuilder import IModelInfoBuilder
from ..LossCoefficientFinder.LossCoefficientFinder import BBoxLossCoefficientFinder
from ..MapCoefficientFinder.MAPCoefficientFinder import BBoxMAPCoefficientFinder
from ..IOUCoefficientFinder.IOUCoefficientFinder import BBoxIOUCoefficientFinder

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
    @staticmethod
    def buildFromStr(stringData:str)->ModelInfo:
        iOU = BBoxIOUCoefficientFinder.getIOUfrStringData(stringData)
        mAP = BBoxMAPCoefficientFinder.getMAPfrStringData(stringData)
        loss = BBoxLossCoefficientFinder.getLossfrStringData(stringData)
        if iOU is None or mAP is None or loss is None:
            return
        return ModelInfo(loss,iOU,mAP)
