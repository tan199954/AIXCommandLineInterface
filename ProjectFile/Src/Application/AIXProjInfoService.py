from typing import List
from ProjectFile.Src.Application.Interfaces.IAIXProjInfoService import IAIXProjInfoService
from ProjectFile.Src.AbstractFactory.Interfaces.IProjInfoFactory import IProjInfoFactory
from ProjectFile.Src.AbstractFactory.ProjInfoV1Factory import ProjInfoV1Factory
from ProjectFile.Src.Service.ProjectFileService.AIXProjFileService import AIXProjFileService
from ProjectFile.Src.Core.Interfaces.IAIXProjCompositon import IAIXProjCompositon
from ProjectFile.Src.Core.Models.AIXProjInfoAggregate.AIXProjInfo import AIXProjInfoV1
from ProjectFile.Src.Core.Models.AIXProjInfoAggregate.AIXSeedData import AIXSeedData
from ProjectFile.Src.Core.Models.AIXProjInfoAggregate.Device import Device
from ProjectFile.Src.Service.Common.DeviceService import DeviceService



class AIXProjInfoService(IAIXProjInfoService):
    @property
    def projInfoFactory(self)->IProjInfoFactory:
        return ProjInfoV1Factory()
    def getAIXProjInfo(self)->AIXProjInfoV1:
        self.__checkExist()
        aIXProjFileService=AIXProjFileService()
        dictData = aIXProjFileService.readProjFile()
        projInfoCVT=self.projInfoFactory.createProjInfoConverter()
        return projInfoCVT.toProjInfo(dictData)
    def setAIXProjInfo(self,imagePath:str,labelPath:str,objectNames:List[str]):
        aIXSeedData=AIXSeedData(imagePath,labelPath,objectNames)
        deviceService=DeviceService()
        device=Device(deviceService.getTotalFreeGPUmenmory())
        #build process
        aIXProjInfoV1Builder=self.projInfoFactory.createProjInfoBuilder()
        aIXProjInfoV1Builder.setAIXSeedData(aIXSeedData)
        aIXProjInfoV1Builder.setDevice(device)
        aIXProjInfo = aIXProjInfoV1Builder.build()
        projInfoCVT=self.projInfoFactory.createProjInfoConverter()
        newDictData=projInfoCVT.toDict(aIXProjInfo)
        aIXProjFileService=AIXProjFileService()
        aIXProjFileService.writeProjFile(newDictData)
    def updateAIXProjInfo(self,aIXProjCompositon:IAIXProjCompositon):
        self.__checkExist()
        aIXProjFileService=AIXProjFileService()
        dictData = aIXProjFileService.readProjFile()
        projInfoCVT=self.projInfoFactory.createProjInfoConverter()
        aIXProjInfo = projInfoCVT.toProjInfo(dictData)
        aIXProjInfo.update(aIXProjCompositon)
        newDictData=projInfoCVT.toDict(aIXProjInfo)
        aIXProjFileService.writeProjFile(newDictData)
    def __checkExist(self):
        aIXProjFileService=AIXProjFileService()
        if not aIXProjFileService.isExist():
            raise Exception("Could not find AIX project File\n"
                            "Please use command \"AIX-CLI init -h\"")