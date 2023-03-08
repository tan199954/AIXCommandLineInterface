from abc import ABC,abstractclassmethod
import numpy as np

class IImageSourceManager(ABC):
    @abstractclassmethod
    def isContinueGeneratingImages(self)->bool:
        """
        Return true if the IImageSourceManager can continue to generate images
        Elese return False
        """
        pass
    @abstractclassmethod
    def getImage(self)->np.ndarray:
        pass
