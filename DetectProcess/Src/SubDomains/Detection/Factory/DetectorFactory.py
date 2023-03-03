from ....Enum.DetectType import DetectType
from ...Detection.Services.Detector.Interfaces.IDetector import IDetector

class DetectorFactory:

    @staticmethod
    def createDetector(detectType:DetectType,modelFilePath:str)->IDetector:
        pass