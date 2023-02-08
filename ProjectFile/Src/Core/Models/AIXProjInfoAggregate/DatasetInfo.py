from ProjectFile.Src.Core.Interfaces.IAIXProjCompositon import IAIXProjCompositon

class DatasetInfo(IAIXProjCompositon):
    def __init__(self,datasetPath:str=None,trainImagePath:str=None,validImagePath:str=None,
        trainLabelPath:str=None,validLabelPath:str=None) -> None:
        super().__init__()
        self.datasetPath=datasetPath
        self.trainImagePath=trainImagePath
        self.validImagePath=validImagePath
        self.trainLabelPath=trainLabelPath
        self.validLabelPath=validLabelPath
    def getDatasetPath(self)->str:
        return self.datasetPath
    def getTrainImagePath(self)->str:
        return self.trainImagePath
    def getValidImagePath(self)->str:
        return self.validImagePath
    def getTrainLabelPath(self)->str:
        return self.trainLabelPath
    def getValidLabelPath(self)->str:
        return self.validLabelPath
