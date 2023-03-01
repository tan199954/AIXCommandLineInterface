from .AbstractTrainer import AbstractYOLOTrainer
from ...TrainCommandLineGeneratorService.Implementations.SegCLIGererator import AbstractYOLOCLIGererator,SegCLIGererator
from ...ModelInfoBuilder.Interfaces.IModelInfoBuilder import IModelInfoBuilder
from ...ModelInfoBuilder.Implementations.SegModelInfoBuilder import SegModelInfoBuilder
class SegTrainer(AbstractYOLOTrainer):
    def __init__(self, manual: bool = False,learningRate:float=0.01,imageSize:int=320,batchSize:int=32) -> None:
        super().__init__(manual)
        self._YOLOCLIGenerator=SegCLIGererator(learningRate,imageSize,batchSize)
        self._modelInfoBuilder=SegModelInfoBuilder()
    @property
    def YOLOCLIGenerator(self)->AbstractYOLOCLIGererator:
        return self._YOLOCLIGenerator
    @property
    def modelInfoBuilder(self)->IModelInfoBuilder:
        return  self._modelInfoBuilder