from typing import Union
from ...Enum.ImageSourceType import ImageSourceType
from .ImageSourceChecker import ImageFormatChecker,TcpIPFormatChecker
from ..Common.SocketManager.SocketManager import SocketManager


class ImageSourceDetector:
    @staticmethod
    def getImageSourceType(source:Union[str,dict])->ImageSourceType:
        if isinstance(source,str):
            ImageFormatChecker.checkImageFilePath(source)
            return ImageSourceType.File
        if isinstance(source,dict):
            TcpIPFormatChecker.checkTcpIPDictionary(source)
            if SocketManager.isListeningServer(source["ip"],source["port"]):
                return ImageSourceType.TcpServer
            return ImageSourceType.TcpClient
        raise TypeError(f"{source} must be string or dict")
        