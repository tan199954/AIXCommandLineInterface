from abc import ABC,abstractclassmethod


class ITrainCommandLineGeneratorService(ABC):
    @abstractclassmethod
    def getCommadLine(self)->str:
        pass