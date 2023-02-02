from typing import List
from ProjectFile.Src.Core.Models.AIXProjInfoAggregate.AIXEnum import AIXType
from ProjectFile.Src.Core.Interfaces.IAIXProjCompositon import IAIXProjCompositon
class AIXSeedData(IAIXProjCompositon):
    def __init__(self,imagePath:str,labelPath:str,objectNames:List[str],AIXType:AIXType) -> None:
        super().__init__()
        self.imagePath=imagePath
        self.labelPath=labelPath
        self.objectNames=objectNames
        self.AIXType = AIXType
    def getImagePath(self)->str:
        return self.imagePath
    def getLabelPath(self)->str:
        return self.labelPath
    def getObjetNames(self)->List[str]:
        return self.objectNames
    def getAIXType(self)->AIXType:
        return self.AIXType
    def getDictInfo(self)->dict:
        return {"AIXSeedData":{
            "imagePath": self.imagePath,
            "labelPath": self.labelPath,
            "objectNames": self.objectNames,
            "AIXType": self.AIXType.value
        }}