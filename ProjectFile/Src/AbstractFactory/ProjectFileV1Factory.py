from ProjectFile.Src.AbstractFactory.interfaces.IProjectFileFactory import IProjFileAbstractFactory
from ProjectFile.Src.Core.Interfaces.IAIXProjInfo import IAIXProjInfo
from ProjectFile.Src.Core.Models.AIXProjInfoAggregate.AIXProjInfo import AIXProjInfoV1

class ProjectFileV1Factory(IProjFileAbstractFactory):
    def getAIXProjInfo(self)->IAIXProjInfo:
        pass
    def getAIXProjInfoFrDictData(self,data:dict)->IAIXProjInfo:
        pass