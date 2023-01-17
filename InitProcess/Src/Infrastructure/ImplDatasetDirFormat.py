from InitProcess.Src.Core import DatasetDirFormat
from typing import List
import os

class YoloDatasetDirFormat(DatasetDirFormat):
    def getTrainValidPath(self)->List[str]:
        imagesTrainPath=os.path.join(self.datasetPath,"images/train")
        imagesValidPath=os.path.join(self.datasetPath,"images/valid")
        return [imagesTrainPath,imagesValidPath] 
    def getLabelTrainValidPath(self)->List[str]:
        labelsTrainPath=os.path.join(self.datasetPath,"labels/train")
        labelsValidPath=os.path.join(self.datasetPath,"labels/valid")
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