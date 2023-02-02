from ProjectFile.Src.Core.Interfaces.IAIXProjInfo import IAIXProjInfo
from abc import ABC,abstractclassmethod

class IProjFileAbstractFactory(ABC):
    @abstractclassmethod
    def getAIXProjInfo(self)->IAIXProjInfo:
        pass
    @abstractclassmethod
    def getAIXProjInfoFrDictData(self,data:dict)->IAIXProjInfo:
        pass