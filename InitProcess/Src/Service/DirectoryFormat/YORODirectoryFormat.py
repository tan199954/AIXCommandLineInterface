from InitProcess.Src.Service.DirectoryFormat.AbstractTrainValidDirectoryFormat import AbstractTrainValidDirectoryFormat
import os
class YORODirectoryFormat(AbstractTrainValidDirectoryFormat):
    def __init__(self) -> None:
        super().__init__()
        paths=[self.imagesTrainPath,self.imagesValidPath,
                self.labelsTrainPath,self.labelsValidPath]
        for path in paths:
            self.makeDirs(path)
    @property
    def imagesTrainPath(self)->str:
        return os.path.join(self.datasetPath,"train")
    @property
    def imagesValidPath(self)->str:
        return os.path.join(self.datasetPath,"valid")
    @property
    def labelsTrainPath(self)->str:
        return os.path.join(self.datasetPath,"train")
    @property
    def labelsValidPath(self)->str:
        return os.path.join(self.datasetPath,"valid")
    def makeDirs(self,path:str):
        if not os.path.exists(path):
            os.makedirs(path)