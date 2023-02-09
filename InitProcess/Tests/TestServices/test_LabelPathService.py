import os
import sys
currentFilePath=os.path.abspath(__file__)
testServicesPath=os.path.dirname(currentFilePath)
testsPath=os.path.dirname(testServicesPath)
modulePath=os.path.dirname(testsPath)
parentPath=os.path.dirname(modulePath)
sys.path.append(parentPath)

import unittest
from InitProcess.Src.Service.LabelPathService.YOROLabelPathService import YOROLabelPathService
from InitProcess.Src.Service.LabelPathService.YOLOLabelPathService import YOLOLabelPathService


class TestYoloLabelPathService(unittest.TestCase):
    def testYoloLabelPathService(self):
        imageFilePath=os.path.join(testsPath,r"imagePath\\test.jpg")
        boxLabelPath=os.path.join(testsPath,r"boxLabelPath")
        labelFilePath=os.path.join(boxLabelPath,r"test.txt")
        labelFilePatthFrService=YOLOLabelPathService.getLabelFilePathFrImageFilePath(boxLabelPath,imageFilePath)
        self.assertEqual(labelFilePatthFrService,labelFilePath)
class TestYoroLabelPathService(unittest.TestCase):
    def testYoroLabelPathService(self):
        imageFilePath=os.path.join(testsPath,r"imagePath\\test.jpg")
        boxLabelPath=os.path.join(testsPath,r"bbLabelPath")
        labelFilePath=os.path.join(boxLabelPath,r"test.jpg.mark")
        labelFilePatthFrService=YOROLabelPathService.getLabelFilePathFrImageFilePath(boxLabelPath,imageFilePath)
        self.assertEqual(labelFilePatthFrService,labelFilePath)
if __name__=="__main__":
     unittest.main()