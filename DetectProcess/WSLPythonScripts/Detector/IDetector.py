from abc import abstractclassmethod
from PySide6.QtCore import QObject
import numpy as np

class IDetector(QObject):
    @abstractclassmethod
    def getObjectsInfo(self,image:np.ndarray)->str:
        pass