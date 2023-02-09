from InitProcess.Src.Service.DatasetDistributor.AbstractTrainValidDatasetDistributor import AbstractTrainValidDatasetDistributor
from InitProcess.Src.Service.DirectoryFormat.AbstractTrainValidDirectoryFormat import AbstractTrainValidDirectoryFormat
from InitProcess.Src.Service.DirectoryFormat.YORODirectoryFormat import YORODirectoryFormat
from InitProcess.Src.Service.ImageResizer.YOROImageResizer import YOROImageResizer, IImageResizer
class YORODatasetDistributor(AbstractTrainValidDatasetDistributor):
    def getDatasetDirectoryFormat(self)->AbstractTrainValidDirectoryFormat:
        return YORODirectoryFormat()
    def getImageResizer(self,imageFilePath:str)->IImageResizer:
        return YOROImageResizer(imageFilePath)