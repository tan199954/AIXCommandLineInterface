import os
import sys
currentFilePath=os.path.abspath(__file__)
testServicePath=os.path.dirname(currentFilePath)
testsPath=os.path.dirname(testServicePath)
modulePath=os.path.dirname(testsPath)
parentPath=os.path.dirname(modulePath)
sys.path.append(parentPath)

import unittest
from ProjectFile.Src.Service.AIXProjInfoBuilder.DatasetPathChecker import DatasetPathChecker
from ProjectFile.Src.Core.Models.AIXProjInfoAggregate.AIXEnum import AIXType
class TestDatasetPathChecker(unittest.TestCase):
    def testDetectAIXTypeService(self):
        labelPath=os.path.join(testsPath,"segLabelPath")
        imagePath=os.path.join(testsPath,"imagePath")
        DatasetPathChecker.checkImagePath(imagePath)
        DatasetPathChecker.checkLabelPath(labelPath)
        DatasetPathChecker.checkLabelPath(labelPath,AIXType.Segment)


if __name__=="__main__":
     unittest.main()