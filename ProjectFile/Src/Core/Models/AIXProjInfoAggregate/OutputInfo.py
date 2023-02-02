from ProjectFile.Src.Core.Interfaces.IAIXProjCompositon import IAIXProjCompositon

class OutputInfo(IAIXProjCompositon):
    def __init__(self,outputPath:str,outputModelFilePath=None) -> None:
        super().__init__()
        self.outputPath=outputPath
        self.outputModelFilePath=outputModelFilePath
    def getOutputPath(self)->str:
        return self.outputPath
    def getOutputModelFilePath(self)->str:
        return self.outputModelFile
    def setOutputModelFilePath(self,newOutputModelFilePath:str):
        self.outputModelFilePath = newOutputModelFilePath
    def getDictInfo(self)->dict:
        if self.outputModelFilePath is not None:
            return {"Output":{
                "outputPath": self.outputPath,
                "outputModelFile":self.outputModelFile
            }}
        return {"Output":{
                "outputPath": self.outputPath
            }}