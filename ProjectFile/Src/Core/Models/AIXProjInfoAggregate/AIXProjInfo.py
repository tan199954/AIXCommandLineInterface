from ProjectFile.Src.Core.Interfaces.IAIXProjInfo import IAIXProjInfo
from ProjectFile.Src.Core.Interfaces.IAIXProjCompositon import IAIXProjCompositon
from ProjectFile.Src.Core.Models.AIXProjInfoAggregate import AIXSeedData,DatasetInfo,Device,OutputInfo

class AIXProjInfoV1(IAIXProjInfo):
    AIX_SEED_DATA_KEY="AIXSeedData"
    DATASET_INFO_KEY = "DatasetInfo"
    DEVICE_KEY = "Device"
    OUTPUT_INFO_KEY = "Output"
    def __init__(self,AIXSeedData:AIXSeedData.AIXSeedData=None,datasetInfo:DatasetInfo.DatasetInfo=None,
                device:Device.Device=None,outputInfo:OutputInfo.OutputInfo=None) -> None:
        self.AIXSeedData=AIXSeedData
        self.datasetInfo=datasetInfo
        self.device=device
        self.outputInfo=outputInfo
        super().__init__()
    def update(self,projCompositon:IAIXProjCompositon):
        projCompositonDict=projCompositon.getDictInfo()
        projCompositonKey=projCompositonDict.keys()[0]
        self.updateProperty(projCompositonKey,projCompositon)
    def updateProperty(self,key:str,projCompositon:IAIXProjCompositon):
        if key == self.AIX_SEED_DATA_KEY:
            self.AIXSeedData=projCompositon
        elif key == self.DATASET_INFO_KEY:
            self.datasetInfo=projCompositon
        elif key == self.DEVICE_KEY:
            self.device=projCompositon
        else:
            self.outputInfo=projCompositon
    def getDictData(self)->dict:
        dictData = {}
        AIXProjCompositons=[self.AIXSeedData,
                            self.datasetInfo,
                            self.device,
                            self.outputInfo]
        for AIXProjCompositon in AIXProjCompositons:
            if AIXProjCompositon is not None:
                compositonData = AIXProjCompositon.getDictInfo()
                dictData[compositonData.keys()[0]]=compositonData.values()
        return dictData
    