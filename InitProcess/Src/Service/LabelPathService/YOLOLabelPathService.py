from InitProcess.Src.Service.Interfaces.ILabelPathService import ILabelPathService
from PySide6 import QtCore

class YOLOLabelPathService(ILabelPathService):
    YOLO_LABEL_FORMAT=".txt"
    @staticmethod
    def getLabelFilePathFrImageFilePath(labelPath:str,imageFilePath:str)->str:
        return labelPath + "\\" + QtCore.QFileInfo(imageFilePath).baseName() + YOLOLabelPathService.YOLO_LABEL_FORMAT