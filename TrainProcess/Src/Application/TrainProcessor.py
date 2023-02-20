from typing import List
from ..Enum.TrainType import TrainType
from ..Services.TrainTypeConverter.TrainTypeConverter import TrainTypeCVT
from ..SubDomains.TrainPreparation.Factory.TrainPreparerFactory import TrainPreparerFactory
from ..Trainner import Trainner
from ..TrainPreparer import TrainPreparer
class TrainProcessor:
    def __init__(self,trainType:TrainType,gpuMenmory:int,trainPath:str,validPath:str
                 ,nameObjects:List[str],manual:bool=False) -> None:
        trainPrepationType = TrainTypeCVT.train2PreparationType(trainType)
        trainingType = TrainTypeCVT.train2TraningType(trainType)
        trainExportationType=TrainTypeCVT.train2ExportationType(trainType)
        self.trainExporter=TrainPreparerFactory.createTrainPreparer(trainPrepationType,gpuMenmory,
                                                                    trainPath,validPath,nameObjects)
        self.trainner=Trainner()
        self.trainPreparer=TrainPreparer()
    def execute(self):
        self.trainPreparer.execute()
        self.trainPreparer.execute()
        self.trainPreparer.execute()
    def getDictionaryData(self):
        return {
            "outputPath":self.trainExporter.outputPath,
            "modelFilePath":self.trainExporter.ouputModelFilePath
        }