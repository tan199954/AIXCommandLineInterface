from .AbstractModelInfoBuilder import AbstractYOLOModelInfoBuilder, AbstractYOLOLossCoefficientFinder, AbstractYOLOMAPCoefficientFinder
from .LossCoefficientFinder import SegLossCoefficientFinder
from .MAPCoefficientFinder import SegMAPCoefficientFinder

class SegModelInfoBuilder(AbstractYOLOModelInfoBuilder):
     @property
     def lossCoefficientFinder(self)->AbstractYOLOLossCoefficientFinder:
          return SegLossCoefficientFinder()
     @property
     def mAPCoefficientFinder(self)->AbstractYOLOMAPCoefficientFinder:
          return SegMAPCoefficientFinder()