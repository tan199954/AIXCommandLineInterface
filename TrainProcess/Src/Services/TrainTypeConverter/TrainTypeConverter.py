from ...Enum.TrainType import TrainType
from ...SubDomains.TrainPreparation.TrainPreparationEnum.TrainPreparationType import TrainPreparationType

class TrainTypeCVT:
    TRAIN_TO_PREPARETION_DICTIONARY={TrainType.BBox:TrainPreparationType.YORO,
                                TrainType.Box:TrainPreparationType.YOLO,
                                TrainType.Seg:TrainPreparationType.YOLO}
    @staticmethod
    def train2PreparationType(trainType:TrainType)->TrainPreparationType:
        return TrainTypeCVT.TRAIN_TO_PREPARETION_DICTIONARY[trainType]
    @staticmethod
    def train2TraningType(trainType:TrainType):
        return
    @staticmethod
    def train2ExportationType(trainType:TrainType):
        return
