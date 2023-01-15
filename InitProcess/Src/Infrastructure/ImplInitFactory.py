from InitProcess.Src.Core import InitFactory
from InitProcess.Src.Infrastructure.ImplDatasetService import BBoxDatasetService,BoxDatasetService,SegDatasetService
from InitProcess.Src.Infrastructure.ImplProjInputChecker import BBoxProjInputChecker,BoxProjInputChecker,SegProjInputChecker

class BoxInitFactory(InitFactory):
     def createProjInputChecker(self):
          return BoxProjInputChecker(self.imagePath,self.labelPath)
     def createDatasetService(self):
          return BoxDatasetService(self.imagePath,self.labelPath)
class BBoxInitFactory(InitFactory):
     def createProjInputChecker(self):
          return BBoxProjInputChecker(self.imagePath,self.labelPath)
     def createDatasetService(self):
          return BBoxDatasetService(self.imagePath,self.labelPath)
class SegInitFactory(InitFactory):
     def createProjInputChecker(self):
          return SegProjInputChecker(self.imagePath,self.labelPath)
     def createDatasetService(self):
          return SegDatasetService(self.imagePath,self.labelPath)