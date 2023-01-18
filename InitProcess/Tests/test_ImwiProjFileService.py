import os
import sys
currentFilePath=os.path.abspath(__file__)
testsPath=os.path.dirname(currentFilePath)
modulePath=os.path.dirname(testsPath)
parentPath=os.path.dirname(modulePath)
sys.path.append(parentPath)

import unittest

from InitProcess.Src.Service.ImwiProjFileService import ImwiProjFileService
from InitProcess.Src.Core import TrainType

class TestImwiProjFileService(unittest.TestCase):
     def __init__(self, methodName: str = ...) -> None:
          super().__init__(methodName)
          self.imwiProjFileService = ImwiProjFileService("d:/image","d:laebl",TrainType.Segment)
     def testWriteRoot(self):
          self.imwiProjFileService.writeRoot()
     def testWriteDataset(self):
          dataset={"trainPath":"hehe",
                   "validPah":"hihi",
                   "outputPath":"haha",
                   "modelFilePath":"huhu"}
          self.imwiProjFileService.writeDataset(dataset)
if __name__=="__main__":
     unittest.main()