from ProjectFile.Src.Core.Interfaces.IAIXProjInfo import IAIXProjInfo
from ProjectFile.Src.Core.Models.AIXProjInfoAggregate import AIXSeedData,DatasetInfo,Device,OutputInfo
from abc import ABC,abstractclassmethod


class IAIXProjInfoBuilder(ABC):
    @abstractclassmethod
    def build(self)->IAIXProjInfo:
        pass
class IAIXProjInfoV1Buider(IAIXProjInfoBuilder):
    @abstractclassmethod
    def setAIXSeedData(self,aIXSeedData:AIXSeedData)->"IAIXProjInfoBuilder":
        pass
    @abstractclassmethod
    def setDatasetInfo(self,datasetInfo:DatasetInfo)->"IAIXProjInfoBuilder":
        pass
    @abstractclassmethod
    def setDevice(self,device:Device)->"IAIXProjInfoBuilder":
        pass
    @abstractclassmethod
    def setOutputInfo(self,outputInfo:OutputInfo)->"IAIXProjInfoBuilder":
        pass