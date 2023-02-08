from typing import List,overload
from ProjectFile.Src.AbstractFactory.Interfaces.IProjInfoFactory import IProjInfoFactory
from ProjectFile.Src.Service.AIXProjInfoBuilder.AIXProjInfoBuilder import AIXProjInfoV1Builder
from ProjectFile.Src.Service.AIXProjInfoConverter.AIXProjInfoConverter import AIXProjInfoV1CVT
from ProjectFile.Src.Service.AIXProjInfoBuilder.AIXProjInfoBuilder import AIXProjInfoV1Builder
from ProjectFile.Src.Service.AIXProjInfoConverter.AIXProjInfoConverter import AIXProjInfoV1CVT

class ProjInfoV1Factory(IProjInfoFactory):
    def createProjInfoBuilder(self)->AIXProjInfoV1Builder:
        return AIXProjInfoV1Builder()
    def createProjInfoConverter(self)->AIXProjInfoV1CVT:
        return AIXProjInfoV1CVT()