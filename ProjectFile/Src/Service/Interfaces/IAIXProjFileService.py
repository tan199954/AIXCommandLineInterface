from abc import ABC,abstractclassmethod

class IAIXProjFileService(ABC):
    @abstractclassmethod
    def isExist(self)->bool:
        pass
    @abstractclassmethod
    def writeProjFile(self,data:dict):
        pass
    @abstractclassmethod
    def readProjFile(self)->dict:
        pass