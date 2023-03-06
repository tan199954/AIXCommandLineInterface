from ..Enum.DetectType import DetectType
from ..SubDomains.Detection.Factory.DetectorFactory import DetectorFactory
from ..SubDomains.ImageProcess.Factory.ImageProcessorFactory import ImageProcessorFactory

class DetectProcessor:
    def __init__(self,detectType:DetectType,modelFilePath:str,source:str) -> None:
        self.detector=DetectorFactory.createDetector(detectType,modelFilePath)
        self.imageProcessor=ImageProcessorFactory.createImageProcessor(source)
    def execute(self):
        while self.imageProcessor.isContinuingImageAnalysis():
            image = self.imageProcessor.getNewImage()
            if image is None:
                continue
            result=self.detector.getObjectsInfo(image)
            self.imageProcessor.exportResult(result)