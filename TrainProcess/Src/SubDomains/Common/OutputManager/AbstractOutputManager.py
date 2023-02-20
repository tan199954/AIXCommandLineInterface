import os
from typing import List
from abc import abstractclassmethod,abstractproperty, ABC
from PySide6 import QtCore

class AbstractOutputManager(ABC):
    OUTPUT_DIR_NAME="Output"
    @abstractclassmethod
    def isLastModelExist()->bool:
        pass
    @abstractclassmethod
    def getLastModelPath()->str:
        pass
    @staticmethod
    def getOutputDirPath()->str:
        currentPath = os.getcwd()
        return os.path.join(currentPath,AbstractOutputManager.OUTPUT_DIR_NAME)

class AbstractYOLOOutputManager(AbstractOutputManager):
    MODEL_DIR_NAME="weights"
    LAST_MODEL_FILE_NAME="last.pt"
    @abstractproperty
    def TRAIN_DIR_NAME(self)->str:
        pass
    def getLastModelPath(self)->str:
        entries = self.__getScandirInterator()
        sortedEntries = sorted(entries, key=lambda entry: entry.stat().st_mtime, reverse=True)
        subDirsSorted = [sub.path for sub in sortedEntries if sub.is_dir()]
        for DirPath in subDirsSorted:
            modelDirPath = os.path.join(DirPath,self.MODEL_DIR_NAME)
            lastModelFilePath=os.path.join(modelDirPath,self.LAST_MODEL_FILE_NAME)
            if os.path.exists(lastModelFilePath):
                return lastModelFilePath
        raise FileNotFoundError("could not find last.pt File, "
                                "check last model exist with method 'isLastModelExist()'")
    def isLastModelExist(self)->bool:
        subTrainDirPath=self.__getSubTrainDirPaths()
        for DirPath in subTrainDirPath:
            modelDirPath = os.path.join(DirPath,self.MODEL_DIR_NAME)
            lastModelFilePath=os.path.join(modelDirPath,self.LAST_MODEL_FILE_NAME)
            if os.path.exists(lastModelFilePath):
                return True
        return False
    def __getScandirInterator(self):
        outputPath=AbstractOutputManager.getOutputDirPath()
        trainDirName=self.TRAIN_DIR_NAME
        trainDirPath=os.path.join(outputPath,trainDirName)
        if os.path.exists(trainDirPath):
            return os.scandir(trainDirPath)
        return list()
    def __getSubTrainDirPaths(self)->List[str]:
        entries = self.__getScandirInterator()
        return [sub.path for sub in entries if sub.is_dir()]