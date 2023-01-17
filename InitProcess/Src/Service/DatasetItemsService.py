import os, glob
from typing import List
from PySide6 import QtCore
from InitProcess.Src.Core import DatasetItem

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

class DatasetItemsService:
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

    def getTxtFilePath(self,imageFilePath):
        txtFilePath = self.labelPath + "/" + QtCore.QFileInfo(imageFilePath).baseName() + ".txt"
        return txtFilePath

    def getDatasetItems(self)->List[DatasetItem]:
        imageFilePaths=self.getImageFilePaths()
        datasetItems = list()
        for imageFilePath in imageFilePaths:
            txtFilePath=self.getTxtFilePath(imageFilePath)
            if(DatasetItemIO.isCompatible(imageFilePath,txtFilePath)):
                datasetItems.append(DatasetItem(imageFilePath,txtFilePath))
        return datasetItems