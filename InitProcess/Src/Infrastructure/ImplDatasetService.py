from InitProcess.Src.Core import DatasetService

class BoxDatasetService(DatasetService):
     def execute(self):
          make train/valid sub folder in self.datasetPath
          get dataset from image path and label __path__
          copy dateset to train valid 
     def getDatasetInfo(self)->dict:
          return {"datasetPath":self.datasetPath,
               "trainPath":self.imagesTrainPath,
               "validPath":self.imagesValidPath}
class BBoxDatasetService(DatasetService):
     def execute(self):
          pass
     def getDatasetInfo(self)->dict:
          return {"datasetPath":self.datasetPath,
          "trainPath":self.imagesTrainPath,
          "validPath":self.imagesValidPath}
class SegDatasetService(DatasetService):
     def execute(self):
          pass
     def getDatasetInfo(self)->dict:
          return {"datasetPath":self.datasetPath,
               "trainPath":self.imagesTrainPath,
               "validPath":self.imagesValidPath}