import os
import sys
currentFilePath=os.path.abspath(__file__)
testServicePath=os.path.dirname(currentFilePath)
testsPath=os.path.dirname(testServicePath)
modulePath=os.path.dirname(testsPath)
parentPath=os.path.dirname(modulePath)
sys.path.append(parentPath)

import unittest
from ProjectFile.Src.Service.AIXProjInfoBuilder.AIXProjInfoBuilder import AIXProjInfoV1Builder
from ProjectFile.Src.Core.Models.AIXProjInfoAggregate.AIXProjInfo import AIXProjInfoV1
from ProjectFile.Src.Core.Models.AIXProjInfoAggregate.AIXSeedData import AIXSeedData
from ProjectFile.Src.Core.Models.AIXProjInfoAggregate.DatasetInfo import DatasetInfo
from ProjectFile.Src.Core.Models.AIXProjInfoAggregate.Device import Device
from ProjectFile.Src.Core.Models.AIXProjInfoAggregate.OutputInfo import OutputInfo
class TestAIXProjInfoV1Builder(unittest.TestCase):
    def testAIXProjInfoV1Builder(self):
        labelPath=os.path.join(testsPath,"segLabelPath")
        imagePath=os.path.join(testsPath,"imagePath")
        outputPath=os.path.join(testsPath,"imagePath")
        datasetPath=os.path.join(testsPath,"imagePath")
        aIXSeedData=AIXSeedData(imagePath,labelPath,["hehe"])
        datasetInfo=DatasetInfo(datasetPath,imagePath,imagePath,labelPath,labelPath)
        device=Device(4500)
        outputInfo=OutputInfo(outputPath)

        aIXProjInfoV1Builder=AIXProjInfoV1Builder().setAIXSeedData(aIXSeedData)
        aIXProjInfoV1Builder=aIXProjInfoV1Builder.setDatasetInfo(datasetInfo)
        aIXProjInfoV1Builder=aIXProjInfoV1Builder.setDevice(device)
        aIXProjInfoV1Builder=aIXProjInfoV1Builder.setOutputInfo(outputInfo)
        aIXProjInfoV1FrBuilder=aIXProjInfoV1Builder.build()
        
        aIXProjInfoV1=AIXProjInfoV1(aIXSeedData,datasetInfo,device,outputInfo)

        self.assertEqual(aIXProjInfoV1FrBuilder.__dict__,aIXProjInfoV1.__dict__)


if __name__=="__main__":
     unittest.main()