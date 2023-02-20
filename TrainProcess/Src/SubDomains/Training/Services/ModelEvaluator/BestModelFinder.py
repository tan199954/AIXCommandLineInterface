from PySide6 import QtCore
from ....Models.ModelInfo.Implementations.ModelInfo import ModelInfo

class BestModelFinder(QtCore.QObject):
    bestModelFound=QtCore.Signal(ModelInfo)
    def __init__(self) -> None:
        self.bestModelInfo=None
    def addNewModel(self,newModelInfo:ModelInfo):
        if not self.__isGoodIOU(newModelInfo.IOU):
            return
        if not self.__isGoodMAP(newModelInfo.MAP):
            return
        if self.bestModelInfo is None:
            self.bestModelInfo=newModelInfo
            return
        self.__compareModelInfo(newModelInfo)
    def __isGoodIOU(newIOU:float)->bool:
        if newIOU > 0.5:
            return True
        return False
    def __isGoodMAP(newMAP:float)->bool:
        if newMAP >0.5:
            return True
        return False
    def __compareModelInfo(self,newModelInfo:ModelInfo):
        if newModelInfo.MAP > 0.6:
            self.bestModelFound.emit(self.bestModelInfo)
            return
        if newModelInfo.MAP > self.bestModelInfo.MAP:
            self.bestModelInfo=newModelInfo    