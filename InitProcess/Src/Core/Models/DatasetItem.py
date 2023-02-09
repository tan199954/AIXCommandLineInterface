from InitProcess.Src.Core.Interfaces.IDatasetItem import IDatasetItem

class ImageDatasetItem(IDatasetItem):
    def __init__(self,imageFilePath:str=None,labelFilePath:str=None) -> None:
        self.imageFilePath=imageFilePath
        self.labelFilePath=labelFilePath