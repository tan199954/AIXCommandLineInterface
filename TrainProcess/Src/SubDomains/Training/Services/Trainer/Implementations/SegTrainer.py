from .AbstractTrainer import AbstractYOLOTrainer
from ...CommandLineGeneratorService.Implementations.SegCLIGererator import AbstractYOLOCLIGererator,SegCLIGererator
from ...ModelInfoBuilder.Implementations.ModelInfoBuilder import IModelInfoBuilder, SegModelInfoBuilder
class SegTrainer(AbstractYOLOTrainer):
    def __init__(self) -> None:
        super().__init__()
        self._YOLOCLIGenerator=SegCLIGererator()
        self._modelInfoBuilder=SegModelInfoBuilder()
    @property
    def YOLOCLIGenerator(self)->AbstractYOLOCLIGererator:
        return self._YOLOCLIGenerator
    @property
    def modelInfoBuilder(self)->IModelInfoBuilder:
        return  self._modelInfoBuilder