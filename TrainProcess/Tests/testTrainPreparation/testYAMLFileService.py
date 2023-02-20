import os
import sys
currentFilePath=os.path.abspath(__file__)
testTrainPreparationPath=os.path.dirname(currentFilePath)
testsPath=os.path.dirname(testTrainPreparationPath)
modulePath=os.path.dirname(testsPath)
parentPath=os.path.dirname(modulePath)
sys.path.append(parentPath)
import unittest

from TrainProcess.Src.SubDomains.TrainPreparation.Services.YAMLFileService.YAMLFileService import YAMLFileService
class TestYAMLFileService(unittest.TestCase):
    def testReadFromPath(self):
        data=YAMLFileService.readDictData(r"E:\Jobs\AIX command-Line Interfaces\AIXCommandLineInterface\TrainProcess\SampleFiles\YOLOData.yaml")
        self.assertEqual(type(dict()),type(data))
if __name__ == "__main__":
    unittest.main()