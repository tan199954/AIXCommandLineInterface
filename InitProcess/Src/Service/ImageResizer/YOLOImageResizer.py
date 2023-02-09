import numpy as np
import cv2
from InitProcess.Src.Service.Interfaces.IImageResizer import IImageResizer
class YOLOImageResizer(IImageResizer):
    MAX_IMAGE_SIZE=512
    def __init__(self,imageFilePath:str) -> None:
        self.image=cv2.imread(imageFilePath)
        super().__init__()
    def getResizedImage(self)->np.ndarray:
        height, width, _=self.image.shape
        if height >self.MAX_IMAGE_SIZE or width >self.MAX_IMAGE_SIZE:
            return cv2.resize(self.image,(512,512))
        return self.image