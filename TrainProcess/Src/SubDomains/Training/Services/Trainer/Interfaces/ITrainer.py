from abc import ABC, abstractclassmethod

class ITrainer(ABC):
    @abstractclassmethod
    def train(self):
        pass