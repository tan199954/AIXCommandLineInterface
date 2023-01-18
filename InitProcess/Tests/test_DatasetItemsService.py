import os
import sys
currentFilePath=os.path.abspath(__file__)
testsPath=os.path.dirname(currentFilePath)
modulePath=os.path.dirname(testsPath)
parentPath=os.path.dirname(modulePath)
sys.path.append(parentPath)

import unittest

from InitProcess.Src.Service.DatasetItemsService import YoroDatasetItemsService, YoloDatasetItemsService

class TestYoloLabelPathService(unittest.TestCase):
    def testYoloLabelPathService(self):
        imagePath = os.path.join(testsPath,"imagePath")
        yoloLabelPath = os.path.join(testsPath,"boxLabelPath")
        yoloDatasetItemsService=YoloDatasetItemsService(imagePath,yoloLabelPath)
        yoloDatasetItetms=yoloDatasetItemsService.getDatasetItems()
        testImagePath=os.path.join(testsPath,r"imagePath\test.jpg")
        testLabelPath = os.path.join(testsPath,r"boxLabelPath\test.txt")
        self.assertEqual(testImagePath,yoloDatasetItetms[0].getImagePath())
        self.assertEqual(testLabelPath,yoloDatasetItetms[0].getLabelPath())
class TestYoroLabelPathService(unittest.TestCase):
    def testYoroLabelPathService(self):
        imagePath = os.path.join(testsPath,"imagePath")
        yoroLabelPath = os.path.join(testsPath,"bbLabelPath")
        yoroDatasetItemsService=YoroDatasetItemsService(imagePath,yoroLabelPath)
        yoroDatasetItetms=yoroDatasetItemsService.getDatasetItems()
        testImagePath=os.path.join(testsPath,r"imagePath\test.jpg")
        self.assertEqual(testImagePath,yoroDatasetItetms[0].getImagePath())
        testLabelPath = os.path.join(testsPath,r"bbLabelPath\test.jpg.mark")
        self.assertEqual(testLabelPath,yoroDatasetItetms[0].getLabelPath())
if __name__=="__main__":
     unittest.main()