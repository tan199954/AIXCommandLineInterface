from typing import List
import os
from .AbstractTrainPreparer import AbstractTrainPreparer
from ...ConfigDataService.YOROCfgDataService import YOROCfgDataService
from ...YAMLFileService.YAMLFileService import YAMLFileService

class YOROTrainPreparer(AbstractTrainPreparer):
    NAMES_FILE_NAME="names.names"
    CONFIG_FILE_NAME="cfg.yaml"
    def __init__(self, gpuMenmory: int = None, trainPath: str = None, validPath: str = None,
                nameObjects: List[str] = None) -> None:
        super().__init__(gpuMenmory, trainPath, validPath, nameObjects)
        self.namesFilePath=os.path.join(self.outputDirPath,self.NAMES_FILE_NAME)
        self.configFilePath=os.path.join(self.outputDirPath,self.CONFIG_FILE_NAME)
        self.changeLearningRate=False 
    def _createCofigFile(self):
        yOROCfgDataService=YOROCfgDataService(self.gpuMenmory,self.trainPath,self.validPath,
                                        self.configFilePath,self.namesFilePath)
        newCofigData=yOROCfgDataService.getNewConfigData()
        YAMLFileService.writeDictData(self.configFilePath,newCofigData)
    def _createNamesFile(self):
        YAMLFileService.writeDictData(self.namesFilePath,self.nameObjects)
    def prepare(self):
        self._createNamesFile()
        self._createCofigFile()
