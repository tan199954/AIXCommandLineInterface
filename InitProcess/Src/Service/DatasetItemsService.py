import os, glob
from typing import List
from abc import ABC, abstractclassmethod
from PySide6 import QtCore
from InitProcess.Src.Core import DatasetItem, AbstractLabelPathService

class ImageIO:
    VALID_IMAGES = [".jpg",".png",".bmp"]
    def __init__(self,fullPath):
        self.fullPath=fullPath

    def isFolder(self):
        return os.path.isdir(self.fullPath)

    def isImage(self):
        ext = os.path.splitext(self.fullPath)[1]
        if ext.lower() not in self.VALID_IMAGES:
            return False
        return True
class DatasetItemIO:
    def isCompatible(imagePath,labelPath):
        if os.path.exists(imagePath) and os.path.exists(labelPath):
            return True
        return False

class YoloLabelPathService(AbstractLabelPathService):
    YOLO_LABEL_FORMAT=".txt"
    def getLabelFilePath(self):
        labelFilePath = self.labelPath + "/" + QtCore.QFileInfo(self.imageFilePath).baseName() + self.YOLO_LABEL_FORMAT
        return labelFilePath
class YoroLabelPathService(AbstractLabelPathService):
    YORO_LABEL_FORMAT=".mark"
    def getLabelFilePath(self):
        labelFilePath = self.labelPath + "/" + QtCore.QFileInfo(self.imageFilePath).fileName() + self.YORO_LABEL_FORMAT
        return labelFilePath

class DatasetItemsService(ABC):
    def __init__(self,imgPath=None,labelPath=None):
        self.imgPath = imgPath
        self.labelPath=labelPath
    def getImageFilePaths(self):
        listImageFilePaths=list()
        def getImageFilePathInfoler(imageFolerPath):
            items = glob.glob(imageFolerPath +"/*")
            for item in items:
                item = ImageIO(item)
                if item.isFolder():
                    getImageFilePathInfoler(item.fullPath)
                if item.isImage():
                    listImageFilePaths.append(item.fullPath)        
        getImageFilePathInfoler(self.imgPath)
        return listImageFilePaths

    def getLabelFilePath(self,imageFilePath)->str:
        labelPathService = self.getLabelPathService(imageFilePath)
        return labelPathService.getLabelFilePath()
    def getDatasetItems(self)->List[DatasetItem]:
        imageFilePaths=self.getImageFilePaths()
        datasetItems = list()
        for imageFilePath in imageFilePaths:
            labelFilePath=self.getLabelFilePath(imageFilePath)
            if(DatasetItemIO.isCompatible(imageFilePath,labelFilePath)):
                datasetItems.append(DatasetItem(imageFilePath,labelFilePath))
        return datasetItems
    @abstractclassmethod
    def getLabelPathService(self,imageFilePath)->AbstractLabelPathService:
        pass
class YoloDatasetItemsService(DatasetItemsService):
    def getLabelPathService(self,imageFilePath)->AbstractLabelPathService:
        return YoloLabelPathService(imageFilePath,self.labelPath)
class YoroDatasetItemsService(DatasetItemsService):
    def getLabelPathService(self,imageFilePath)->AbstractLabelPathService:
        return YoroLabelPathService(imageFilePath,self.labelPath)