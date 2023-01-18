from InitProcess.Src.Core import DatasetDirFormat
from typing import List
import os

class YoloDatasetDirFormat(DatasetDirFormat):
    def getImageTrainValidPath(self)->List[str]:
        imagesTrainPath=os.path.join(self.datasetPath,r"images\train")
        imagesValidPath=os.path.join(self.datasetPath,r"images\valid")
        return [imagesTrainPath,imagesValidPath] 
    def getLabelTrainValidPath(self)->List[str]:
        labelsTrainPath=os.path.join(self.datasetPath,r"labels\train")
        labelsValidPath=os.path.join(self.datasetPath,r"labels\valid")
        return [labelsTrainPath,labelsValidPath]
class YoroDatasetDirFormat(DatasetDirFormat):
    def getImageTrainValidPath(self)->List[str]:
        imagesTrainPath=os.path.join(self.datasetPath,"train")
        imagesValidPath=os.path.join(self.datasetPath,"valid")
        return [imagesTrainPath,imagesValidPath]     
    def getLabelTrainValidPath(self)->List[str]:
        labelsTrainPath=os.path.join(self.datasetPath,"train")
        labelsValidPath=os.path.join(self.datasetPath,"valid")
        return [labelsTrainPath,labelsValidPath]