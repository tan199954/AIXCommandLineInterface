import os
import sys
currentFilePath=os.path.abspath(__file__)
testServicePath=os.path.dirname(currentFilePath)
testsPath=os.path.dirname(testServicePath)
modulePath=os.path.dirname(testsPath)
parentPath=os.path.dirname(modulePath)
sys.path.append(parentPath)

import unittest
from ProjectFile.Src.Application.AIXProjInfoService import AIXProjInfoService
from ProjectFile.Src.Core.Models.AIXProjInfoAggregate.AIXProjInfo import AIXProjInfoV1, AIXSeedData, OutputInfo
class TestAIXProjFileService(unittest.TestCase):
    def testSetAIXProjInfo(self):
        labelPath=os.path.join(testsPath,"segLabelPath")
        imagePath=os.path.join(testsPath,"imagePath")
        projFileService=AIXProjInfoService()
        projFileService.setAIXProjInfo(imagePath,labelPath,["hehe","hihi"])
    def testGetAIXProjInfo(self):
        projFileService=AIXProjInfoService()
        projInfo=projFileService.getAIXProjInfo()

        labelPath=os.path.join(testsPath,"segLabelPath")
        imagePath=os.path.join(testsPath,"imagePath")
        aIXSeedData=AIXSeedData.AIXSeedData(imagePath,labelPath,["hehe","hihi"])
        projInfoV1=AIXProjInfoV1(aIXSeedData)

        self.assertEqual(projInfo.AIXSeedData.__dict__,projInfoV1.AIXSeedData.__dict__)
    def testUpdateAIXProjInfo(self):
        labelPath=os.path.join(testsPath,"segLabelPath")
        imagePath=os.path.join(testsPath,"imagePath")
        outPath=imagePath

        outputInfo=OutputInfo.OutputInfo(outPath)
        projFileService=AIXProjInfoService()
        projFileService.updateAIXProjInfo(outputInfo)
        projInfo=projFileService.getAIXProjInfo()

        aIXSeedData=AIXSeedData.AIXSeedData(imagePath,labelPath,["hehe","hihi"])
        projInfoV1=AIXProjInfoV1(AIXSeedData=aIXSeedData,outputInfo=outputInfo)

        self.assertEqual(projInfo.AIXSeedData.__dict__,projInfoV1.AIXSeedData.__dict__)
        self.assertEqual(projInfo.outputInfo.__dict__,projInfoV1.outputInfo.__dict__)

if __name__=="__main__":
     unittest.main()