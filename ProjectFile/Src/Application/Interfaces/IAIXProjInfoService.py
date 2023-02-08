from abc import ABC,abstractclassmethod
from ProjectFile.Src.AbstractFactory.Interfaces.IProjInfoFactory import IProjInfoFactory
class IAIXProjInfoService(ABC):
    """When you update version of AIXProjInfo,
    you have to overwrite getProjInfoFactory method
    by return IProjInfoFactory."""
    @abstractclassmethod
    def getProjInfoFactory(self)->IProjInfoFactory:
        pass