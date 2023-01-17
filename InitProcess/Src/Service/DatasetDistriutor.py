from typing import List
import os
from InitProcess.Src.Core import DatasetItem

class DatasetDistributor:
    MINIMUN_OF_DATASET=2
    REQUIREMENT_MINIMUM_OF_DATASET=4
    MAX_PERCENT=100
    MAX_VALID_PERCENT=50
    MAX_COUNTER=1
    def __init__(self,datasetItems:List[DatasetItem],imagesTrainPath:str,
        imagesValidPath:str,labelsTrainPath:str,labelsValidPath:str) -> None:
        self.datasetItems=datasetItems
        self.imagesTrainPath=imagesTrainPath
        self.imagesValidPath=imagesValidPath
        self.labelsTrainPath=labelsTrainPath
        self.labelsValidPath=labelsValidPath
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
        validTrainRatio=validPercent/(self.MAX_PERCENT-validPercent)
        counter=validTrainRatio
        for datasetItem in self.datasetItems:
            counter=counter+validTrainRatio
            if counter <=self.MAX_COUNTER:
                self.trainDistribute(datasetItem)
            else:
                self.validDistribute(datasetItem)
                counter=validTrainRatio
    def validDistribute(self,datasetItem:DatasetItem):
        labelName = os.path.basename(datasetItem.getlabelPath())
        imageName = os.path.basename(datasetItem.getImagePath())
        newLabelPath = os.path.join(self.labelsValidPath,labelName)
        newImagePath = os.path.join(self.imagesValidPath,imageName)
        os.rename(datasetItem.getlabelPath(),newLabelPath)
        os.rename(datasetItem.getImagePath(),newImagePath)
    def trainDistribute(self,datasetItem:DatasetItem):
        labelName = os.path.basename(datasetItem.getlabelPath())
        imageName = os.path.basename(datasetItem.getImagePath())
        newLabelPath = os.path.join(self.labelsTrainPath,labelName)
        newImagePath = os.path.join(self.imagesTrainPath,imageName)
        os.rename(datasetItem.getlabelPath(),newLabelPath)
        os.rename(datasetItem.getImagePath(),newImagePath)
