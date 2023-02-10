from abc import ABC,abstractclassmethod
from ProjectFile.Src.Service.Interfaces.IAIXProjInfoBuilder import IAIXProjInfoBuilder
from ProjectFile.Src.Service.Interfaces.IAIXProjInfoConverter import IAIXProjInfoConverter
class IProjInfoFactory(ABC):
    '''When you update version of AIXProjInfo,
    you have to overwrite createProjInfoBuilder and createProjInfoConverter method
    by return IAIXProjInfoBuilder, IAIXProjInfoConverter.'''
    @abstractclassmethod
    def createProjInfoBuilder(self)->IAIXProjInfoBuilder:
        pass
    def createProjInfoConverter(self)->IAIXProjInfoConverter:
        pass