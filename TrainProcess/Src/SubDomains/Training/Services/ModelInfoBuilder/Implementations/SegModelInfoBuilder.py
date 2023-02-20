from ..Interfaces.IModelInfoBuilder import IModelInfoBuilder, ModelInfo


class SegModelInfoBuilder(IModelInfoBuilder):
     def __init__(self) -> None:
          super().__init__()
     def setIOU(self,newIOU)->'SegModelInfoBuilder':
          self.IOU=newIOU
          return self
     def setMAP(self,newMAP)->'SegModelInfoBuilder':
          self.MAP=newMAP
          return self
     def setLoss(self,newLoss)->'SegModelInfoBuilder':
          self.loss=newLoss
          return self
     def build(self)->ModelInfo:
        return ModelInfo(self.loss,self.IOU,self.MAP)
     @staticmethod
     def buildFromStr(stringData:str)->ModelInfo:
        pass