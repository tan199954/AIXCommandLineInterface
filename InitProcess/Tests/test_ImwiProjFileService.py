import os
import sys
currentFilePath=os.path.abspath(__file__)
testsPath=os.path.dirname(currentFilePath)
modulePath=os.path.dirname(testsPath)
sys.path.append(modulePath)

import unittest

from InitProcess.Src.Service.ImwiProjFileService import ImwiProjFileService

class TestImwiProjFileService(unittest.TestCase):
     def __init__(self, methodName: str = ...) -> None:
          super().__init__(methodName)
          self.imwiProjFileService = ImwiProjFileService("d:/image","d:laebl","Seg")
     def testWriteRoot(self):
          self.imwiProjFileService.writeRoot()
if __name__=="__main__":
     unittest.main()