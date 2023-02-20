from abc import ABC,abstractclassmethod

class ITrainExporter(ABC):
    @abstractclassmethod
    def export(self):
        pass