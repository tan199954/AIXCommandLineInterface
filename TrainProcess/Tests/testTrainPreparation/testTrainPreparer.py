import os
import sys
currentFilePath=os.path.abspath(__file__)
testTrainPreparationPath=os.path.dirname(currentFilePath)
testsPath=os.path.dirname(testTrainPreparationPath)
modulePath=os.path.dirname(testsPath)
parentPath=os.path.dirname(modulePath)
sys.path.append(parentPath)
import unittest

from TrainProcess.Src.SubDomains.TrainPreparation.Services.TrainPreparer.Implementation.YOROTrainPreparer import YOROTrainPreparer
from TrainProcess.Src.SubDomains.TrainPreparation.Services.TrainPreparer.Implementation.YOLOTrainPreparer import YOLOTrainPreparer
class TestYOROCfgDataService(unittest.TestCase):
    def testGetNewConfigData(self):
        yOROTrainPreparer=YOROTrainPreparer(4000,"hehe","hihi",["haha","kaka"])
        yOROTrainPreparer.prepare(True)
class TestYOROCfgDataService(unittest.TestCase):
    def testGetNewConfigData(self):
        yOROTrainPreparer=YOLOTrainPreparer(4000,"hehe","hihi",["haha","kaka"])
        yOROTrainPreparer.prepare()
if __name__ == "__main__":
    unittest.main()