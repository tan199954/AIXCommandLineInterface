from PySide6 import QtCore
from ...Models.ModelInfo.Implementations.ModelInfo import ModelInfo

class BestModelFinder(QtCore.QObject):
    bestModelFound=QtCore.Signal(ModelInfo)
    def __init__(self, parent: QtCore.QObject = None) -> None:
        super().__init__(parent)
        self.bestModelInfo=None
    def addNewModel(self,newModelInfo:ModelInfo):
        if not self.__isGoodIOU(newModelInfo.iOU):
            return
        if not self.__isGoodMAP(newModelInfo.mAP):
            return
        if self.bestModelInfo is None:
            self.bestModelInfo=newModelInfo
            return
        self.__compareModelInfo(newModelInfo)
    def __isGoodIOU(self,newIOU:float)->bool:
        if newIOU > 0.5:
            return True
        return False
    def __isGoodMAP(self,newMAP:float)->bool:
        if newMAP >0.5:
            return True
        return False
    def __compareModelInfo(self,newModelInfo:ModelInfo):
        if newModelInfo.mAP > 0.6:
            self.bestModelFound.emit(self.bestModelInfo)
            return
        if newModelInfo.mAP > self.bestModelInfo.mAP:
            self.bestModelInfo=newModelInfo    