from ProjectFile.Src.Service.Interfaces.IProjCompositonConverter import IProjCompositonConverter
from ProjectFile.Src.Core.Models.AIXProjInfoAggregate.DatasetInfo import DatasetInfo

class DatasetInfoCVT(IProjCompositonConverter):
    @staticmethod
    def toDict(datasetInfo:DatasetInfo)->dict:
        return {"DatasetInfo":{
            "datasetPath": datasetInfo.datasetPath,
            "trainImagePath": datasetInfo.trainImagePath,
            "validImagePath": datasetInfo.validImagePath,
            "trainLabelPath": datasetInfo.trainLabelPath,
            "validLabelPath": datasetInfo.validLabelPath
        }}
    @staticmethod
    def toProjCompositon(data:dict)->DatasetInfo:
        if not "DatasetInfo" in data.keys():
            raise Exception("dictData has not been \"DatasetInfo key\"")
        datasetInfoData=data["DatasetInfo"]
        datasetPath=datasetInfoData["datasetPath"]
        trainImagePath =datasetInfoData["trainImagePath"]
        validImagePath =datasetInfoData["validImagePath"]
        trainLabelPath =datasetInfoData["trainLabelPath"]
        validLabelPath =datasetInfoData["validLabelPath"]
        return DatasetInfo(datasetPath,trainImagePath,validImagePath,
                            trainLabelPath,validLabelPath)