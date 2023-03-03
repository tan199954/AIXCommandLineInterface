from abc import ABC,abstractclassmethod
import numpy as np

class IDetector(ABC):
    @abstractclassmethod
    def getObjectInfo(self,image:np.ndarray)->str:
        pass