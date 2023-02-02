from ProjectFile.Src.Service.Interfaces.IAIXProjInfoBuilder import IAIXProjInfoV1Buider
from ProjectFile.Src.Core.Interfaces.IAIXProjInfo import IAIXProjInfo
from ProjectFile.Src.Core.Models.AIXProjInfoAggregate import AIXProjInfo,AIXSeedData,OutputInfo,DatasetInfo,Device

class AIXProjInfoV1Builder(IAIXProjInfoV1Buider):
    def __init__(self) -> None:
        super().__init__()
    def setAIXSeedData(self,aIXSeedData:AIXSeedData)->IAIXProjInfoV1Buider:
        self.aIXSeedData=aIXSeedData
        return self
    def setDatasetInfo(self,datasetInfo:DatasetInfo)->IAIXProjInfoV1Buider:
        self.datasetInfo=datasetInfo
        return self
    def setDevice(self,device:Device)->IAIXProjInfoV1Buider:
        self.device=device
        return self
    def setOutputInfo(self,outputInfo:OutputInfo)->IAIXProjInfoV1Buider:
        self.outputInfo=outputInfo
        return self
    def build(self)->IAIXProjInfo:
        return AIXProjInfo.AIXProjInfoV1(self.aIXSeedData,self.datasetInfo,
                                        self.device,self.outputInfo)