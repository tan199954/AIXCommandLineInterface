from abc import ABC,abstractclassmethod


class ITrainCommandLineGeneratorService(ABC):
    @abstractclassmethod
    def getCommandLine(self)->str:
        pass