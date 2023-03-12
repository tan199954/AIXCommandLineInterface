from typing import Union
from ..Enum.ImageSourceType import ImageSourceType
from ..Services.ImageSourceManager.Interfaces import IImageSourceManager
from ..Services.ImageSourceManager.Implementation import FileImageSourceManager,TcpServerImageSoureManager,TcpClientImageSoureManager
from ..Services.DataTypeDetector.Detector import ImageSourceTypeDetector
from ..Services.SocketManager.SocketManager import TcpSocketManager


class ImageSourceManagerFactory:
    IMAGE_SOUCRE = {ImageSourceType.File:FileImageSourceManager,
                    ImageSourceType.TcpServer:TcpServerImageSoureManager,
                    ImageSourceType.TcpClient:TcpClientImageSoureManager}
    @classmethod
    def createImageSourceManager(cls,source:Union[str,dict],tcpSocketManager:TcpSocketManager)->IImageSourceManager:
        imageSourceType= ImageSourceTypeDetector.getImageSourceType(source)
        imageSourceManager = cls.IMAGE_SOUCRE[imageSourceType]
        if issubclass(imageSourceManager,FileImageSourceManager):
            return imageSourceManager(source)
        return imageSourceManager(source,tcpSocketManager)