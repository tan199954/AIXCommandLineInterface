from abc import ABC, abstractclassmethod

class IDetectedObjectExporter(ABC):
    @abstractclassmethod
    def export(self):
        pass