import os
import sys
currentFilePath=os.path.abspath(__file__)
testTrainPreparationPath=os.path.dirname(currentFilePath)
testsPath=os.path.dirname(testTrainPreparationPath)
modulePath=os.path.dirname(testsPath)
parentPath=os.path.dirname(modulePath)
sys.path.append(parentPath)
import unittest

from TrainProcess.Src.SubDomains.Training.Services.CommandLineGeneratorService.Implementations.SegCLIGererator import SegCLIGererator

class TestSegCLIGererator(unittest.TestCase):
     def testgetCommadLine(self):
          commandLine=SegCLIGererator().getCommadLine()
          self.assertEqual(commandLine,'wsl -d IMWI_WSL_Yoro -- cd /; cd "/mnt/d/Tanworking/python/AIXCommandLineInterface/TrainProcess/Tests/Output"; yolo segment train data=data.yaml model="/mnt/d/Tanworking/python/AIXCommandLineInterface/TrainProcess/Tests/Output/runs/segment/train15/weights/last.pt" imgsz=320 batch=32 lr0=0.01;')

if __name__ == "__main__":
    unittest.main()