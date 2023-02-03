from ProjectFile.Src.Service.Interfaces.IProjCompositonConverter import IProjCompositonConverter
from ProjectFile.Src.Core.Models.AIXProjInfoAggregate.AIXSeedData import AIXSeedData,AIXType

class AIXSeedDataCVT(IProjCompositonConverter):
    @staticmethod
    def toDict(aIXSeedData:AIXSeedData)->dict:
        return {"AIXSeedData":{
            "imagePath": aIXSeedData.imagePath,
            "labelPath": aIXSeedData.labelPath,
            "objectNames": aIXSeedData.objectNames,
            "AIXType": aIXSeedData.AIXType.value
        }}
    @staticmethod
    def toProjCompositon(data:dict)->AIXSeedData:
        if not "AIXSeedData" in data.keys():
            raise Exception("dictData has not been \"AIXSeedData key\"")
        imagePath=data["AIXSeedData"]["imagePath"]
        labelPath=data["AIXSeedData"]["labelPath"]
        objectNames=data["AIXSeedData"]["objectNames"]
        aIXType=AIXType(data["AIXSeedData"]["AIXType"])
        return AIXSeedData(imagePath,labelPath,objectNames,aIXType)