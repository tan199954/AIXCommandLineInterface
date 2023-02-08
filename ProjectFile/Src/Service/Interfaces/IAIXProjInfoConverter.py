from abc import ABC,abstractclassmethod
from ProjectFile.Src.Core.Interfaces.IAIXProjCompositon import IAIXProjCompositon
from ProjectFile.Src.Core.Interfaces.IAIXProjInfo import IAIXProjInfo


class IProjCompositonConverter(ABC):
    @staticmethod
    @abstractclassmethod
    def toDict(AIXProjCompositon:IAIXProjCompositon)->dict:
        pass
    @staticmethod
    @abstractclassmethod
    def toProjCompositon(data:dict)->IAIXProjCompositon:
        pass
class IAIXProjInfoConverter(ABC):
    @staticmethod
    @abstractclassmethod
    def toDict(aIXProjInfo:IAIXProjInfo)->dict:
        pass
    @staticmethod
    @abstractclassmethod
    def toProjInfo(data:dict)->IAIXProjInfo:
        pass