from typing import List
from ProjectFile.Src.Core.Models.AIXProjInfoAggregate.AIXEnum import AIXType
from ProjectFile.Src.Core.Interfaces.IAIXProjCompositon import IAIXProjCompositon
from ProjectFile.Src.Service.DetectAIXTypeService.DetectAIXTypeService import DetectAIXTypeService

class AIXSeedData(IAIXProjCompositon):
    def __init__(self,imagePath:str=None,labelPath:str=None,objectNames:List[str]=None,AIXType:AIXType=None) -> None:
        super().__init__()
        self.imagePath=imagePath
        self.labelPath=labelPath
        self.objectNames=objectNames
        if AIXType is None and labelPath is not None:
            self.AIXType = DetectAIXTypeService.getAIXType(labelPath).value
        else:
            self.AIXType=AIXType
    def getImagePath(self)->str:
        return self.imagePath
    def getLabelPath(self)->str:
        return self.labelPath
    def getObjectNames(self)->List[str]:
        return self.objectNames
    def getAIXType(self)->AIXType:
        return AIXType(self.AIXType)