import os
import sys
currentFilePath=os.path.abspath(__file__)
testTrainPreparationPath=os.path.dirname(currentFilePath)
testsPath=os.path.dirname(testTrainPreparationPath)
modulePath=os.path.dirname(testsPath)
parentPath=os.path.dirname(modulePath)
sys.path.append(parentPath)
def getcwd():
    return testsPath
os.getcwd = getcwd
import unittest

from TrainProcess.Src.SubDomains.Common.YOROConfigFile.YOROConfigFile import YOROConfigFile

class TestYOROConfigFile(unittest.TestCase):
     def test_updatedDictionaryData(self):
        oldData={"X":1,"Y":2,
                 "Z":{"A":3,"B":4}}
        newData={"Z":{"A":5},
                 "U":0,
                 "X":0}
        updatedData1={"X":0,"Y":2,
                        "Z":{"A":5,"B":4}}
        updatedData=YOROConfigFile()._updatedDictionaryData(oldData,newData)
        self.assertEqual(updatedData1,updatedData)
        
if __name__ == "__main__":
    unittest.main()