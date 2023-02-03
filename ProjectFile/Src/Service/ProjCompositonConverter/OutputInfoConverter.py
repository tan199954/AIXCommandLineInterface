from ProjectFile.Src.Service.Interfaces.IProjCompositonConverter import IProjCompositonConverter
from ProjectFile.Src.Core.Models.AIXProjInfoAggregate.OutputInfo import OutputInfo

class OutputInfoCVT(IProjCompositonConverter):
    @staticmethod
    def toDict(outputInfo:OutputInfo)->dict:
        if outputInfo.outputModelFilePath is not None:
            return {"Output":{
                "outputPath": outputInfo.outputPath,
                "outputModelFilePath":outputInfo.outputModelFilePath
            }}
        return {"Output":{
                "outputPath": outputInfo.outputPath
            }}
    @staticmethod
    def toProjCompositon(data:dict)->OutputInfo:
        if not "Output" in data.keys():
            raise Exception("dictData has not been \"Output key\"")
        outputData=data["Output"]
        outputPath=outputData["outputPath"]
        if not "outputModelFilePath" in  outputData.keys():
            return OutputInfo(outputPath)
        outputModelFilePath=outputData["outputModelFilePath"]
        return OutputInfo(outputPath,outputModelFilePath)