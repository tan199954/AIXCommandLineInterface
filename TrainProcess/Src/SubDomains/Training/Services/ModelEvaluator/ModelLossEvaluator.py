from PySide6 import QtCore

class ModelLossEvaluator(QtCore.QObject):
    LOSSES_SIZE=10
    lossIncreasing=QtCore.Signal()
    def __init__(self, parent: QtCore.QObject = None) -> None:
        super().__init__(parent)
        self.losses=list()
        self.smallestLoss=None
    def addNewLoss(self,loss:float):
        if len(self.losses)<=self.LOSSES_SIZE:
            self.losses.append(loss)
            return
        minLosses = min(self.losses)
        self.losses=list()
        if self.smallestLoss is None or minLosses<self.smallestLoss:
            self.smallestLoss = minLosses
        self.lossIncreasing.emit()