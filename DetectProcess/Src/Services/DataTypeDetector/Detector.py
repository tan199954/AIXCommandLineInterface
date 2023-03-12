from typing import Union, List
from ...Enum.ImageSourceType import ImageSourceType
from ...Enum.DetectedObjectExporterType import DetectedObjectExporterType
from .Checker import ImageFormatChecker,TcpIPFormatChecker
from ..Common.TCPIPManager.TCPIPManager import TCPIPManager


class ImageSourceTypeDetector:
    @staticmethod
    def getImageSourceType(source:Union[str,dict])->ImageSourceType:
        if isinstance(source,str):
            ImageFormatChecker.checkImageFilePath(source)
            return ImageSourceType.File
        if isinstance(source,dict):
            TcpIPFormatChecker.checkTcpIPDictionary(source)
            if TCPIPManager.isListeningServer(source["ip"],source["port"]):
                return ImageSourceType.TcpServer
            return ImageSourceType.TcpClient
        raise TypeError(f"{source} must be string or dict")
    
class DetectedObjectExporterTypeDetector:
    @staticmethod
    def getDetectedObjectExporterTypes(source:Union[str,dict])->List[DetectedObjectExporterType]:
        if isinstance(source,str):
            ImageFormatChecker.checkImageFilePath(source)
            return [DetectedObjectExporterType.Terminal]
        if isinstance(source,dict):
            TcpIPFormatChecker.checkTcpIPDictionary(source)
            if TCPIPManager.isListeningServer(source["ip"],source["port"]):
                return [DetectedObjectExporterType.TCPSocket,DetectedObjectExporterType.Terminal]
        raise TypeError(f"{source} must be string or dict")
        