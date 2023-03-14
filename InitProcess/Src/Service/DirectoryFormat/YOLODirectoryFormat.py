from InitProcess.Src.Service.DirectoryFormat.AbstractTrainValidDirectoryFormat import AbstractTrainValidDirectoryFormat
import os
class YOLODirectoryFormat(AbstractTrainValidDirectoryFormat):
    def __init__(self) -> None:
        super().__init__()
        paths=[self.trainImagePath,self.validImagePath,
                self.trainLabelPath,self.validLabelPath]
        for path in paths:
            self.makeDirs(path)
    @property
    def trainImagePath(self)->str:
        return os.path.join(self.datasetPath,r"images\train")
    @property
    def validImagePath(self)->str:
        return os.path.join(self.datasetPath,r"images\valid")
    @property
    def trainLabelPath(self)->str:
        return os.path.join(self.datasetPath,r"labels\train")
    @property
    def validLabelPath(self)->str:
        return os.path.join(self.datasetPath,r"labels\valid")
    def makeDirs(self,path:str):
        if not os.path.exists(path):
            os.makedirs(path)