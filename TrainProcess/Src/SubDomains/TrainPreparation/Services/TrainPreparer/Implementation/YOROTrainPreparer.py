from typing import List
import os
from .AbstractTrainPreparer import AbstractTrainPreparer
from ...ConfigDataService.YOROCfgDataService import YOROCfgDataService
from .....Common.YAMLFileService.YAMLFileService import YAMLFileService
from .....Common.YOROConfigFile.YOROConfigFile import YOROConfigFile

class YOROTrainPreparer(AbstractTrainPreparer):
    NAMES_FILE_NAME="names.names"
    def __init__(self, gpuMenmory: int = None, trainPath: str = None, validPath: str = None,
                nameObjects: List[str] = None) -> None:
        super().__init__(gpuMenmory, trainPath, validPath, nameObjects)
        self.namesFilePath=os.path.join(self.outputDirPath,self.NAMES_FILE_NAME) 
    def _createConfigFile(self):
        if not YOROConfigFile.isExist():
            YOROConfigFile.createSampleFile()
        yOROCfgDataService=YOROCfgDataService(self.gpuMenmory,self.trainPath,self.validPath,
                                            self.namesFilePath)
        newConfigData=yOROCfgDataService.getNewConfigData()
        YOROConfigFile.updateData(newConfigData)
    def _createNamesFile(self):
        YAMLFileService.writeDictData(self.namesFilePath,self.nameObjects)
    def prepare(self):
        self._createNamesFile()
        self._createConfigFile()
