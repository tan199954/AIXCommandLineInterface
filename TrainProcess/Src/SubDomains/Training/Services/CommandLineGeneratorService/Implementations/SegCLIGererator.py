from .AbstractYOLOCLIGererator import AbstractYOLOCLIGererator 


class SegCLIGererator(AbstractYOLOCLIGererator):
    @property
    def MODEL_DEFAULT(self)->str:
        return "yolov8n-seg.pt"
    @property
    def TRAIN_COMMAND(self)->str:
        return "yolo segment train"