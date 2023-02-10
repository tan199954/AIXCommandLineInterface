import nvidia_smi


class DeviceService:
    def getTotalFreeGPUmenmory(self)->int:
        if not self.hasBeenGPU():
            return None
        GPUNum=self.getGpuNumber()
        total=0
        for i in range(0,GPUNum,1):
            freeGpuMemory=self.getFreeGPUmemory(i)
            total=total+freeGpuMemory
        return total
    def getGpuNumber(self)->int:
        nvidia_smi.nvmlInit()
        count = nvidia_smi.nvmlDeviceGetCount()
        return count
    def hasBeenGPU(self):
        try:
            nvidia_smi.nvmlInit()
            return True
        except nvidia_smi.NVMLError:
            return False
    def getFreeGPUmemory(self,index:int):
        nvidia_smi.nvmlInit()
        handle = nvidia_smi.nvmlDeviceGetHandleByIndex(index)
        gpu_info = nvidia_smi.nvmlDeviceGetMemoryInfo(handle)
        memory_free = int(gpu_info.free / 1024 / 1024)
        return memory_free
        