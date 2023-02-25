from .AbstractTrainer import AbstractYOLOTrainer
from ...CommandLineGeneratorService.Implementations.BoxCLIGererator import AbstractYOLOCLIGererator,BoxCLIGererator
from ...ModelInfoBuilder.Implementations.ModelInfoBuilder import IModelInfoBuilder, BoxModelInfoBuilder
class BoxTrainer(AbstractYOLOTrainer):
    def __init__(self) -> None:
        super().__init__()
        self._YOLOCLIGenerator=BoxCLIGererator()
        self._modelInfoBuilder=BoxModelInfoBuilder()
    @property
    def YOLOCLIGenerator(self)->AbstractYOLOCLIGererator:
        return self._YOLOCLIGenerator
    @property
    def modelInfoBuilder(self)->IModelInfoBuilder:
        return  self._modelInfoBuilder