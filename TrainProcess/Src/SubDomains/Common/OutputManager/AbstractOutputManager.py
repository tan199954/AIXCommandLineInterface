import os
from typing import List
from abc import abstractclassmethod,abstractproperty, ABC

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
    BEST_MODEL_FILE_NAME="best.pt"
    @abstractproperty
    def TRAIN_DIR_NAME(self)->str:
        pass
    def __getModelPath(self,modelFilleName:str)->str:
        subTrainDirPaths=self.__getSubTrainDirPaths()
        for dirPath in subTrainDirPaths:
            modelDirPath = os.path.join(dirPath,self.MODEL_DIR_NAME)
            lastModelFilePath=os.path.join(modelDirPath,modelFilleName)
            if os.path.exists(lastModelFilePath):
                return lastModelFilePath
        raise FileNotFoundError(f"could not find {modelFilleName}, "
                                "check model exist with method 'isModelExist()'")
    def getLastModelPath(self)->str:
        return self.__getModelPath(self.LAST_MODEL_FILE_NAME)
    def getBestModelPath(self)->str:
        return self.__getModelPath(self.BEST_MODEL_FILE_NAME)
    def __isModelExist(self,modelFilleName:str)->bool:
        subTrainDirPaths=self.__getSubTrainDirPaths()
        for dirPath in subTrainDirPaths:
            modelDirPath = os.path.join(dirPath,self.MODEL_DIR_NAME)
            lastModelFilePath=os.path.join(modelDirPath,modelFilleName)
            if os.path.exists(lastModelFilePath):
                return True
        return False
    def isLastModelExist(self)->bool:
        return self.__isModelExist(self.LAST_MODEL_FILE_NAME)
    def isBestModelExist(self)->bool:
        return self.__isModelExist(self.BEST_MODEL_FILE_NAME)
    def __getScandirInterator(self):
        outputPath=AbstractOutputManager.getOutputDirPath()
        trainDirPath=os.path.join(outputPath,self.TRAIN_DIR_NAME)
        if os.path.exists(trainDirPath):
            return os.scandir(trainDirPath)
        return list()
    def __getSubTrainDirPaths(self)->List[str]:
        entries = self.__getScandirInterator()
        sortedEntries = sorted(entries, key=lambda entry: entry.stat().st_mtime, reverse=True)
        return [sub.path for sub in sortedEntries if sub.is_dir()]