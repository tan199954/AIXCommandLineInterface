from abc import ABC,abstractclassmethod
class IDatasetDistributor(ABC):
    @abstractclassmethod
    def execute(self):
        pass