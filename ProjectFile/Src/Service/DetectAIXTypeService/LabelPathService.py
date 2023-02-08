from ProjectFile.Src.Core.Models.AIXProjInfoAggregate.AIXEnum import AIXType
from ProjectFile.Src.Service.DetectAIXTypeService.LabelFileService import LabelFileService
from PySide6 import QtCore


class LabelPathService:
    @staticmethod
    def detectAIXType(labelPath)->AIXType:
        filePath=LabelPathService.getFirstLabelFile(labelPath)
        return LabelFileService.detectAIXType(filePath)
    def getFirstLabelFile(labelPath):
        filters = LabelFileService.YOLO_FILTER+LabelFileService.YORO_FILTER
        fileInfoList = QtCore.QDir(labelPath).entryInfoList(filters, QtCore.QDir.Files|QtCore.QDir.NoDotAndDotDot)
        if not fileInfoList:
            raise Exception(f"{labelPath} is not contains labels (*.txt or *.mark Files)")
        return fileInfoList[0].filePath()