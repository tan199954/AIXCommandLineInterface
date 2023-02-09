from InitProcess.Src.Service.Interfaces.ILabelPathService import ILabelPathService
from PySide6 import QtCore

class YOROLabelPathService(ILabelPathService):
    YORO_LABEL_FORMAT=".mark"
    @staticmethod
    def getLabelFilePathFrImageFilePath(labelPath:str,imageFilePath:str)->str:
        return labelPath + "\\" + QtCore.QFileInfo(imageFilePath).fileName() + YOROLabelPathService.YORO_LABEL_FORMAT
  