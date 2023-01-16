import os
import sys
currentFilePath=os.path.abspath(__file__)
testsPath=os.path.dirname(currentFilePath)
modulePath=os.path.dirname(testsPath)
parentPath=os.path.dirname(modulePath)
sys.path.append(parentPath)

import unittest

from InitProcess.Src.Infrastructure.ImplProjInputChecker import BBoxProjInputChecker,BoxProjInputChecker,SegProjInputChecker

class TestProjInputChecker(unittest.TestCase):
     def __init__(self, methodName: str = ...) -> None:
          super().__init__(methodName)
          imagePath = os.path.join(testsPath,"imagePath")
          segLabelPath=os.path.join(testsPath,"segLabelPath")
          boxLabelPath=os.path.join(testsPath,"boxLabelPath")
          bboxLabelPath=os.path.join(testsPath,"bbLabelPath")
          self.segProjInputChecker = SegProjInputChecker(imagePath,segLabelPath)
          self.boxProjInputChecker=BoxProjInputChecker(imagePath,boxLabelPath)
          self.bboxProjInputChecker=BBoxProjInputChecker(imagePath,bboxLabelPath)
     def testCheck(self):
          self.segProjInputChecker.check()
          self.boxProjInputChecker.check()
          self.bboxProjInputChecker.check()

if __name__=="__main__":
     unittest.main()