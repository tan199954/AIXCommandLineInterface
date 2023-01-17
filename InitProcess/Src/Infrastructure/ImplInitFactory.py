from InitProcess.Src.Core import InitFactory
from InitProcess.Src.Core import AbstractDatasetService,ProjInputChecker
from InitProcess.Src.Infrastructure.ImplAbstractDatasetService import BBoxDatasetService,BoxDatasetService,SegDatasetService
from InitProcess.Src.Infrastructure.ImplProjInputChecker import BBoxProjInputChecker,BoxProjInputChecker,SegProjInputChecker

class BoxInitFactory(InitFactory):
     def createProjInputChecker(self)->ProjInputChecker:
          return BoxProjInputChecker(self.imagePath,self.labelPath)
     def createDatasetService(self)->AbstractDatasetService:
          return BoxDatasetService(self.imagePath,self.labelPath)
class BBoxInitFactory(InitFactory):
     def createProjInputChecker(self)->ProjInputChecker:
          return BBoxProjInputChecker(self.imagePath,self.labelPath)
     def createDatasetService(self)->AbstractDatasetService:
          return BBoxDatasetService(self.imagePath,self.labelPath)
class SegInitFactory(InitFactory):
     def createProjInputChecker(self)->ProjInputChecker:
          return SegProjInputChecker(self.imagePath,self.labelPath)
     def createDatasetService(self)->AbstractDatasetService:
          return SegDatasetService(self.imagePath,self.labelPath)