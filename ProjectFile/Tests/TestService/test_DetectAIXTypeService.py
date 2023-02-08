import os
import sys
currentFilePath=os.path.abspath(__file__)
testServicePath=os.path.dirname(currentFilePath)
testsPath=os.path.dirname(testServicePath)
modulePath=os.path.dirname(testsPath)
parentPath=os.path.dirname(modulePath)
sys.path.append(parentPath)

import unittest
from ProjectFile.Src.Service.DetectAIXTypeService.DetectAIXTypeService import DetectAIXTypeService
from ProjectFile.Src.Core.Models.AIXProjInfoAggregate.AIXEnum import AIXType
class TestDetectAIXTypeService(unittest.TestCase):
    def testDetectAIXTypeService(self):
        labelPath=os.path.join(testsPath,"segLabelPath")
        aixType=DetectAIXTypeService.getAIXType(labelPath)
        self.assertEqual(aixType,AIXType.Segment)


if __name__=="__main__":
     unittest.main()