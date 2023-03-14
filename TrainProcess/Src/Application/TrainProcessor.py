from typing import List
from ..Enum.TrainType import TrainType
from ..SubDomains.TrainPreparation.Factory.TrainPreparerFactory import TrainPreparerFactory
from ..SubDomains.Training.Factory.TrainerFactory import TrainerFactory
from ..SubDomains.TrainExportation.Factory.TrainExporterFactory import TrainExporterFactory
class TrainProcessor:
    def __init__(self,trainType:TrainType,gpuMenmory:int,trainPath:str,validPath:str
                 ,objectNames:List[str],learningRate:float
                 ,imageSize:int,batchSize:int,manual:bool=False) -> None:
        self.trainPreparer=TrainPreparerFactory.createTrainPreparer(trainType,gpuMenmory,
                                                                    trainPath,validPath,objectNames)
        self.trainer=TrainerFactory.createTrainer(trainType,learningRate,imageSize,batchSize,manual)
        self.trainExporter=TrainExporterFactory.createTrainExporter(trainType)
    def execute(self):
        self.trainPreparer.prepare()
        self.trainer.train()
        self.trainExporter.export()
    def getDictionaryData(self):
        return {
            "outputPath":self.trainExporter.outputPath,
            "outputModelFilePath":self.trainExporter.ouputModelFilePath
        }