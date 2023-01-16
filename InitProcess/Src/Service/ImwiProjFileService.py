import os
import yaml
from PySide6 import QtCore
from InitProcess.Src.Core import TrainType

class ImwiProjFileService:
     def __init__(self,imagePath:str,labelPath:str,trainType:TrainType) -> None:
          self.imagePath=imagePath
          self.labelPath=labelPath
          self.trainType=trainType
          currentDir = os.getcwd()
          dirName = os.path.basename(currentDir)
          self.imwiProjFilePath = os.path.join(currentDir,dirName+".imwi") 
     def isExist(self)->bool:
          imwiProjFile=QtCore.QFile(self.imwiProjFilePath)
          return imwiProjFile.exists()
     def getImwiProjFilePath(self)->str:
          return self.imwiProjFilePath
     def getRootDict(self)->dict:
          return {"imagePath":self.imagePath,
                    "labelPath":self.labelPath,
                    "trainType":self.trainType}
     def getProjDict(self)->dict:
          if not self.isExist():
               return {}
          with open(self.getImwiProjFilePath(),"r")  as projFile:
               data= yaml.load(projFile,Loader=yaml.FullLoader)
               projFile.close()
          if data is not None:
               return data
          return {}
     def writeRoot(self):
          projDict = self.getProjDict()
          rootDict = self.getRootDict()
          projDict["root"]=rootDict
          with open(self.getImwiProjFilePath(),"w")  as projFile:
               yaml.dump(projDict,projFile,sort_keys=False)
          projFile.close()
     def writeDataset(self,dataset:dict):
          projDict = self.getProjDict()
          projDict["dataset"]=dataset
          with open(self.getImwiProjFilePath(),"w")  as projFile:
               yaml.dump(projDict,projFile,sort_keys=False)
          projFile.close()