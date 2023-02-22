from ..Interfaces.IModelInfo import IModelInfo

class ModelInfo(IModelInfo):
    def __init__(self,loss:float,iOU:float,mAP:float) -> None:
        self.loss=loss
        self.iOU=iOU
        self.mAP=mAP
        super().__init__()