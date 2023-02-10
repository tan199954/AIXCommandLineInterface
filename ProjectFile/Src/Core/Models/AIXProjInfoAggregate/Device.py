from ProjectFile.Src.Core.Interfaces.IAIXProjCompositon import IAIXProjCompositon

class Device(IAIXProjCompositon):
    def __init__(self,totalFreeGPUmemory:int=None) -> None:
        super().__init__()
        self.totalFreeGPUmemory=totalFreeGPUmemory
    def getAIXType(self)->int:
        return self.totalFreeGPUmemory
