import numpy as np
import cv2
from InitProcess.Src.Service.Interfaces.IImageResizer import IImageResizer
class YOROImageResizer(IImageResizer):
    MAX_IMAGE_SIZE=512
    def __init__(self,imageFilePath:str) -> None:
        self.image=cv2.imread(imageFilePath)
        super().__init__()
    def getResizedImage(self)->np.ndarray:
        return self.image