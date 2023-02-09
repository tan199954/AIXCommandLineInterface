from abc import ABC,abstractclassmethod
from typing import List
from InitProcess.Src.Core.Interfaces.IDatasetItem import IDatasetItem
class IDatasetItemService(ABC):
    @abstractclassmethod
    def getDatasetItems(self)->List[IDatasetItem]:
        pass