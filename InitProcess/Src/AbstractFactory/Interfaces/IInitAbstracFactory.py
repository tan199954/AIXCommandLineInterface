from abc import ABC,abstractclassmethod
from InitProcess.Src.Core.Models.InitEnum import InitType
from InitProcess.Src.AbstractFactory.Interfaces.IInitFactory import IInitFactory

class IInitAbstractFactory(ABC):
    @abstractclassmethod
    def getFactory(self,initType:InitType)->IInitFactory:
        pass