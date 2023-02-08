from typing import Union
from ProjectFile.Src.Core.Interfaces.IAIXProjInfo import IAIXProjInfo
from ProjectFile.Src.Core.Interfaces.IAIXProjCompositon import IAIXProjCompositon
from ProjectFile.Src.Core.Models.AIXProjInfoAggregate.AIXProjInfo import AIXProjInfoV1
from ProjectFile.Src.Core.Models.AIXProjInfoAggregate.AIXSeedData import AIXSeedData
from ProjectFile.Src.Core.Models.AIXProjInfoAggregate.DatasetInfo import DatasetInfo
from ProjectFile.Src.Core.Models.AIXProjInfoAggregate.Device import Device
from ProjectFile.Src.Core.Models.AIXProjInfoAggregate.OutputInfo import OutputInfo
from ProjectFile.Src.Service.Interfaces.IAIXProjInfoConverter import IAIXProjInfoConverter
from ProjectFile.Src.Service.AIXProjInfoBuilder.AIXProjInfoBuilder import AIXProjInfoV1Builder
class AIXProjInfoV1CVT(IAIXProjInfoConverter):
    def getCompositonData(compositon:Union[IAIXProjCompositon,IAIXProjInfo])->dict:
        compositonData=compositon.__dict__
        dictData={}
        for key in compositonData.keys():
            if isinstance(compositonData[key],IAIXProjCompositon):
                newCompositonData=AIXProjInfoV1CVT.getCompositonData(compositonData[key])
                if newCompositonData:
                    dictData[key]=newCompositonData
            elif compositonData[key] is not None:
                dictData[key]=compositonData[key]
        return dictData
    @staticmethod
    def toDict(aIXProjInfo:AIXProjInfoV1)->dict:
        return AIXProjInfoV1CVT.getCompositonData(aIXProjInfo)
    @staticmethod
    def toProjInfo(data:dict)->AIXProjInfoV1:
        aIXProjInfoV1Builder=AIXProjInfoV1Builder()
        if 'AIXSeedData' in data.keys():
            aIXSeedDictData=data['AIXSeedData']
            aIXSeedData=AIXSeedData()
            aIXSeedData.__dict__.update(**aIXSeedDictData)
            aIXProjInfoV1Builder.setAIXSeedData(aIXSeedData)
        if 'datasetInfo' in data.keys():
            datasetInfoData=data['datasetInfo']
            datasetInfo=DatasetInfo()
            datasetInfo.__dict__.update(**datasetInfoData)
            aIXProjInfoV1Builder.setDatasetInfo(datasetInfo)
        if "device" in data.keys():
            deviceData=data["device"]
            device=Device()
            device.__dict__.update(**deviceData)
            aIXProjInfoV1Builder.setDevice(device)
        if "outputInfo" in data.keys():
            outputInfoData=data["outputInfo"]
            outputInfo=OutputInfo()
            outputInfo.__dict__.update(**outputInfoData)
            aIXProjInfoV1Builder.setOutputInfo(outputInfo)
        return aIXProjInfoV1Builder.build()