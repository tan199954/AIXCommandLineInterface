from abc import ABC, abstractclassmethod

class IAIXProjInfo(ABC):
    @abstractclassmethod
    def getDictData(self):
        pass
    @abstractclassmethod
    def update(self):
        pass