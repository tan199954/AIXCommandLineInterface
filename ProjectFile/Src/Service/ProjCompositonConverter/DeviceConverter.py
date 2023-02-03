from ProjectFile.Src.Service.Interfaces.IProjCompositonConverter import IProjCompositonConverter
from ProjectFile.Src.Core.Models.AIXProjInfoAggregate.Device import Device

class DeviceCVT(IProjCompositonConverter):
    @staticmethod
    def toDict(device:Device)->dict:
        return {"Device":{
            "GPUmenmory": device.GPUmenmory
        }}
    @staticmethod
    def toProjCompositon(data:dict)->Device:
        if not "Device" in data.keys():
            raise Exception("dictData has not been \"Device key\"")
        deviceData=data["Device"]
        GPUmenmory=deviceData["GPUmenmory"]
        return Device(GPUmenmory)