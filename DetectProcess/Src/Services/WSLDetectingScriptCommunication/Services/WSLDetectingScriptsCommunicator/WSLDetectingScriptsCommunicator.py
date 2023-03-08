import numpy as np
from PySide6 import QtCore
class WSLDetectingScriptsCommunicator(QtCore.QObject):
    resultReceived=QtCore.Signal(str)
    def writeImage(self,image:np.ndarray):
        pass