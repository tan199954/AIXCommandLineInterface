from abc import abstractclassmethod
from InitProcess.Src.Infrastructure.ImplDatasetDirFormat import YoloDatasetDirFormat,YoroDatasetDirFormat
from InitProcess.Src.Core import DatasetDirFormat,AbstractDatasetService
from InitProcess.Src.Service.DatasetItemsService import DatasetItemsService,YoloDatasetItemsService,YoroDatasetItemsService
from InitProcess.Src.Service.DatasetDistriutor import DatasetDistributor


class TrainValidDatasetService(AbstractDatasetService):
     def __init__(self,imagePath: str,labelPath :str) -> None:
          super().__init__()
          self.imagePath=imagePath
          self.labelPath=labelPath
          self.datasetDirFormat=self.getDatasetDirFormat()
          self.datasetItemsService = self.getDatasetItemsService()
          self.datasetPath=self.datasetDirFormat.datasetPath
          self.imagesTrainPath,self.imagesValidPath =self.datasetDirFormat.getImageTrainValidPath()
          self.labelsTrainPath,self.labelsValidPath = self.datasetDirFormat.getLabelTrainValidPath()
     def execute(self):
          self.datasetDirFormat.makeDirs()
          datasetItems=self.datasetItemsService.getDatasetItems()
          datasetDistributor=DatasetDistributor(  datasetItems,
                                                  self.imagesTrainPath,
                                                  self.imagesValidPath,
                                                  self.labelsTrainPath,
                                                  self.labelsValidPath)
          datasetDistributor.execute()
     def getDatasetInfo(self)->dict:
          return {"datasetPath":self.datasetPath,
               "trainPath":self.imagesTrainPath,
               "validPath":self.imagesValidPath}
     @abstractclassmethod
     def getDatasetDirFormat(self)->DatasetDirFormat:
          pass
     @abstractclassmethod
     def getDatasetItemsService(self)->DatasetItemsService:
          pass

class BoxDatasetService(TrainValidDatasetService):
     def getDatasetDirFormat(self)->DatasetDirFormat:
          return YoloDatasetDirFormat()
     def getDatasetItemsService(self)->DatasetItemsService:
          return YoloDatasetItemsService(self.imagePath,self.labelPath)
class BBoxDatasetService(TrainValidDatasetService):
     def getDatasetDirFormat(self)->DatasetDirFormat:
          return YoroDatasetDirFormat()
     def getDatasetItemsService(self)->DatasetItemsService:
          return YoroDatasetItemsService(self.imagePath,self.labelPath)
class SegDatasetService(BoxDatasetService):
     pass
