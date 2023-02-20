import os
import sys
currentFilePath=os.path.abspath(__file__)
testTrainPreparationPath=os.path.dirname(currentFilePath)
testsPath=os.path.dirname(testTrainPreparationPath)
modulePath=os.path.dirname(testsPath)
parentPath=os.path.dirname(modulePath)
sys.path.append(parentPath)
import unittest

from TrainProcess.Src.SubDomains.TrainPreparation.Services.ConfigDataService.YOROCfgDataService import YOROCfgDataService
class TestYOROCfgDataService(unittest.TestCase):
    def testGetNewConfigData(self):
        configFilePath=os.path.join(testTrainPreparationPath,"cfg.yaml")
        namesFilePath=os.path.join(testTrainPreparationPath,"names.names")
        yOROCfgDataService=YOROCfgDataService(4000,"hehe","hihi",configFilePath,namesFilePath,True)
        dictData=yOROCfgDataService.getNewConfigData()
        self.assertEqual(type(dict()),type(dictData))
if __name__ == "__main__":
    unittest.main()