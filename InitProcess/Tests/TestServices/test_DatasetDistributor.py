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
from InitProcess.Src.Service.DatasetDistributor.YOLODatasetDistributor import YOLODatasetDistributor
from InitProcess.Src.Service.DatasetDistributor.YORODatasetDistributor import YORODatasetDistributor


class TestYOLODatasetItemsService(unittest.TestCase):
    def testYOLODatasetItemsService(self):
        imagePath=os.path.join(testsPath,r"imagePath")
        labelPath=os.path.join(testsPath,r"boxLabelPath")
        yOLODatasetItemsService=YOLODatasetItemsService(imagePath,labelPath)
        dataseItems=yOLODatasetItemsService.getDatasetItems()
        yOLODatasetDistributor=YOLODatasetDistributor(dataseItems)
        yOLODatasetDistributor.execute()

class TestYORODatasetItemsService(unittest.TestCase):
    def testYORODatasetItemsService(self):
        imagePath=os.path.join(testsPath,r"imagePath")
        labelPath=os.path.join(testsPath,r"bbLabelPath")
        yORODatasetItemsService=YORODatasetItemsService(imagePath,labelPath)
        dataseItems=yORODatasetItemsService.getDatasetItems()
        yORODatasetDistributor=YORODatasetDistributor(dataseItems)
        yORODatasetDistributor.execute()


if __name__=="__main__":
     unittest.main()