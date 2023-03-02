from .....Common.OutputManager.BBoxOutputManager import BBoxOutputManager
from .....Common.ApplicationThread.ApplicationThread import AbstractQCoreApplicationThreadManager
from .....Common.CommandPromptService.CommandPromptService import CommandPromptService
from ...ExportCLIGenerator.YOROExportCLIGenerator import YOROExportCLIGenerator
from ..Interfaces.ITrainExporter import ITrainExporter


class BBoxExporter(AbstractQCoreApplicationThreadManager,ITrainExporter):
    def __init__(self) -> None:
        super().__init__()
        self.outputPath=BBoxOutputManager.getOutputDirPath()
        self.ouputModelFilePath=None
    def defineMainFuncitionOfQCoreAppThread(self):
        self.CMDService=CommandPromptService()
        self.CMDService.finished.connect(self.__onFinished)
        self.CMDService.errorFinished.connect(self.__onErrorFinished)
        self.CMDService.outputReceived.connect(self.__onResultReceived)
        self.CMDService.errorReceived.connect(self.__onResultReceived)
        commandLine=YOROExportCLIGenerator.getCommandLine()
        self.CMDService.commandLine=commandLine
        self.CMDService.start()
        self.appThr.app.aboutToQuit.connect(self.__cleanUpPySide6Classes)
    def export(self):
        self.execute()
        self.ouputModelFilePath=BBoxOutputManager().getOutputModelFilePath()
    def __onFinished(self):
        self.quitQCoreAppThread()
    def __onErrorFinished(self,error:str):
        self.__cleanUpPySide6Classes()
        self.quitQCoreAppThread()
        raise RuntimeError(error)
    def __onResultReceived(self,result:str):
        pass
    def __cleanUpPySide6Classes(self):
        try:
            self.CMDService.finished.disconnect(self.__onFinished)
            self.CMDService.errorFinished.disconnect(self.__onErrorFinished)
            self.CMDService.outputReceived.disconnect(self.__onResultReceived)
            self.CMDService.errorReceived.disconnect(self.__onResultReceived)
        except:
            pass
        self.CMDService.stop()