from abc import ABC,abstractclassmethod
import numpy as np

class IDetector(ABC):
    @abstractclassmethod
    def getObjectsInfo(self,image:np.ndarray)->str:
        pass