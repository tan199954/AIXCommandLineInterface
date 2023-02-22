from PySide6 import QtCore
from .ModelLossEvaluator import ModelLossEvaluator
from .BestModelFinder import BestModelFinder
from ...Models.ModelInfo.Implementations.ModelInfo import ModelInfo

class ModelEvaluator(QtCore.QObject):
    learningRateMustDecrease=QtCore.Signal()
    datasetLowQuality = QtCore.Signal()
    bestModelFound=QtCore.Signal(ModelInfo)
    MAX_LEARNING_RATE_CHANGE_SIGNALS=5
    def __init__(self, parent: QtCore.QObject = None) -> None:
        super().__init__(parent)
        self.modelLossEvaluator=ModelLossEvaluator()
        self.modelLossEvaluator.lossIncreasing.connect(self._onLossIncreasing)
        self.bestModelFinder=BestModelFinder()
        self.bestModelFinder.bestModelFound.connect(lambda modelInfo: self.bestModelFound.emit(modelInfo))
        self.currentLearningRateChangeCount=0
    def evaluate(self,modelInfo:ModelInfo):
        self.modelLossEvaluator.addNewLoss(modelInfo.loss)
        self.bestModelFinder.addNewModel(modelInfo)
    def _onLossIncreasing(self):
        if self.currentLearningRateChangeCount <= self.MAX_LEARNING_RATE_CHANGE_SIGNALS:
            self.learningRateMustDecrease.emit()
            self.currentLearningRateChangeCount += 1
            return
        self.datasetLowQuality.emit()

