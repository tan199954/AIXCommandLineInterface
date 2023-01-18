import os
import sys
currentFilePath=os.path.abspath(__file__)
testsPath=os.path.dirname(currentFilePath)
modulePath=os.path.dirname(testsPath)
parentPath=os.path.dirname(modulePath)
sys.path.append(parentPath)

import unittest

from InitProcess.Src.Service.DatasetDistriutor import DatasetDistributor
from InitProcess.Src.Service.DatasetItemsService import YoloDatasetItemsService
from InitProcess.Src.Core import DatasetItem

class TestDatasetDistributor(unittest.TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        self.trainPath = os.path.join(testsPath,"train")
        self.validPath = os.path.join(testsPath,"valid")
        imagePath=os.path.join(testsPath,"imagePath")
        labelPath=os.path.join(testsPath,"boxLabelPath")
        yoloDatasetItemsService=YoloDatasetItemsService(imagePath,labelPath)
        datasetItems=yoloDatasetItemsService.getDatasetItems()
        testImageFilePath = os.path.join(testsPath,r"imagePath\test.jpg")
        testLabelFilePath = os.path.join(testsPath,r"boxLabelPath\test.txt")
        self.datasetItem = DatasetItem(testImageFilePath,testLabelFilePath)
        self.datasetDistributor=DatasetDistributor(datasetItems,
                            self.trainPath,self.validPath,self.trainPath,self.validPath)
    def testTrainDistribute(self):
        newImageFilePath=os.path.join(self.trainPath,"test.jpg")
        newLabelFilePath=os.path.join(self.trainPath,"test.txt")
        self.datasetDistributor.trainDistribute(self.datasetItem)
        oldImageFileExists=os.path.exists(self.datasetItem.getImagePath())
        oldLabelFileExists=os.path.exists(self.datasetItem.getLabelPath())
        newImageFileExists=os.path.exists(newImageFilePath)
        newLabelFileExists=os.path.exists(newLabelFilePath)
        self.assertEqual(oldImageFileExists,True)
        self.assertEqual(oldLabelFileExists,True)
        self.assertEqual(newImageFileExists,True)
        self.assertEqual(newLabelFileExists,True)
    def testExecute(self):
        self.datasetDistributor.execute()
if __name__=="__main__":
     unittest.main()