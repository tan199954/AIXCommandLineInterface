import os
import sys
currentFilePath=os.path.abspath(__file__)
testTrainPreparationPath=os.path.dirname(currentFilePath)
testsPath=os.path.dirname(testTrainPreparationPath)
modulePath=os.path.dirname(testsPath)
parentPath=os.path.dirname(modulePath)
sys.path.append(parentPath)
import unittest

from TrainProcess.Src.SubDomains.Training.Services.ModelInfoBuilder.Implementations.LossCoefficientFinder import SegLossCoefficientFinder,BoxLossCoefficientFinder

class TestSegLossCoefficientFinder(unittest.TestCase):
     def testGetLoss(self):
          lossCoefficientParser=SegLossCoefficientFinder()
          loss = lossCoefficientParser.getLossFrStr("1/3       1.5G      1.275      3.219      3.311      1.229        438        320:  33%|███▎      | 1/3 [00:10<00:21, 10.61s/it]")
          self.assertEqual(loss,1.229)
          loss = lossCoefficientParser.getLossFrStr("Epoch    GPU_mem   box_loss   seg_loss   cls_loss   dfl_loss  Instances       Size")
          self.assertEqual(loss,None)
class TestBoxLossCoefficientFinder(unittest.TestCase):
     def testGetLoss(self):
          lossCoefficientParser=BoxLossCoefficientFinder()
          loss = lossCoefficientParser.getLossFrStr("     3/3      1.17G      1.346      1.852       1.31        168        320:  50%|█████     | 4/8 [00:04<00:03,  1.15it/s]")
          self.assertEqual(loss,1.31)
          loss = lossCoefficientParser.getLossFrStr("Epoch    GPU_mem   box_loss   seg_loss   cls_loss   dfl_loss  Instances       Size")
          self.assertEqual(loss,None)

if __name__ == "__main__":
    unittest.main()