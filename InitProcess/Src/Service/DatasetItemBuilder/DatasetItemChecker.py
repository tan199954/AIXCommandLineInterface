from typing import overload, List
from PySide6 import QtCore
from InitProcess.Src.Core.Models.InitEnum import InitType
import os


class DatasetFilePathChecker:
    IMAGE_EXTENSIONS = [ ".png" , ".jpg" , ".bmp"]
    YOLO_LABEL_EXTENSION = [".txt"]
    YORO_LABEL_EXTENSION = [".mark"]
    @overload
    @staticmethod
    def checkLabelFilePath(labelFilePath:str,initType:InitType):...
    @overload
    @staticmethod
    def checkLabelFilePath(labelFilePath:str):...
    @staticmethod
    def checkLabelFilePath(para1=None,para2=None):
        if isinstance(para2,InitType):
            if para2 == InitType.YORO:
                DatasetFilePathChecker.checkLabelFilePathbyExtension(para1,DatasetFilePathChecker.YORO_LABEL_EXTENSION)
            else: DatasetFilePathChecker.checkLabelFilePathbyExtension(para1,DatasetFilePathChecker.YOLO_LABEL_EXTENSION)
        else:
            extensions=DatasetFilePathChecker.YOLO_LABEL_EXTENSION+DatasetFilePathChecker.YORO_LABEL_EXTENSION
            DatasetFilePathChecker.checkLabelFilePathbyExtension(para1,extensions)

    def checkLabelFilePathbyExtension(labelFilePath:str,Extension:List[str]):
        if not QtCore.QFile(labelFilePath).exists():
            raise Exception(f"{labelFilePath} is not exists")
        if not DatasetFilePathChecker.isEqualExtensison(labelFilePath,Extension):
            raise Exception(f"{labelFilePath} is not {', '.join(Extension)} format")
    @staticmethod
    def checkImageFilePath(imageFilePath:str):
        if not QtCore.QFile(imageFilePath).exists():
            raise Exception(f"{imageFilePath} is not exists")
        if not DatasetFilePathChecker.isEqualExtensison(imageFilePath,DatasetFilePathChecker.IMAGE_EXTENSIONS):
            raise Exception(f"{imageFilePath} is not png, jpg or bmp format")
    def isEqualExtensison(labelFilePath:str,fileExtensions:List[str])->bool:
        ext = os.path.splitext(labelFilePath)[1]
        if ext.lower() not in fileExtensions:
            return False
        return True