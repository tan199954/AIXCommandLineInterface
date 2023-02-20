import os
import sys
currentFilePath=os.path.abspath(__file__)
testTrainPreparationPath=os.path.dirname(currentFilePath)
testsPath=os.path.dirname(testTrainPreparationPath)
modulePath=os.path.dirname(testsPath)
parentPath=os.path.dirname(modulePath)
sys.path.append(parentPath)
import unittest

from TrainProcess.Src.SubDomains.Common.OutputManager.SegOutputManager import SegOutputManager

class TestSegOutputManager(unittest.TestCase):
     def testGetOutputDirPath(self):
        outputDir = os.path.join(testsPath,"Output")
        outputDir1=SegOutputManager.getOutputDirPath()
        self.assertEqual(outputDir1,outputDir)
     def testIsLastModelExist(self):
          lastModelExist=SegOutputManager().isLastModelExist()
          self.assertEqual(lastModelExist,True)
     def testGetLastModelPath(self):
          lastModelPath = os.path.join(testsPath,r"Output\runs\segment\train15\weights\last.pt")
          lastModelPath1=SegOutputManager().getLastModelPath()
          self.assertEqual(lastModelPath,lastModelPath1)

if __name__ == "__main__":
    unittest.main()