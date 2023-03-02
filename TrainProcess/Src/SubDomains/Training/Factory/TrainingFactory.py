from ..Enum.TrainingType import TrainingType
from ..Services.Trainer.Implementations import SegTrainer,BBoxTrainer,BoxTrainer
from ..Services.Trainer.Interfaces.ITrainer import ITrainer

class TrainingFactory:
    TRAINER_DICTIONARY = {
        TrainingType.Box:BoxTrainer.BoxTrainer,
        TrainingType.BBox:BBoxTrainer.BBoxTrainer,
        TrainingType.Seg:SegTrainer.SegTrainer
    }
    @staticmethod
    def createTrainer(trainingType:TrainingType,learningRate:float,imageSize:int,batchSize:int,manual: bool = False)->ITrainer:
        return TrainingFactory.TRAINER_DICTIONARY[trainingType](manual=manual,learningRate=learningRate,imageSize=imageSize,batchSize=batchSize)
        