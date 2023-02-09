from typing import List
from InitProcess.Src.Core.Models.DatasetItem import ImageDatasetItem

from InitProcess.Src.AbstractFactory.Interfaces.IInitFactory import IInitFactory
from InitProcess.Src.Service.DatasetDistributor.YOLODatasetDistributor import YOLODatasetDistributor
from InitProcess.Src.Service.Interfaces.IDatasetDistributor import IDatasetDistributor
from InitProcess.Src.Service.DatasetItemsService.YOLODatasetItemsService import YOLODatasetItemsService
from InitProcess.Src.Service.Interfaces.IDatasetItemService import IDatasetItemService
class YOLOInitFactory(IInitFactory):
    def createDatasetDistributor(self,imageDatasetItems:List[ImageDatasetItem])->IDatasetDistributor:
        return YOLODatasetDistributor(imageDatasetItems)
    def createDatasetItemService(self,imagePath,labelPath)->IDatasetItemService:
        return YOLODatasetItemsService(imagePath,labelPath)