from abc import ABC,abstractproperty
from ProjectFile.Src.AbstractFactory.Interfaces.IProjInfoFactory import IProjInfoFactory
class IAIXProjInfoService(ABC):
    """When you update version of AIXProjInfo,
    you have to overwrite getProjInfoFactory method
    by return IProjInfoFactory."""
    @abstractproperty
    def projInfoFactory(self)->IProjInfoFactory:
        pass