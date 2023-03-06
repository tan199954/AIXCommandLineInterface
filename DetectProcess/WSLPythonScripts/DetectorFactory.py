from enum import Enum
from .Detector.IDetector import IDetector
from .Detector.YOLODetector import BoxDetector,SegDetector
from .Detector.YORODetector import YORODetector


class DetectorType(Enum):
    Seg="Seg"
    Box="Box"
    BBox="BBox"

class DetectorFactory:
    DETECTOR_DICTIONARY = {
        DetectorType.BBox:YORODetector,
        DetectorType.Box:BoxDetector,
        DetectorType.Seg:SegDetector
    }
    @staticmethod
    def createDetector(detectorType:DetectorType,modelFilePath:str)->IDetector:
        return DetectorFactory.DETECTOR_DICTIONARY[detectorType](modelFilePath)