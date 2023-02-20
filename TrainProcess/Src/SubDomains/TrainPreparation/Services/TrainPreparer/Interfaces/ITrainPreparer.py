from abc import ABC,abstractclassmethod

class ITrainPreparer(ABC):
    @abstractclassmethod
    def prepare(self):
        pass