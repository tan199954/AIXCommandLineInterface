import os
from typing import List
from .AbstractTrainPreparer import AbstractTrainPreparer
from .....Common.PathConverter.PathConverter import PathConverter
from .....Common.YAMLFileService.YAMLFileService import YAMLFileService

class YOLOTrainPreparer(AbstractTrainPreparer):
    DATA_FILE_NAME="data.yaml"
    def __init__(self, gpuMenmory: int = None, trainPath: str = None, validPath: str = None, nameObjects: List[str] = None) -> None:
        super().__init__(gpuMenmory, trainPath, validPath, nameObjects)
        self.dataFilePath=os.path.join(self.outputDirPath,self.DATA_FILE_NAME)
    def prepare(self):
        self._creataDataYamlFile()
    def _creataDataYamlFile(self):
        data=self._getYamlData()
        YAMLFileService.writeDictData(self.dataFilePath,data)
    def _getYamlData(self):
        return {
            "train":PathConverter.Windows2WSL(self.trainPath),  
            "val": PathConverter.Windows2WSL(self.validPath),  
            "test": None,
            "names":self._getDictionaryNames()
        }
    def _getDictionaryNames(self)->dict:
        dictNames={}
        for id,name in enumerate(self.nameObjects):
            dictNames[id]=name
        return dictNames
