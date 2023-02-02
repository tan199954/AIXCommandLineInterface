from ProjectFile.Src.Service.Interfaces.IAIXProjFileService import IAIXProjFileService
from PySide6 import QtCore
import yaml
import os


class AIXProjFileService(IAIXProjFileService):
    def __init__(self) -> None:
        currentDir = os.getcwd()
        dirName = os.path.basename(currentDir)
        self.imwiProjFilePath = os.path.join(currentDir,dirName+".imwi") 
        super().__init__()
    def isExist(self)->bool:
        imwiProjFile=QtCore.QFile(self.imwiProjFilePath)
        return imwiProjFile.exists()
    def writeProjFile(self,data:dict):
        with open(self.imwiProjFilePath,"w")  as projFile:
            yaml.dump(data,projFile,sort_keys=False)
        projFile.close()
    def readProjFile(self)->dict:
        with open(self.imwiProjFilePath,"r")  as projFile:
            data= yaml.load(projFile,Loader=yaml.FullLoader)
        projFile.close()
        return data