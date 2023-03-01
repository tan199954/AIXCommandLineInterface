from .AbstractYOLOCLIGererator import AbstractYOLOCLIGererator 
from .....Common.OutputManager.BoxOutputManager import AbstractYOLOOutputManager,BoxOutputManager


class BoxCLIGererator(AbstractYOLOCLIGererator):
    @property
    def MODEL_DEFAULT(self)->str:
        return "yolov8n.pt"
    @property
    def TRAIN_COMMAND(self)->str:
        return "yolo detect train"
    @property
    def abstractYOLOOutputManager(self)->AbstractYOLOOutputManager:
        return BoxOutputManager()