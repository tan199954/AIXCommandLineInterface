from .AbstractTrainer import AbstractYOLOTrainer
from ...CommandLineGeneratorService.Implementations.SegCLIGererator import AbstractYOLOCLIGererator,SegCLIGererator
from ...ModelInfoBuilder.Implementations.ModelInfoBuilder import IModelInfoBuilder, SegModelInfoBuilder
class SegTrainer(AbstractYOLOTrainer):
    @property
    def YOLOCLIGenerator(self)->AbstractYOLOCLIGererator:
        return SegCLIGererator()
    @property
    def modelInfoBuilder(self)->IModelInfoBuilder:
        return  SegModelInfoBuilder()