from .AbstractTrainer import AbstractYOLOTrainer
from ...CommandLineGeneratorService.Implementations.BoxCLIGererator import AbstractYOLOCLIGererator,BoxCLIGererator
from ...ModelInfoBuilder.Implementations.ModelInfoBuilder import IModelInfoBuilder, BoxModelInfoBuilder
class BoxTrainer(AbstractYOLOTrainer):
    @property
    def YOLOCLIGenerator(self)->AbstractYOLOCLIGererator:
        return BoxCLIGererator()
    @property
    def modelInfoBuilder(self)->IModelInfoBuilder:
        return BoxModelInfoBuilder()