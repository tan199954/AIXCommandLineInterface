from .AbstractTrainer import AbstractYOLOTrainer
from ...TrainCommandLineGeneratorService.Implementations.BoxCLIGererator import AbstractYOLOCLIGererator,BoxCLIGererator
from ...ModelInfoBuilder.Interfaces.IModelInfoBuilder import IModelInfoBuilder
from ...ModelInfoBuilder.Implementations.BoxModelInfoBuilder import BoxModelInfoBuilder
class BoxTrainer(AbstractYOLOTrainer):
    def __init__(self, manual: bool,learningRate:float,imageSize:int,batchSize:int) -> None:
        super().__init__(manual)
        self._YOLOCLIGenerator=BoxCLIGererator(learningRate,imageSize,batchSize)
        self._modelInfoBuilder=BoxModelInfoBuilder()
    @property
    def YOLOCLIGenerator(self)->AbstractYOLOCLIGererator:
        return self._YOLOCLIGenerator
    @property
    def modelInfoBuilder(self)->IModelInfoBuilder:
        return  self._modelInfoBuilder