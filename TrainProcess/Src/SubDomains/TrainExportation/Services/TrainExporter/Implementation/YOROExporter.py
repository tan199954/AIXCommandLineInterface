from ..Interfaces.ITrainExporter import ITrainExporter
from .....Common.OutputManager.BBoxOutputManager import BBoxOutputManager
from .....Common.ApplicationThread.ApplicationThread import QCoreApplicationThread

class YOROExporter(ITrainExporter):
    def __init__(self) -> None:
        super().__init__()
        self.outputPath=BBoxOutputManager.getOutputDirPath()
        self.ouputModelFilePath=None
        self.applicationThread=QCoreApplicationThread(self.defineMainFuncitionOfQCoreAppThread)
    def defineMainFuncitionOfQCoreAppThread(self):
        pass
    def export(self):
        getcomline
        runcommandline
        self.ouputModelFilePath=BBoxOutputManager().getOutputModelFilePath()