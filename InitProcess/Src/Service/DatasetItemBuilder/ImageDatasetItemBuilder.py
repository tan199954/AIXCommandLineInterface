from InitProcess.Src.Core.Models.DatasetItem import ImageDatasetItem
from InitProcess.Src.Service.DatasetItemBuilder.DatasetItemChecker import DatasetFilePathChecker
class ImageDatasetItemBuilder:
    def __init__(self) -> None:
        self.imageDatasetItem=ImageDatasetItem()
    def setImageFilePath(self,imageFilePath:str)->"ImageDatasetItemBuilder":
        DatasetFilePathChecker.checkImageFilePath(imageFilePath)
        self.imageDatasetItem.imageFilePath=imageFilePath
        return self
    def setLabelFilePath(self,labelFilePath:str)->"ImageDatasetItemBuilder":
        DatasetFilePathChecker.checkLabelFilePath(labelFilePath)
        self.imageDatasetItem.labelFilePath=labelFilePath
        return self
    def build(self)->ImageDatasetItem:
        return self.imageDatasetItem