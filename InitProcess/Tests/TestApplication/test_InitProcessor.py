import os
import sys
currentFilePath=os.path.abspath(__file__)
testServicesPath=os.path.dirname(currentFilePath)
testsPath=os.path.dirname(testServicesPath)
modulePath=os.path.dirname(testsPath)
parentPath=os.path.dirname(modulePath)
sys.path.append(parentPath)

import unittest
from InitProcess.Src.Application.InitProcessor import InitProcessor
from InitProcess.Src.Core.Models.InitEnum import InitType


class TestImageDatasetItemBuilder(unittest.TestCase):
    def testImageDatasetItemBuilder(self):
        imagePath=os.path.join(testsPath,r"imagePath")
        labelPath=os.path.join(testsPath,r"bbLabelPath")
        initType=InitType.YORO
        initProcessor = InitProcessor(imagePath,labelPath,initType)
        initProcessor.execute()
        print(initProcessor.getDirFormat())
if __name__=="__main__":
     unittest.main()