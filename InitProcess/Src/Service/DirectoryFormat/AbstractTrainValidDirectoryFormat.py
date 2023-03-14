from abc import abstractmethod
import os
from InitProcess.Src.Service.Interfaces.IDatasetDirectoryFormat import IDatasetDirectoryFormat
class AbstractTrainValidDirectoryFormat(IDatasetDirectoryFormat):
    DATASET_DIR_NAME="Dataset"
    def __init__(self) -> None:
        super().__init__()
        currentPath = os.getcwd()
        self.datasetPath=os.path.join(currentPath,self.DATASET_DIR_NAME)
    @property
    @abstractmethod
    def trainImagePath(self)->str:
        pass
    @property
    @abstractmethod
    def validImagePath(self)->str:
        pass
    @property
    @abstractmethod
    def trainLabelPath(self)->str:
        pass
    @property
    @abstractmethod
    def validLabelPath(self)->str:
        pass
    