import os
from typing import List
from ..Interfaces.ITrainPreparer import ITrainPreparer
from .....Common.OutputDirManager.AbstractOutputManager import OutputDirManager

class AbstractTrainPreparer(ITrainPreparer):
    def __init__(self,gpuMenmory:int=None,trainPath:str=None,validPath:str=None,nameObjects:List[str]=None) -> None:
        super().__init__()
        self.gpuMenmory=gpuMenmory
        self.trainPath=trainPath
        self.validPath=validPath
        self.nameObjects=nameObjects
        self.outputDirPath=OutputDirManager.getOutputDirPath()
        self._makeOutputdir()
    def _makeOutputdir(self):
        if not os.path.exists(self.outputDirPath):
            os.makedirs(self.outputDirPath)
    