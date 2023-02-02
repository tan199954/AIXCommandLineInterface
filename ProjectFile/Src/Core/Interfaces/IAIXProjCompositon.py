from abc import ABC, abstractclassmethod

class IAIXProjCompositon(ABC):
    @abstractclassmethod
    def getDictInfo(self)->dict:
        pass