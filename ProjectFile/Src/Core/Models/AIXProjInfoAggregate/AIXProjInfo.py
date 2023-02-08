from ProjectFile.Src.Core.Interfaces.IAIXProjInfo import IAIXProjInfo
from ProjectFile.Src.Core.Interfaces.IAIXProjCompositon import IAIXProjCompositon
from ProjectFile.Src.Core.Models.AIXProjInfoAggregate import AIXSeedData,DatasetInfo,Device,OutputInfo

class AIXProjInfoV1(IAIXProjInfo):
    '''When you update AIXProjInfo version (Core),
    you have to update AIXProjInfoService in Application Directory
    ProjInfo"Version"Factory in AbstractFactory Directory,
    AIXProjInfo"Version"Builder and AIXProjInfo"Version"CVT in Service Directory
    "Version" is V1, V2,...'''
    def __init__(self,AIXSeedData:AIXSeedData.AIXSeedData=None,datasetInfo:DatasetInfo.DatasetInfo=None,
                device:Device.Device=None,outputInfo:OutputInfo.OutputInfo=None) -> None:
        self.AIXSeedData=AIXSeedData
        self.datasetInfo=datasetInfo
        self.device=device
        self.outputInfo=outputInfo
        super().__init__()
    def update(self,projCompositon:IAIXProjCompositon):
        if isinstance(projCompositon,AIXSeedData.AIXSeedData):
            self.AIXSeedData=projCompositon
        if isinstance(projCompositon,DatasetInfo.DatasetInfo):
            self.datasetInfo=projCompositon
        if isinstance(projCompositon,Device.Device):
            self.device=projCompositon
        if isinstance(projCompositon,OutputInfo.OutputInfo):
            self.outputInfo=projCompositon
    