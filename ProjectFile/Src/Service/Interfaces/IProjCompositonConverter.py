from abc import ABC,abstractclassmethod
from ProjectFile.Src.Core.Interfaces.IAIXProjCompositon import IAIXProjCompositon
class IProjCompositonConverter(ABC):
    @abstractclassmethod
    @staticmethod
    def toDict(AIXProjCompositon:IAIXProjCompositon)->dict:
        pass
    @abstractclassmethod
    @staticmethod
    def toProjCompositon(data:dict)->IAIXProjCompositon:
        pass