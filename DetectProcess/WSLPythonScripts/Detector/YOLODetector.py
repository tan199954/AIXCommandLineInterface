from PySide6 import QtCore
from .IDetector import IDetector
import numpy as np
from ultralytics import YOLO

class YOLODetector(IDetector):
    PARAMETER_SEPARATOR=", "
    OBJECT_SEPARATOR="; "
    LAST_STRING_DATA="\n"
    MIN_CONFIDENT=0.7
    def __init__(self, modelFilePath:str,parent: QtCore.QObject = None) -> None:
        super().__init__(parent)
        #load model
        self.model = YOLO(modelFilePath)
class SegDetector(YOLODetector):
    def getObjectsInfo(self,image:np.ndarray)->str:
        results = self.model.predict(source=image, save=False, save_txt=False)
        stringOutputData = "#Object = "
        for result in results:
            confs=result.boxes.conf
            ids=result.boxes.cls
            boxs=result.boxes.xywh
            for i,id in enumerate(ids):
                if not confs[i].tolist() >= self.MIN_CONFIDENT:
                    continue
                name=self.model.names[int(id)]
                box=boxs[i].tolist()
                x=box[0]
                y=box[1]
                w=box[2]
                h=box[3]
                stringOutputData += self.PARAMETER_SEPARATOR + str(name)
                stringOutputData += self.PARAMETER_SEPARATOR + str(x)
                stringOutputData += self.PARAMETER_SEPARATOR + str(y)
                stringOutputData += self.PARAMETER_SEPARATOR + str(w)
                stringOutputData += self.PARAMETER_SEPARATOR + str(h)
                stringOutputData += self.OBJECT_SEPARATOR
        return stringOutputData + self.LAST_STRING_DATA

class BoxDetector(YOLODetector):
    def getObjectsInfo(self,image:np.ndarray)->str:
        results = self.model.predict(source=image, save=False, save_txt=False)
        stringOutputData = "#Object = "
        for result in results:
            segments = result.masks.segments
            confs=result.boxes.conf
            ids=result.boxes.cls
            boxs=result.boxes.xywh
            for i,id in enumerate(ids):
                if not confs[i].tolist() >= self.MIN_CONFIDENT:
                    continue
                name=self.model.names[int(id)]
                box=boxs[i].tolist()
                x=box[0]
                y=box[1]
                seg=segments[i].tolist()
                stringOutputData += self.PARAMETER_SEPARATOR + str(name)
                stringOutputData += self.PARAMETER_SEPARATOR + str(x)
                stringOutputData += self.PARAMETER_SEPARATOR + str(y)
                for point in seg:
                    xpoint=point[0]
                    ypoint=point[1]
                    stringOutputData += self.PARAMETER_SEPARATOR + str(xpoint)
                    stringOutputData += self.PARAMETER_SEPARATOR + str(ypoint)
                stringOutputData += self.OBJECT_SEPARATOR
        return stringOutputData + self.LAST_STRING_DATA

             