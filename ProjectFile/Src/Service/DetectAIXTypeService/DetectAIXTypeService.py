from typing import overload
from ProjectFile.Src.Core.Models.AIXProjInfoAggregate.AIXEnum import AIXType
from ProjectFile.Src.Service.DetectAIXTypeService.LabelFileService import LabelFileService
from ProjectFile.Src.Service.DetectAIXTypeService.LabelPathService import LabelPathService
import os


class DetectAIXTypeService:
    @staticmethod
    @overload
    def getAIXType(labelPath:str):...
    @staticmethod
    @overload
    def getAIXType(labelFilePath:str):...
    @staticmethod
    def getAIXType(para1=None)->AIXType:
        if not isinstance(para1,str):
            raise TypeError("getAIXType() argument_1 must be a string type")
        if os.path.isdir(para1):
            return LabelPathService.detectAIXType(para1)
        if LabelFileService.isLabel(para1):
            return LabelFileService.detectAIXTypepara1
        raise Exception(f"{para1} must be directory path or label path (*.txt file, *.mark file)")
