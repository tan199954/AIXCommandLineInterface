from PySide6 import QtCore
from .IDetector import IDetector
import numpy as np
from yoro import api

class YORODetector(QtCore.QObject,IDetector):
    PARAMETER_SEPARATOR=", "
    OBJECT_SEPARATOR="; "
    LAST_STRING_DATA="\n"
    def __init__(self, modelFilePath:str,parent: QtCore.QObject = None) -> None:
        super().__init__(parent)
        #load model
        devType = api.DeviceType.AUTO
        self.detector = api.YORODetector(modelFilePath, devType)
    def getObjectsInfo(self,image:np.ndarray)->str:
        def getDegreeDetectron2Type(degree):
            if (degree >=-180 and degree <= 90):
                degree = 90 + degree
                return degree
            else:
                degree = -(270 - degree)
                return degree
        # Run detector
        # timeStart = time.time()
        pred = self.detector.detect(image, 0.9, 0.5)
        # timeDetect = time.time() - timeStart
        # timeDetect = float("{0:.3f}".format(timeDetect))
        # convert output to list
        stringOutputData = "#Object = "
        for inst in pred:
            stringOutputData += str(inst.label)
            stringOutputData += self.PARAMETER_SEPARATOR + str(inst.x)
            stringOutputData += self.PARAMETER_SEPARATOR + str(inst.y)
            stringOutputData += self.PARAMETER_SEPARATOR + str(inst.w)
            stringOutputData += self.PARAMETER_SEPARATOR + str(inst.h)
            degree = getDegreeDetectron2Type(inst.degree)
            stringOutputData += self.PARAMETER_SEPARATOR + str(degree) 
            stringOutputData += self.OBJECT_SEPARATOR
        return stringOutputData + self.LAST_STRING_DATA
             