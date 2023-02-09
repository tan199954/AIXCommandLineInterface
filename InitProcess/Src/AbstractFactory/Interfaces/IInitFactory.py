from abc import ABC,abstractclassmethod
from typing import List
from InitProcess.Src.Service.Interfaces.IDatasetDistributor import IDatasetDistributor
from InitProcess.Src.Service.Interfaces.IDatasetItemService import IDatasetItemService
from InitProcess.Src.Core.Models.DatasetItem import ImageDatasetItem
class IInitFactory(ABC):
    @abstractclassmethod
    def createDatasetDistributor(self,imageDatasetItems:List[ImageDatasetItem])->IDatasetDistributor:
        pass
    @abstractclassmethod
    def createDatasetItemService(self,imagePath,labelPath)->IDatasetItemService:
        pass