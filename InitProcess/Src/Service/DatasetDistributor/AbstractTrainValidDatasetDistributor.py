from typing import List
from abc import abstractclassmethod
import os
import shutil
import cv2
from InitProcess.Src.Service.Interfaces.IDatasetDistributor import IDatasetDistributor
from InitProcess.Src.Service.DirectoryFormat.AbstractTrainValidDirectoryFormat import AbstractTrainValidDirectoryFormat
from InitProcess.Src.Core.Models.DatasetItem import ImageDatasetItem
from InitProcess.Src.Service.Interfaces.IImageResizer import IImageResizer


class AbstractTrainValidDatasetDistributor(IDatasetDistributor):
    MINIMUN_OF_DATASET=2
    REQUIREMENT_MINIMUM_OF_DATASET=4
    MAX_PERCENT=100
    MAX_VALID_PERCENT=50
    MAX_COUNTER=1
    def __init__(self,datasetItems:List[ImageDatasetItem]) -> None:
        self.datasetItems=datasetItems
        trainValidDatasetDirectoryFormat=self.getDatasetDirectoryFormat()
        self.imagesTrainPath=trainValidDatasetDirectoryFormat.trainImagePath
        self.imagesValidPath=trainValidDatasetDirectoryFormat.validImagePath
        self.labelsTrainPath=trainValidDatasetDirectoryFormat.trainLabelPath
        self.labelsValidPath=trainValidDatasetDirectoryFormat.validLabelPath
    @abstractclassmethod
    def getDatasetDirectoryFormat(self)->AbstractTrainValidDirectoryFormat:
        pass
    @abstractclassmethod
    def getImageResizer(self,imageFilePath:str)->IImageResizer:
        pass
    def execute(self):
        if not self.datasetItems or len(self.datasetItems) <self.MINIMUN_OF_DATASET:
            raise Exception("DatasetItems is not enought for the training\n"
                            "Please create more datasetItems")
        if len(self.datasetItems)==self.MINIMUN_OF_DATASET:
            self.distribute(50)
        elif len(self.datasetItems)<self.REQUIREMENT_MINIMUM_OF_DATASET:
            self.distribute(33.33)
        else: 
            self.distribute(25)
    def distribute(self,validPercent:float):
        if validPercent > self.MAX_VALID_PERCENT:
            raise Exception("validPercent must be equal or smaller than 50%")
        validTrainRatio=validPercent/(self.MAX_PERCENT)
        counter=validTrainRatio
        for datasetItem in self.datasetItems:
            counter=counter+validTrainRatio
            if counter <=self.MAX_COUNTER:
                self.trainDistribute(datasetItem)
            else:
                self.validDistribute(datasetItem)
                counter=validTrainRatio
    def validDistribute(self,datasetItem:ImageDatasetItem):
        labelName = os.path.basename(datasetItem.labelFilePath)
        imageName = os.path.basename(datasetItem.imageFilePath)
        newLabelPath = os.path.join(self.labelsValidPath,labelName)
        newImagePath = os.path.join(self.imagesValidPath,imageName)
        newImage=self.getImageResizer(datasetItem.imageFilePath).getResizedImage()
        shutil.copy(datasetItem.labelFilePath,newLabelPath)
        cv2.imwrite(newImagePath,newImage)
    def trainDistribute(self,datasetItem:ImageDatasetItem):
        labelName = os.path.basename(datasetItem.labelFilePath)
        imageName = os.path.basename(datasetItem.imageFilePath)
        newLabelPath = os.path.join(self.labelsTrainPath,labelName)
        newImagePath = os.path.join(self.imagesTrainPath,imageName)
        newImage=self.getImageResizer(datasetItem.imageFilePath).getResizedImage()
        shutil.copy(datasetItem.labelFilePath,newLabelPath)
        cv2.imwrite(newImagePath,newImage)

