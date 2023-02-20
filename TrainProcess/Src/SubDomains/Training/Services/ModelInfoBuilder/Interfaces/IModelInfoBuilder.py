from abc import ABC,abstractclassmethod
from ....Models.ModelInfo.Implementations.ModelInfo import ModelInfo
class IModelInfoBuilder(ABC):
    @abstractclassmethod
    def build(self)->ModelInfo:
        pass
    @staticmethod
    @abstractclassmethod
    def buildFromStr(stringData:str)->ModelInfo:
        pass