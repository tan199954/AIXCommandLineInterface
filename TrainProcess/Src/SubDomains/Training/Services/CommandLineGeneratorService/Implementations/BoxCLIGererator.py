from .AbstractYOLOCLIGererator import AbstractYOLOCLIGererator 


class BoxCLIGererator(AbstractYOLOCLIGererator):
    @property
    def MODEL_DEFAULT(self)->str:
        return "yolov8n.pt"
    @property
    def TRAIN_COMMAND(self)->str:
        return "yolo detect train"