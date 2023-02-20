import os
import sys
currentFilePath=os.path.abspath(__file__)
testTrainPreparationPath=os.path.dirname(currentFilePath)
testsPath=os.path.dirname(testTrainPreparationPath)
modulePath=os.path.dirname(testsPath)
parentPath=os.path.dirname(modulePath)
sys.path.append(parentPath)
import unittest

from TrainProcess.Src.SubDomains.TrainPreparation.Factory.TrainPreparerFactory import (TrainPreparerFactory, TrainPreparationType,
                                                                                        YOLOTrainPreparer,YOROTrainPreparer)
class TestTrainPreparerFactory(unittest.TestCase):
    def testGetPreparer(self):
        YOLOPreparer=TrainPreparerFactory.createTrainPreparer(TrainPreparationType.YOLO)
        YOROPreparer=TrainPreparerFactory.createTrainPreparer(TrainPreparationType.YORO)
        self.assertEqual(YOLOPreparer.__dict__,YOLOTrainPreparer().__dict__)
        self.assertEqual(YOROPreparer.__dict__,YOROTrainPreparer().__dict__)
    def testGetNeWPreparer(self):
        YOLOPreparer=TrainPreparerFactory.createTrainPreparer(TrainPreparationType.YOLO)
        newYOLOPreparer=TrainPreparerFactory.createTrainPreparer(TrainPreparationType.YOLO)
        self.assertIsNot(id(YOLOPreparer), id(newYOLOPreparer))
if __name__ == "__main__":
    unittest.main()