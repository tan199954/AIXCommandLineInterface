from abc import ABC, abstractclassmethod
from ProjectFile.Src.Core.Interfaces.IAIXProjCompositon import IAIXProjCompositon

class IAIXProjInfo(ABC):
    @abstractclassmethod
    def update(self,projCompositon:IAIXProjCompositon):
        pass