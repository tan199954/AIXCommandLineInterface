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
    def imagesTrainPath(self)->str:
        pass
    @property
    @abstractmethod
    def imagesValidPath(self)->str:
        pass
    @property
    @abstractmethod
    def labelsTrainPath(self)->str:
        pass
    @property
    @abstractmethod
    def labelsValidPath(self)->str:
        pass
    