import os
import sys
currentFilePath=os.path.abspath(__file__)
testTrainPreparationPath=os.path.dirname(currentFilePath)
testsPath=os.path.dirname(testTrainPreparationPath)
modulePath=os.path.dirname(testsPath)
parentPath=os.path.dirname(modulePath)
sys.path.append(parentPath)
import unittest

from TrainProcess.Src.SubDomains.Training.Services.ModelInfoBuilder.Implementations.MAPCoefficientFinder import SegMAPCoefficientFinder, BoxMAPCoefficientFinder

class TestSegMAPCoefficientFinder(unittest.TestCase):
     def testGetMAPFromStr(self):
          mAP = SegMAPCoefficientFinder().getMAPFrStr("                    all         26        260     0.0339      0.742     0.0524     0.0303     0.0351      0.769     0.0569     0.0265")
          self.assertEqual(mAP,0.0265)     
class TestBoxMAPCoefficientFinder(unittest.TestCase):
     def testGetMAPFromStr(self):
          mAP = BoxMAPCoefficientFinder().getMAPFrStr("           all        128        929      0.595      0.495      0.519      0.373")
          self.assertEqual(mAP,0.373)    

if __name__ == "__main__":
    unittest.main()