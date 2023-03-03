from abc import ABC,abstractclassmethod
import numpy as np

class IImageProcessor(ABC):
    @abstractclassmethod
    def isContinuingImageAnalysis(self)->bool:
        pass
    @abstractclassmethod
    def getNewImage(self)->np.ndarray:
        pass
    @abstractclassmethod
    def exportResult(self,result:str):
        pass
