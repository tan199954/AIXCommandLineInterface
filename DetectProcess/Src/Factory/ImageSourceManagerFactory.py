from typing import Union
from PySide6 import QtNetwork
from ..Enum.ImageSourceType import ImageSourceType
from ..Services.ImageSourceManager.Interfaces import IImageSourceManager
from ..Services.ImageSourceManager.Implementation import FilePathImageSourceManager,TcpServerImageSoureManager,TcpClientImageSoureManager
from ..Services.ImageSourceDetector.ImageSourceDetector import ImageSourceDetector


class ImageSourceManagerFactory:
    IMAGE_SOUCRE = {ImageSourceType.File:FilePathImageSourceManager,
                    ImageSourceType.TcpServer:TcpServerImageSoureManager,
                    ImageSourceType.TcpClient:TcpClientImageSoureManager}
    @staticmethod
    def createImageSourceManager(source:Union[str,dict],imageSourceSocket:QtNetwork.QTcpSocket)->IImageSourceManager:
        imageSourceType= ImageSourceDetector.getImageSourceType(source)
        imageSourceManager = ImageSourceManagerFactory.IMAGE_SOUCRE[imageSourceType]
        if isinstance(imageSourceManager,FilePathImageSourceManager):
            return imageSourceManager(source)
        return imageSourceManager(source,imageSourceSocket)