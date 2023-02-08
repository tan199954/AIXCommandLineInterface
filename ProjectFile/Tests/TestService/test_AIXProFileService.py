import os
import sys
currentFilePath=os.path.abspath(__file__)
testServicePath=os.path.dirname(currentFilePath)
testsPath=os.path.dirname(testServicePath)
modulePath=os.path.dirname(testsPath)
parentPath=os.path.dirname(modulePath)
sys.path.append(parentPath)

import unittest
from ProjectFile.Src.Service.ProjectFileService.AIXProjFileService import AIXProjFileService

class TestAIXProjFileService(unittest.TestCase):
    def testWriteAndRead(self):
        aIXProjFileService=AIXProjFileService()
        writeData={"TEST":"test"}
        aIXProjFileService.writeProjFile(writeData)
        readData=aIXProjFileService.readProjFile()
        self.assertEqual(readData,writeData)
    def testExist(self):
        aIXProjFileService=AIXProjFileService()
        exist=aIXProjFileService.isExist()
        self.assertEqual(exist,True)
    
if __name__=="__main__":
     unittest.main()