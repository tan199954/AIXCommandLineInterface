import os
from ProjectFile.Src.Service.Interfaces.IAIXProjInfoBuilder import IAIXProjInfoV1Buider
from ProjectFile.Src.Core.Interfaces.IAIXProjInfo import IAIXProjInfo
from ProjectFile.Src.Core.Models.AIXProjInfoAggregate import AIXProjInfo,AIXSeedData,OutputInfo,DatasetInfo,Device
from ProjectFile.Src.Service.AIXProjInfoBuilder.DatasetPathChecker import DatasetPathChecker


class AIXProjInfoV1Builder(IAIXProjInfoV1Buider):
    def __init__(self) -> None:
        self.aIXSeedData=None
        self.datasetInfo=None
        self.device=None
        self.outputInfo=None
        super().__init__()
    def setAIXSeedData(self,aIXSeedData:AIXSeedData.AIXSeedData)->"AIXProjInfoV1Builder":
        #checkImagePath
        imagePath=aIXSeedData.getLabelPath()
        DatasetPathChecker.checkImagePath(imagePath)
        #checkLabelPath
        labelPath=aIXSeedData.getImagePath()
        AIXType=aIXSeedData.getAIXType()
        DatasetPathChecker.checkLabelPath(labelPath,AIXType)
        #checkObjectNames
        objectNames=aIXSeedData.getObjectNames()
        if not objectNames:
            raise Exception("objectNames is empty")
        self.aIXSeedData=aIXSeedData
        return self
    def setDatasetInfo(self,datasetInfo:DatasetInfo.DatasetInfo)->"AIXProjInfoV1Builder":
        #checkDatasetPath
        datasetPath=datasetInfo.getDatasetPath()
        if not os.path.exists(datasetPath):
            raise Exception(f"{datasetPath} is not exists")
        #checkImagePath
        trainImagePath=datasetInfo.getTrainImagePath()
        validImagePath=datasetInfo.getValidImagePath()
        DatasetPathChecker.checkImagePath(trainImagePath)
        DatasetPathChecker.checkImagePath(validImagePath)
        #checkLabelPath
        trainLabelPath=datasetInfo.getTrainLabelPath()
        validLabelPath=datasetInfo.getValidLabelPath()
        DatasetPathChecker.checkLabelPath(trainLabelPath)
        DatasetPathChecker.checkLabelPath(validLabelPath)
        self.datasetInfo=datasetInfo
        return self
    def setDevice(self,device:Device.Device)->"AIXProjInfoV1Builder":
        self.device=device
        return self
    def setOutputInfo(self,outputInfo:OutputInfo.OutputInfo)->"AIXProjInfoV1Builder":
        #check output path
        outputPath=outputInfo.getOutputPath()
        if not os.path.exists(outputPath):
            raise Exception(f"{outputPath} is not exists")
        #check model file path
        modelFilePath=outputInfo.getOutputModelFilePath()
        if modelFilePath is not None and not os.path.exists(modelFilePath):
            raise Exception(f"{modelFilePath} is not exists")
        self.outputInfo=outputInfo
        return self
    def build(self)->IAIXProjInfo:
        return AIXProjInfo.AIXProjInfoV1(self.aIXSeedData,self.datasetInfo,
                                        self.device,self.outputInfo)