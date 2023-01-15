from InitProcess.Src.Service.ImwiProjFileService import ImwiProjFileService
from InitProcess.Src.Core import TrainType
from InitProcess.Src.InitAbstractFactory import InitAbstractFactory
class InitProcess:
     def __init__(self,imagePath: str,labelPath :str,type:TrainType) -> None:
          self.imwiProjFileService = ImwiProjFileService(imagePath,labelPath,type)
          initAbstractFactory = InitAbstractFactory(imagePath,labelPath,type)
          initFactory = initAbstractFactory.getFactory()
          self.projInputChecker = initFactory.createProjInputChecker()
          self.datasetService = initFactory.createDatasetService()
     def execute(self):
          if self.imwiProjFileService.isExist():
               raise Exception("This current directory is constain imwiProjFile\n"
                              "It better initialize in empty directory")
          self.projInputChecker.check()
          self.imwiProjFileService.writeRoot()
          self.datasetService.execute() #create train valid in this folder namseFile to current dir
          datasetInfo = self.datasetService.getDatasetInfo() #return dataset with dict type
          self.imwiProjFileService.writeDataset(datasetInfo)
