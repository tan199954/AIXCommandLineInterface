from ..Interfaces.IModelInfo import IModelInfo

class ModelInfo(IModelInfo):
    def __init__(self,loss:float,IOU:float,MAP:float) -> None:
        self.loss=loss
        self.IOU=IOU
        self.MAP=MAP
        super().__init__()