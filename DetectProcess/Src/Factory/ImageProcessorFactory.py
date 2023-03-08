from ..Services.ImageSourceManager.Interfaces.IImageSourceManager import IImageSourceManager


class ImageSourceManagerFactory:
    @staticmethod
    def createImageSourceManager(source:str)->IImageSourceManager:
        pass