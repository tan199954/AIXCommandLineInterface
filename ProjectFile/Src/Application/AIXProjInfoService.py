from typing import List
from ProjectFile.Src.AbstractFactory.ProjInfoV1Factory import ProjInfoV1Factory
from ProjectFile.Src.Service.ProjectFileService.AIXProjFileService import AIXProjFileService
from ProjectFile.Src.Core.Interfaces.IAIXProjCompositon import IAIXProjCompositon
from ProjectFile.Src.Core.Interfaces.IAIXProjInfo import IAIXProjInfo
from ProjectFile.Src.Core.Models.AIXProjInfoAggregate.AIXEnum import AIXType


class AIXProjInfoService:
    def __init__(self) -> None:
        self.projectFileFactory=ProjInfoV1Factory()
        self.aIXProjFileService=AIXProjFileService()
    def getAIXProjInfo(self)->IAIXProjInfo:
        if not self.aIXProjFileService.isExist():
            raise Exception("Could not find AIX project File\n"
                            "Please use command \"AIX-CLI init -h\"")
        dictData = self.aIXProjFileService.readProjFile()
        return self.projectFileFactory.getAIXProjInfoFrDictData(dictData)
    def setAIXProjInfo(self,imagePath:str,laeblPath:str,objectNames:List[str],AIXType:AIXType):
        aIXProjInfo = self.projectFileFactory.getAIXProjInfo(imagePath,laeblPath,
                                                            objectNames,AIXType)
        newDictData=aIXProjInfo.getDictData()
        self.aIXProjFileService.writeProjFile(newDictData)
    def updateAIXProjInfo(self,aIXProjCompositon:IAIXProjCompositon):
        if not self.aIXProjFileService.isExist():
            raise Exception("Could not find AIX project File\n"
                            "Please use command \"AIX-CLI init -h\"")
        dictData = self.aIXProjFileService.readProjFile()
        aIXProjInfo = self.projectFileFactory.getAIXProjInfoFrDictData(dictData)
        aIXProjInfo.update(aIXProjCompositon)
        newDictData=aIXProjInfo.getDictData()
        self.aIXProjFileService.writeProjFile(newDictData)