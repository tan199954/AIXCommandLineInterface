from ProjectFile.Src.Core.Interfaces.IAIXProjCompositon import IAIXProjCompositon

class OutputInfo(IAIXProjCompositon):
    def __init__(self,outputPath:str=None,outputModelFilePath:str=None) -> None:
        super().__init__()
        self.outputPath=outputPath
        self.outputModelFilePath=outputModelFilePath
    def getOutputPath(self)->str:
        return self.outputPath
    def getOutputModelFilePath(self)->str:
        return self.outputModelFilePath
    def setOutputModelFilePath(self,newOutputModelFilePath:str):
        self.outputModelFilePath = newOutputModelFilePath