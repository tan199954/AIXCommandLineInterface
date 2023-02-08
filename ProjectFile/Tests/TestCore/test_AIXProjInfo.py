import os
import sys
currentFilePath=os.path.abspath(__file__)
testCorePath=os.path.dirname(currentFilePath)
testsPath=os.path.dirname(testCorePath)
modulePath=os.path.dirname(testsPath)
parentPath=os.path.dirname(modulePath)
sys.path.append(parentPath)

import unittest

from ProjectFile.Src.Core.Models.AIXProjInfoAggregate.AIXProjInfo import AIXProjInfoV1
from ProjectFile.Src.Core.Models.AIXProjInfoAggregate.OutputInfo import OutputInfo
from ProjectFile.Src.Core.Models.AIXProjInfoAggregate.AIXSeedData import AIXSeedData

class TestAIXProjInfo(unittest.TestCase):
    def testUpdate(self):
        labelPath=os.path.join(testsPath,"segLabelPath")
        aixSeedData=AIXSeedData("imagePath",labelPath,["objectNames"])
        aIXProjInfoV1=AIXProjInfoV1(aixSeedData)
        outputInfo=OutputInfo("outputPath","outputMoelFilePath")
        aIXProjInfoV1.update(outputInfo)
        self.assertEqual(outputInfo.__dict__,aIXProjInfoV1.outputInfo.__dict__)


if __name__=="__main__":
     unittest.main()