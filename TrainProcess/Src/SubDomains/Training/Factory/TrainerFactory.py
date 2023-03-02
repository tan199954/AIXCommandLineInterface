from ....Enum.TrainType import TrainType
from ..Services.Trainer.Implementations import SegTrainer,BBoxTrainer,BoxTrainer
from ..Services.Trainer.Interfaces.ITrainer import ITrainer

class TrainerFactory:
    TRAINER_DICTIONARY = {
        TrainType.Box:BoxTrainer.BoxTrainer,
        TrainType.BBox:BBoxTrainer.BBoxTrainer,
        TrainType.Seg:SegTrainer.SegTrainer
    }
    @staticmethod
    def createTrainer(trainingType:TrainType,learningRate:float,imageSize:int,batchSize:int,manual: bool = False)->ITrainer:
        return TrainerFactory.TRAINER_DICTIONARY[trainingType](manual=manual,learningRate=learningRate,imageSize=imageSize,batchSize=batchSize)
        