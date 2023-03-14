from ProjectFile.Src.Core.Interfaces.IAIXProjCompositon import IAIXProjCompositon

class Device(IAIXProjCompositon):
    def __init__(self,totalFreeGPUMemory:int=None) -> None:
        super().__init__()
        self.totalFreeGPUMemory=totalFreeGPUMemory
    def getTotalFreeGPUMemory(self)->int:
        return self.totalFreeGPUMemory
