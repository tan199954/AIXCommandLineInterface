from abc import ABC, abstractclassmethod

class ITrainer(ABC):
    @abstractclassmethod
    def execute(self):
        pass