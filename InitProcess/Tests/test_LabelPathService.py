import os
import sys
currentFilePath=os.path.abspath(__file__)
testsPath=os.path.dirname(currentFilePath)
modulePath=os.path.dirname(testsPath)
parentPath=os.path.dirname(modulePath)
sys.path.append(parentPath)

import unittest

from InitProcess.Src.Service.DatasetItemsService import YoloLabelPathService, YoroLabelPathService

class TestYoloLabelPathService(unittest.TestCase):
    def testYoloLabelPathService(self):
        imageFilePath="d:/image/test.png"
        labelPath="d:/label"
        yoloLabelPathService=YoloLabelPathService(imageFilePath,labelPath)
        labelFilePath=yoloLabelPathService.getLabelFilePath()
        self.assertEqual("d:/label/test.txt",labelFilePath)
class TestYoroLabelPathService(unittest.TestCase):
    def testYoroLabelPathService(self):
        imageFilePath="d:/image/test.png"
        labelPath="d:/label"
        yoroLabelPathService=YoroLabelPathService(imageFilePath,labelPath)
        labelFilePath=yoroLabelPathService.getLabelFilePath()
        self.assertEqual("d:/label/test.png.mark",labelFilePath)
if __name__=="__main__":
     unittest.main()