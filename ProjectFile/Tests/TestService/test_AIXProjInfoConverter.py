import os
import sys
currentFilePath=os.path.abspath(__file__)
testServicePath=os.path.dirname(currentFilePath)
testsPath=os.path.dirname(testServicePath)
modulePath=os.path.dirname(testsPath)
parentPath=os.path.dirname(modulePath)
sys.path.append(parentPath)

import unittest
from ProjectFile.Src.Service.AIXProjInfoConverter.AIXProjInfoConverter import AIXProjInfoV1CVT
from ProjectFile.Src.Core.Models.AIXProjInfoAggregate.AIXSeedData import AIXSeedData
from ProjectFile.Src.Core.Models.AIXProjInfoAggregate.DatasetInfo import DatasetInfo
from ProjectFile.Src.Core.Models.AIXProjInfoAggregate.Device import Device
from ProjectFile.Src.Core.Models.AIXProjInfoAggregate.OutputInfo import OutputInfo
from ProjectFile.Src.Core.Models.AIXProjInfoAggregate.AIXProjInfo import AIXProjInfoV1
class TestAIXProjInfoV1CVT(unittest.TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        labelPath=os.path.join(testsPath,"segLabelPath")
        imagePath=os.path.join(testsPath,"imagePath")
        outputPath=os.path.join(testsPath,"imagePath")
        datasetPath=os.path.join(testsPath,"imagePath")
        aIXSeedData=AIXSeedData(imagePath,labelPath,["hehe"])
        datasetInfo=DatasetInfo(datasetPath,imagePath,imagePath,labelPath,labelPath)
        device=Device(4500)
        outputInfo=OutputInfo(outputPath)

        self.aIXProjInfoV1=AIXProjInfoV1(aIXSeedData,datasetInfo,device,outputInfo)
    def testAIXProjInfoV1CVT(self):
        dictData=AIXProjInfoV1CVT.toDict(self.aIXProjInfoV1)
        aiXProjInfo=AIXProjInfoV1CVT.toProjInfo(dictData)
        self.assertEqual(aiXProjInfo.AIXSeedData.__dict__,self.aIXProjInfoV1.AIXSeedData.__dict__)
        self.assertEqual(aiXProjInfo.datasetInfo.__dict__,self.aIXProjInfoV1.datasetInfo.__dict__)
        self.assertEqual(aiXProjInfo.device.__dict__,self.aIXProjInfoV1.device.__dict__)
        self.assertEqual(aiXProjInfo.outputInfo.__dict__,self.aIXProjInfoV1.outputInfo.__dict__)
if __name__=="__main__":
     unittest.main()