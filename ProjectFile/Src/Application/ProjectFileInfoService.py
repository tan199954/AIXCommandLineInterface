from ProjectFile.Src.AbstractFactory.ProjectFileV1Factory import ProjectFileV1Factory
from ProjectFile.Src.Service.ProjectFileService.AIXProjFileService import AIXProjFileService
from ProjectFile.Src.Core.Interfaces.IAIXProjCompositon import IAIXProjCompositon
class ProjectFileInfoService:
    def __init__(self) -> None:
        self.projectFileFactory=ProjectFileV1Factory()
        self.aIXProjFileService=AIXProjFileService()
    def getProjFileInFo(self):
        if not self.aIXProjFileService.isExist():
            raise Exception("Could not find AIX project File\n"
                            "Please use command \"AIX-CLI init -h\"")
        dictData = self.aIXProjFileService.readProjFile()
        return self.projectFileFactory.getAIXProjInfoFrDictData(dictData)
    def setProjFileInFo(self):
        aIXProjInfo = self.projectFileFactory.getAIXProjInfo()
        newDictData=aIXProjInfo.getDictData()
        self.aIXProjFileService.writeProjFile(newDictData)
    def updateFileInfo(self,aIXProjCompositon:IAIXProjCompositon):
        if not self.aIXProjFileService.isExist():
            raise Exception("Could not find AIX project File\n"
                            "Please use command \"AIX-CLI init -h\"")
        dictData = self.aIXProjFileService.readProjFile()
        aIXProjInfo = self.projectFileFactory.getAIXProjInfoFrDictData(dictData)
        aIXProjInfo.update(aIXProjCompositon)
        newDictData=aIXProjInfo.getDictData()
        self.aIXProjFileService.writeProjFile(newDictData)