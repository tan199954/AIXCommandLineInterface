from .AbstractModelInfoBuilder import AbstractYOLOModelInfoBuilder, AbstractYOLOLossCoefficientFinder, AbstractYOLOMAPCoefficientFinder
from .LossCoefficientFinder import BoxLossCoefficientFinder
from .MAPCoefficientFinder import BoxMAPCoefficientFinder

class BoxModelInfoBuilder(AbstractYOLOModelInfoBuilder):
     @property
     def lossCoefficientFinder(self)->AbstractYOLOLossCoefficientFinder:
          return BoxLossCoefficientFinder()
     @property
     def mAPCoefficientFinder(self)->AbstractYOLOMAPCoefficientFinder:
          return BoxMAPCoefficientFinder()