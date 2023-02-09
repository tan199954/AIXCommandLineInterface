from abc import ABC,abstractclassmethod
class ILabelPathService(ABC):
    @staticmethod
    @abstractclassmethod
    def getLabelFilePathFrImageFilePath(labelPath:str,imageFilePath:str)->str:
        pass