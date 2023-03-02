from abc import abstractproperty
from .....Common.OutputManager.AbstractOutputManager import AbstractYOLOOutputManager
from .....Common.OutputManager.BoxOutputManager import BoxOutputManager
from .....Common.OutputManager.SegOutputManager import SegOutputManager
from ..Interfaces.ITrainExporter import ITrainExporter


class AbstractYOLOExporter(ITrainExporter):
    @property
    def abstractYOLOOutputManager(self)->AbstractYOLOOutputManager:
        pass
    def __init__(self) -> None:
        super().__init__()
        self.outputPath=self.abstractYOLOOutputManager.getOutputDirPath()
        self.ouputModelFilePath=self.abstractYOLOOutputManager.getBestModelFilePath()
    def export(self):
        pass

class BoxExporter(AbstractYOLOExporter):
    @property
    def abstractYOLOOutputManager(self):
        return BoxOutputManager()

class SegExporter(AbstractYOLOExporter):
    @property
    def abstractYOLOOutputManager(self):
        return SegOutputManager()