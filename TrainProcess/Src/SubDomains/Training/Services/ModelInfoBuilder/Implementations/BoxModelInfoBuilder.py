from .AbstractModelInfoBuilder import AbstractYOLOModelInfoBuilder, AbstractYOLOMAPCoefficientFinder,AbstractYOLOLossCoefficientFinder
from ..LossCoefficientFinder.LossCoefficientFinder import BoxLossCoefficientFinder
from ..MapCoefficientFinder.MAPCoefficientFinder import BoxMAPCoefficientFinder

class BoxModelInfoBuilder(AbstractYOLOModelInfoBuilder):
     @property
     def lossCoefficientFinder(self)->AbstractYOLOLossCoefficientFinder:
          return BoxLossCoefficientFinder()
     @property
     def mAPCoefficientFinder(self)->AbstractYOLOMAPCoefficientFinder:
          return BoxMAPCoefficientFinder()