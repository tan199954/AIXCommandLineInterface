import os
import sys
currentFilePath=os.path.abspath(__file__)
testServicesPath=os.path.dirname(currentFilePath)
testsPath=os.path.dirname(testServicesPath)
modulePath=os.path.dirname(testsPath)
parentPath=os.path.dirname(modulePath)
sys.path.append(parentPath)

import unittest
from InitProcess.Src.Service.DatasetItemsService.YOLODatasetItemsService import YOLODatasetItemsService
from InitProcess.Src.Service.DatasetItemsService.YORODatasetItemsService import YORODatasetItemsService
from InitProcess.Src.Core.Models.DatasetItem import ImageDatasetItem

class TestYOLODatasetItemsService(unittest.TestCase):
    def testYOLODatasetItemsService(self):
        imagePath=os.path.join(testsPath,r"imagePath")
        labelPath=os.path.join(testsPath,r"segLabelPath")
        imageFilePath=os.path.join(testsPath,r"imagePath\\test.jpg")
        labelFilePath=os.path.join(testsPath,r"segLabelPath\\test.txt")
        datasetItem=ImageDatasetItem(imageFilePath,labelFilePath)

        yOLODatasetItemsService=YOLODatasetItemsService(imagePath,labelPath)
        dataseItems=yOLODatasetItemsService.getDatasetItems()
        # self.assertEqual(dataseItems[0].__dict__,datasetItem.__dict__)
        print(dataseItems[0].labelFilePath)
        print(datasetItem.labelFilePath)
class TestYORODatasetItemsService(unittest.TestCase):
    def testYORODatasetItemsService(self):
        imagePath=os.path.join(testsPath,r"imagePath")
        labelPath=os.path.join(testsPath,r"bbLabelPath")
        imageFilePath=os.path.join(testsPath,r"imagePath\\test.jpg")
        labelFilePath=os.path.join(testsPath,r"bbLabelPath\\test.jpg.mark")
        datasetItem=ImageDatasetItem(imageFilePath,labelFilePath)

        yORODatasetItemsService=YORODatasetItemsService(imagePath,labelPath)
        dataseItems=yORODatasetItemsService.getDatasetItems()
        # self.assertEqual(dataseItems[2].__dict__,datasetItem.__dict__)
        print(dataseItems[2].imageFilePath)
        print(datasetItem.imageFilePath)
if __name__=="__main__":
     unittest.main()