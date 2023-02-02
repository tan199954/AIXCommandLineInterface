from ProjectFile.Src.Core.Interfaces.IAIXProjCompositon import IAIXProjCompositon

class DatasetInfo(IAIXProjCompositon):
    def __init__(self,datasetPath,imageTrainPath,imageValidPath,
        labelTrainPath,labelValidPath) -> None:
        super().__init__()
        self.datasetPath=datasetPath
        self.imageTrainPath=imageTrainPath
        self.imageValidPath=imageValidPath
        self.labelTrainPath=labelTrainPath
        self.labelValidPath=labelValidPath
    def getDatasetPath(self)->str:
        return self.datasetPath
    def getImageTrainPath(self)->str:
        return self.imageTrainPath
    def getImageValidPath(self)->str:
        return self.imageValidPath
    def getLabelTrainPath(self)->str:
        return self.labelTrainPath
    def getLabelValidPath(self)->str:
        return self.labelValidPath
    def getDictInfo(self)->dict:
        return {"DatasetInfo":{
            "datasetPath": self.datasetPath,
            "imageTrainPath": self.imageTrainPath,
            "imageValidPath": self.imageValidPath,
            "labelTrainPath": self.labelTrainPath,
            "labelValidPath": self.labelValidPath
        }}