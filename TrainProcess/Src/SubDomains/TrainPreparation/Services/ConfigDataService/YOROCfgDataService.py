import os

from ....Common.PathConverter.PathConverter import PathConverter
from ..YAMLFileService.YAMLFileService import YAMLFileService

currentFilePath=os.path.abspath(__file__)
configDataServicePath=os.path.dirname(currentFilePath)
ServicesPath=os.path.dirname(configDataServicePath)
TrainPreparationPath=os.path.dirname(ServicesPath)
SubDomainPath=os.path.dirname(TrainPreparationPath)
SrcPath=os.path.dirname(SubDomainPath)
TrainProcessPath=os.path.dirname(SrcPath)

class YOROCfgDataService:
    SAMPLE_CFG_FILE_RELATIVE_PATH=r"SampleFiles\YOROConfig.yaml"
    BATCH_SIZE_DEFAULT=32
    def __init__(self, gpuMenmory: int, trainPath: str, 
                 validPath: str,configFilePath:str,namesFilePath:str) -> None:
        self.gpuMenmory=gpuMenmory
        self.trainPath=trainPath
        self.validPath=validPath
        self.configFilePath=configFilePath
        self.namesFilePath=namesFilePath
        self.sampleCfgFilePath=os.path.join(TrainProcessPath,self.SAMPLE_CFG_FILE_RELATIVE_PATH)
    def getNewConfigData(self):
        currentData=self._getCurrentCofigData()
        return self._getNewConfigDataFrOldData(currentData)
    def _getNewMaxIter(self,oldMaxIter:int):
        return oldMaxIter+3000
    def _getNewLr(self,oldMaxIter:float):
        return oldMaxIter/10
    def _getBathSize(self):
        #update later
        return self.BATCH_SIZE_DEFAULT
    def _getNewConfigDataFrOldData(self,oldCofigData:dict):
        newCofigData=oldCofigData
        newCofigData["dataset"]["names_file"]=PathConverter.Windows2WSL(self.namesFilePath)
        newCofigData["dataset"]["train_dir"]=PathConverter.Windows2WSL(self.trainPath)
        newCofigData["dataset"]["valid_dir"]=PathConverter.Windows2WSL(self.validPath)
        newCofigData["train_param"]["batch"]=self._getBathSize()
        newCofigData["train_param"]["max_iter"]=self._getNewMaxIter(newCofigData["train_param"]["max_iter"])
        return newCofigData 
    def _getCurrentCofigData(self):
        if os.path.exists(self.configFilePath):
            return YAMLFileService.readDictData(self.configFilePath)
        return YAMLFileService.readDictData(self.sampleCfgFilePath)