from .AbstractModelInfoBuilder import AbstractYOLOModelInfoBuilder, AbstractYOLOMAPCoefficientFinder,AbstractYOLOLossCoefficientFinder
from ..LossCoefficientFinder.LossCoefficientFinder import SegLossCoefficientFinder
from ..MapCoefficientFinder.MAPCoefficientFinder import SegMAPCoefficientFinder

class SegModelInfoBuilder(AbstractYOLOModelInfoBuilder):
     @property
     def lossCoefficientFinder(self)->AbstractYOLOLossCoefficientFinder:
          return SegLossCoefficientFinder()
     @property
     def mAPCoefficientFinder(self)->AbstractYOLOMAPCoefficientFinder:
          return SegMAPCoefficientFinder()