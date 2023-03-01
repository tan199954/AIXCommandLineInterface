import os
from ..OutputManager.AbstractOutputManager import AbstractOutputManager
from ..YAMLFileService.YAMLFileService import YAMLFileService

currentFilePath=os.path.abspath(__file__)
configDataServicePath=os.path.dirname(currentFilePath)
ServicesPath=os.path.dirname(configDataServicePath)
TrainPreparationPath=os.path.dirname(ServicesPath)
SubDomainPath=os.path.dirname(TrainPreparationPath)
SrcPath=os.path.dirname(SubDomainPath)
TrainProcessPath=os.path.dirname(SrcPath)

class YOROConfigFile:
    CONFIG_FILE_NAME="cfg.yaml"
    SAMPLE_CFG_FILE_RELATIVE_PATH=r"SampleFiles\YOROConfig.yaml"
    __outputDirPath=AbstractOutputManager.getOutputDirPath()
    configFilePath=os.path.join(__outputDirPath,CONFIG_FILE_NAME)
    @staticmethod
    def isExist()->bool:    
        return os.path.exists(YOROConfigFile.configFilePath)
    @staticmethod    
    def createSampleFile():
        """
        After create sample file, you have to update some dictionary data (trainPath, validPath, namesFilePath,...) by YOROConfigFile.updateData() method\n
        see more in "SampleFiles\YOROConfig.yaml"
        """
        sampleCfgFilePath=os.path.join(TrainProcessPath,YOROConfigFile.SAMPLE_CFG_FILE_RELATIVE_PATH)
        sampleCfgData=YAMLFileService.readDictData(sampleCfgFilePath)
        YAMLFileService.writeDictData(YOROConfigFile.configFilePath,sampleCfgData)
    @staticmethod
    def updateData(newData:dict):
        """
        A new data for update must have same structure as in "SampleFiles\YOROConfig.yaml"
        """
        oldData=YOROConfigFile.getCurrentData()
        data=YOROConfigFile()._updatedDictionaryData(oldData,newData)
        YAMLFileService.writeDictData(YOROConfigFile.configFilePath,data)
    @staticmethod
    def getCurrentData()->dict:
        if not YOROConfigFile.isExist():
            YOROConfigFile.createSampleFile()
        return YAMLFileService.readDictData(YOROConfigFile.configFilePath)
    def _updatedDictionaryData(self,oldData:dict,newData:dict)->dict:
        for key in newData.keys():
            if key not in oldData.keys():
                continue
            if not isinstance(newData[key],dict) and not isinstance(oldData[key],dict):
                oldData[key]=newData[key]
                continue
            if isinstance(newData[key],dict) and isinstance(oldData[key],dict):
                oldData[key]=YOROConfigFile()._updatedDictionaryData(oldData[key],newData[key])
        return oldData