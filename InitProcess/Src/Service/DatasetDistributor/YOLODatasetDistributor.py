from InitProcess.Src.Service.DatasetDistributor.AbstractTrainValidDatasetDistributor import AbstractTrainValidDatasetDistributor
from InitProcess.Src.Service.DirectoryFormat.AbstractTrainValidDirectoryFormat import AbstractTrainValidDirectoryFormat
from InitProcess.Src.Service.DirectoryFormat.YOLODirectoryFormat import YOLODirectoryFormat
from InitProcess.Src.Service.ImageResizer.YOLOImageResizer import YOLOImageResizer, IImageResizer
class YOLODatasetDistributor(AbstractTrainValidDatasetDistributor):
    def getDatasetDirectoryFormat(self)->AbstractTrainValidDirectoryFormat:
        return YOLODirectoryFormat()
    def getImageResizer(self,imageFilePath:str)->IImageResizer:
        return YOLOImageResizer(imageFilePath)