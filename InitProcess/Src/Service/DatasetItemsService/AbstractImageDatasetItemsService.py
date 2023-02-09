from typing import List
from abc import ABC, abstractclassmethod
from PySide6 import QtCore
from InitProcess.Src.Core.Models.DatasetItem import ImageDatasetItem
from InitProcess.Src.Service.Interfaces.ILabelPathService import ILabelPathService
from InitProcess.Src.Service.DatasetItemBuilder.ImageDatasetItemBuilder import ImageDatasetItemBuilder

class AbstractImageDatasetItemsService(ABC):
    IMAGE_FILTERS=["*png","*jpg","*bmp"]
    def __init__(self,imgPath=None,labelPath=None):
        self.imagePath = imgPath
        self.labelPath=labelPath
    @abstractclassmethod
    def getLabelPathService(self)->ILabelPathService:
        pass
    def getImageFilePaths(self):
        if not QtCore.QDir(self.imagePath).exists():
            raise Exception(f"{self.imagePath} is not exists")
        fileInfos= QtCore.QDir(self.imagePath).entryInfoList(self.IMAGE_FILTERS, QtCore.QDir.Files|QtCore.QDir.NoDotAndDotDot)
        return [fileInfo.filePath() for fileInfo in fileInfos]
    def getDatasetItems(self)->List[ImageDatasetItem]:
        imageFilePaths=self.getImageFilePaths()
        datasetItems = list()
        for imageFilePath in imageFilePaths:
            labelFilePath=self.getLabelPathService(
                ).getLabelFilePathFrImageFilePath(self.labelPath,imageFilePath)
            try:
                imageDatasetItem=ImageDatasetItemBuilder(
                ).setImageFilePath(imageFilePath).setLabelFilePath(labelFilePath
                ).build()
                datasetItems.append(imageDatasetItem)
            except:
                pass
        return datasetItems