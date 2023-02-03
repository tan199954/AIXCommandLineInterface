from typing import List,overload

from ProjectFile.Src.AbstractFactory.interfaces.IProjInfoFactory import IProjInfoAbstractFactory
from ProjectFile.Src.Core.Interfaces.IAIXProjInfo import IAIXProjInfo
from ProjectFile.Src.Service.AIXProjInfoBuilder.AIXProjInfoBuilder import AIXProjInfoV1Builder
from ProjectFile.Src.Service.Common.DeviceService import DeviceService
from ProjectFile.Src.Core.Models.AIXProjInfoAggregate import DatasetInfo,Device,AIXProjInfo,AIXSeedData,AIXEnum
from ProjectFile.Src.Service.ProjCompositonConverter import AIXSeedDataConverter,DatasetInfoConverter,DeviceConverter,OutputInfoConverter

class ProjInfoV1Factory(IProjInfoAbstractFactory):
    def getAIXProjInfo(self,para1=None,para2=None,para3=None,para4=None)->IAIXProjInfo:
        if self.AIXProjInfoOverloadService.isFirstOverloadMenthod(para1,para2,para3,para4):
            imagePath=para1
            laeblPath=para2
            objectNames=para3
            AIXType=para4
            aIXSeedData=AIXSeedData.AIXSeedData(imagePath,laeblPath,objectNames,AIXType)
            deviceService=DeviceService()
            device=Device.Device(deviceService.getGPUmenmory())
            #build process
            aIXProjInfoV1Builder=AIXProjInfoV1Builder().setAIXSeedData(aIXSeedData)
            aIXProjInfoV1Builder= aIXProjInfoV1Builder.setDevice(device)
            return aIXProjInfoV1Builder.build()
    @overload
    def getAIXProjInfo(self,imagePath:str,laeblPath:str,objectNames:List[str],AIXType:AIXEnum.AIXType):...
    def getAIXProjInfoFrDictData(self,data:dict)->IAIXProjInfo:
        aIXProjInfoV1=AIXProjInfo.AIXProjInfoV1()
        aIXSeedData={aIXProjInfoV1.AIX_SEED_DATA_KEY:data[aIXProjInfoV1.AIX_SEED_DATA_KEY]}
        datasetInfoData={aIXProjInfoV1.DATASET_INFO_KEY:data[aIXProjInfoV1.DATASET_INFO_KEY]}
        deviceData={aIXProjInfoV1.DEVICE_KEY:data[aIXProjInfoV1.DEVICE_KEY]}
        outputInfoData={aIXProjInfoV1.OUTPUT_INFO_KEY:data[aIXProjInfoV1.OUTPUT_INFO_KEY]}
        
        aIXSeedData=AIXSeedDataConverter.AIXSeedDataCVT.toProjCompositon(aIXSeedData)
        datasetInfo=DatasetInfoConverter.DatasetInfoCVT.toProjCompositon(datasetInfoData)
        device=DeviceConverter.DeviceCVT.toProjCompositon(deviceData)
        outputInfo=OutputInfoConverter.OutputInfoCVT.toProjCompositon(outputInfoData)
        #build process
        aIXProjInfoV1Builder=AIXProjInfoV1Builder().setAIXSeedData(aIXSeedData)
        aIXProjInfoV1Builder= aIXProjInfoV1Builder.setDatasetInfo(datasetInfo)
        aIXProjInfoV1Builder= aIXProjInfoV1Builder.setDevice(device)
        aIXProjInfoV1Builder= aIXProjInfoV1Builder.setOutputInfo(outputInfo)
        return aIXProjInfoV1Builder.build()
    class AIXProjInfoOverloadService:
        @staticmethod
        def isFirstOverloadMenthod(para1=None,para2=None,para3=None,Para4=None)->bool:
            result=True
            if not isinstance(para1, str):
                result=False
            if not isinstance(para2, str):
                result=False
            if not isinstance(para3, List[str]):
                result=False
            if not isinstance(Para4, AIXEnum.AIXType):
                result=False
            return result


