from typing import List
from ....Enum.TrainType import TrainType
from ..Services.TrainPreparer.Interfaces.ITrainPreparer import ITrainPreparer
from ..Services.TrainPreparer.Implementation.YOLOTrainPreparer import YOLOTrainPreparer
from ..Services.TrainPreparer.Implementation.YOROTrainPreparer import YOROTrainPreparer
class TrainPreparerFactory:
    TRAIN_PREPARER_DICTIONARY = {
        TrainType.Seg:YOLOTrainPreparer,
        TrainType.BBox:YOROTrainPreparer,
        TrainType.Box:YOLOTrainPreparer
    }
    @staticmethod
    def createTrainPreparer(trainType:TrainType,gpuMenmory:int=None,trainPath:str=None,validPath:str=None,nameObjects:List[str]=None)->ITrainPreparer:
        return TrainPreparerFactory.TRAIN_PREPARER_DICTIONARY[trainType](gpuMenmory,trainPath,validPath,nameObjects)