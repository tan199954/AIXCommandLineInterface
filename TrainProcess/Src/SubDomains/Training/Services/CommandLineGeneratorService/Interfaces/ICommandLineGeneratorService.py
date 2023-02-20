from abc import ABC,abstractclassmethod


class ICommandLineGeneratorService(ABC):
    @abstractclassmethod
    def getCommadLine(self)->str:
        pass