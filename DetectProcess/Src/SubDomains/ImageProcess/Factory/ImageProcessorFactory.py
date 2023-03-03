from ..Services.ImageProcessor.Interfaces.IImageProcessor import IImageProcessor


class ImageProcessorFactory:
    @staticmethod
    def createImageProcessor(source:str)->IImageProcessor:
        pass