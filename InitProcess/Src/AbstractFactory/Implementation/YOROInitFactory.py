from typing import List
from InitProcess.Src.Core.Models.DatasetItem import ImageDatasetItem

from InitProcess.Src.AbstractFactory.Interfaces.IInitFactory import IInitFactory
from InitProcess.Src.Service.DatasetDistributor.YORODatasetDistributor import YORODatasetDistributor
from InitProcess.Src.Service.Interfaces.IDatasetDistributor import IDatasetDistributor
from InitProcess.Src.Service.DatasetItemsService.YORODatasetItemsService import YORODatasetItemsService
from InitProcess.Src.Service.Interfaces.IDatasetItemService import IDatasetItemService
class YOROInitFactory(IInitFactory):
    def createDatasetDistributor(self,imageDatasetItems:List[ImageDatasetItem])->IDatasetDistributor:
        return YORODatasetDistributor(imageDatasetItems)
    def createDatasetItemService(self,imagePath,labelPath)->IDatasetItemService:
        return YORODatasetItemsService(imagePath,labelPath)