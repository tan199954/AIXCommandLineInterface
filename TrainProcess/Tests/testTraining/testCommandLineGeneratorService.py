import os
import sys
currentFilePath=os.path.abspath(__file__)
testTraining=os.path.dirname(currentFilePath)
testsPath=os.path.dirname(testTraining)
modulePath=os.path.dirname(testsPath)
parentPath=os.path.dirname(modulePath)
sys.path.append(parentPath)
import unittest
def cwd():
     return testsPath
os.getcwd =cwd

from TrainProcess.Src.SubDomains.Training.Services.TrainCommandLineGeneratorService.Implementations.SegCLIGererator import SegCLIGererator
from TrainProcess.Src.SubDomains.Training.Services.TrainCommandLineGeneratorService.Implementations.BBoxCLIGererator import BBoxCLIGererator
class TestSegCLIGererator(unittest.TestCase):
     def testGetCommadLine(self):
          commandLine=SegCLIGererator().getCommadLine()
          self.assertEqual(commandLine,'wsl -d IMWI_WSL_Yoro -- cd /; cd "/mnt/d/Tanworking/python/AIXCommandLineInterface/TrainProcess/Tests/Output"; yolo segment train data=data.yaml model="/mnt/d/Tanworking/python/AIXCommandLineInterface/TrainProcess/Tests/Output/runs/segment/train15/weights/last.pt" imgsz=320 batch=32 lr0=0.01;')
class TestBBoxCLIGererator(unittest.TestCase):
     def testGetCommadLine(self):
          commandLine=BBoxCLIGererator().getCommadLine()
          self.assertEqual(commandLine,'wsl -d IMWI_WSL_Yoro -- cd /; cd "/mnt/d/Tanworking/python/AIXCommandLineInterface/TrainProcess/Tests/Output"; pretrain_exporter "/mnt/d/Tanworking/python/AIXCommandLineInterface/TrainProcess/Tests/Output/models.backup/iter1.sdict" model.pt; trainer cfg.yaml --pretrain model.pt;')
if __name__ == "__main__":
    unittest.main()