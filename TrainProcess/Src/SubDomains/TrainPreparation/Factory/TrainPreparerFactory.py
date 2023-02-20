from typing import List

from ..Services.TrainPreparer.Interfaces.ITrainPreparer import ITrainPreparer
from ..Services.TrainPreparer.Implementation.YOLOTrainPreparer import YOLOTrainPreparer
from ..Services.TrainPreparer.Implementation.YOROTrainPreparer import YOROTrainPreparer
from ..TrainPreparationEnum.TrainPreparationType import TrainPreparationType
class TrainPreparerFactory:
    TRAIN_PREPARER_DICTIONARY = {
        TrainPreparationType.YOLO:YOLOTrainPreparer,
        TrainPreparationType.YORO:YOROTrainPreparer
    }
    @staticmethod
    def createTrainPreparer(trainType:TrainPreparationType,gpuMenmory:int=None,trainPath:str=None,validPath:str=None,nameObjects:List[str]=None)->ITrainPreparer:
        return TrainPreparerFactory.TRAIN_PREPARER_DICTIONARY[trainType](gpuMenmory,trainPath,validPath,nameObjects)