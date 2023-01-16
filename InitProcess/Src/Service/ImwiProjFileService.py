import os
import yaml
from PySide6 import QtCore
from InitProcess.Src.Core import TrainType

class ImwiProjFileService:
     def __init__(self,imagePath:str,labelPath:str,type:TrainType) -> None:
          self.imagePath=imagePath
          self.labelPath=labelPath
          self.type=type

          currentDir = os.getcwd()
          dirName = os.path.basename(currentDir)
          self.imwiProjFilePath = os.path.join(currentDir,dirName+".imwi") 
     def isExist(self)->bool:
          imwiProjFile=QtCore.QFile(self.imwiProjFilePath)
          return imwiProjFile.exists()
     def getImwiProjFilePath(self)->str:
          return self.imwiProjFilePath
     def getRootDict(self)->dict:
          return {
                    {"imagePath":self.imagePath},
                    {"labelPath":self.labelPath},
                    {"type":self.type}
                    }
     def getProjDict(self)->dict:
          if self.isExist():
               with open(self.getImwiProjFilePath(),"r")  as projFile:
                    return yaml.load(projFile,Loader=yaml.FullLoader)
          return {}
     def writeRoot(self):
          projDict = self.getProjDict()
          rootDict = self.getRootDict()
          projDict["root"]=rootDict
          with open(self.getImwiProjFilePath(),"w")  as projFile:
               yaml.dump(projDict,sort_keys=False)
     def writeDataset(self,dataset:dict):
          projDict = self.getProjDict()
          projDict["dataset"]=dataset
          with open(self.getImwiProjFilePath(),"w")  as projFile:
               yaml.dump(projDict,sort_keys=False)