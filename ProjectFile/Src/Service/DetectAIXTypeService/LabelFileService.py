import os
from PySide6 import QtCore
from typing import List
from ProjectFile.Src.Core.Models.AIXProjInfoAggregate.AIXEnum import AIXType
from ProjectFile.Src.Service.DetectAIXTypeService.LabelFileInfoService import YOLOFileInfo,YOROFileInfo


class LabelFileService:
    YORO_FILTER=["*.mark"]
    YOLO_FILTER=["*.txt"]
    @staticmethod
    def isLabel(labelFilePath:str):
        if LabelFileService.isYoloLabel(labelFilePath) or LabelFileService.isYoloLabel(labelFilePath):
            return True
        return False
    @staticmethod
    def detectAIXType(labelFilePath:str)->AIXType:
        if LabelFileService.isYoloLabel(labelFilePath):
            yOLOFileInfo=YOLOFileInfo(QtCore.QFileInfo(labelFilePath))
            if yOLOFileInfo.isBoxFormat() :return AIXType.Box
            if yOLOFileInfo.isSegmentFormat() :return AIXType.Segment
            raise Exception (f"{labelFilePath} is wrong YOLO format")
        if LabelFileService.isYoroLabel(labelFilePath):
            yOLOFileInfo=YOROFileInfo(QtCore.QFileInfo(labelFilePath))
            if yOLOFileInfo.isMarkFormat() :return AIXType.BoundingBox
            raise Exception (f"{labelFilePath} is wrong YORO format")
        raise Exception(f"{labelFilePath} must be label path (*.txt file, *.mark file)")
    def isYoroLabel(labelFilePath)->bool:
        fileExtension=[element.replace("*","") for element in LabelFileService.YORO_FILTER]
        return LabelFileService.isEqualExtensison(labelFilePath,fileExtension)
    def isYoloLabel(labelFilePath:str)->bool:
        fileExtension=[element.replace("*","") for element in LabelFileService.YOLO_FILTER]
        return LabelFileService.isEqualExtensison(labelFilePath,fileExtension)
    def isEqualExtensison(labelFilePath:str,fileExtensions:List[str])->bool:
        ext = os.path.splitext(labelFilePath)[1]
        if ext.lower() not in fileExtensions:
            return False
        return True
    