import os
from typing import overload, List
from PySide6 import QtCore
from ProjectFile.Src.Core.Models.AIXProjInfoAggregate.AIXEnum import AIXType


class DatasetPathChecker:
    IMAGE_FILTERS = [ "*.png" , "*.jpg" , "*.bmp"]
    YOLO_LABEL_FILTER = ["*.txt"]
    YORO_LABEL_FILTER = ["*.mark"]
    @overload
    @staticmethod
    def checkLabelPath(labelPath:str,AIXtype:AIXType):...
    @overload
    @staticmethod
    def checkLabelPath(labelPath:str):...
    @staticmethod
    def checkLabelPath(para1=None,para2=None):
        if isinstance(para2,AIXType):
            if para2 == AIXType.BoundingBox:
                DatasetPathChecker.checkLabelPathbyFilter(para1,DatasetPathChecker.YORO_LABEL_FILTER)
            else: DatasetPathChecker.checkLabelPathbyFilter(para1,DatasetPathChecker.YOLO_LABEL_FILTER)
        else:
            filters=DatasetPathChecker.YOLO_LABEL_FILTER+DatasetPathChecker.YORO_LABEL_FILTER
            DatasetPathChecker.checkLabelPathbyFilter(para1,filters)

    def checkLabelPathbyFilter(labelPath:str,filter:List[str]):
        fileInfoList = QtCore.QDir(labelPath).entryInfoList(filter, QtCore.QDir.Files|QtCore.QDir.NoDotAndDotDot)
        if not fileInfoList:
            raise Exception(f"{labelPath} is not contains label files ({', '.join(filter)} Files)")
    @staticmethod
    def checkImagePath(imagePath:str):
        if not QtCore.QDir(imagePath).exists():
                    raise Exception(f"{imagePath} is not exists")
        fileInfoList = QtCore.QDir(imagePath).entryInfoList(DatasetPathChecker.IMAGE_FILTERS, QtCore.QDir.Files|QtCore.QDir.NoDotAndDotDot)
        if not fileInfoList:
            raise Exception(f"{imagePath} is not contain image (png,jpg,bmp)")
