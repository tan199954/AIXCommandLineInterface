from ProjectFile.Src.Core.Interfaces.IAIXProjCompositon import IAIXProjCompositon

class Device(IAIXProjCompositon):
    def __init__(self,GPUmenmory) -> None:
        super().__init__()
        self.GPUmenmory=GPUmenmory
    def getAIXType(self)->int:
        return self.GPUmenmory
