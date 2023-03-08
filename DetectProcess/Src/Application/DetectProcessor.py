from ..Enum.DetectType import DetectType
from ..SubDomains.Common.ApplicationThread.ApplicationThread import AbstractQCoreApplicationThreadManager
from ..SubDomains.WSLDetectingScriptCommunication.Services.WSLDetectingScriptsCommunicator.WSLDetectingScriptsCommunicator import WSLDetectingScriptsCommunicator
from ..SubDomains.DetectedObjectExportation.Factory
from ..SubDomains.ImageSourceManagement.Factory.ImageProcessorFactory import ImageSourceManagerFactory

class DetectProcessor(AbstractQCoreApplicationThreadManager):
    def __init__(self,detectType:DetectType,modelFilePath:str,source:str) -> None:
        super().__init__()
        wSLDetectingScriptsCommunicator=WSLDetectingScriptsCommunicator()
        self.detector=DetectorFactory.createDetector(detectType,modelFilePath)
        self.imageProcessor=ImageProcessorFactory.createImageProcessor(source)
    def defineMainFuncitionOfQCoreAppThread(self):
        pass
