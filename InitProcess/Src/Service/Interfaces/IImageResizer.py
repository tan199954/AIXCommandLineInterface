from abc import ABC, abstractclassmethod
import numpy as np

class IImageResizer(ABC):
    @abstractclassmethod
    def getResizedImage(self)->np.ndarray:
        pass