from .....Common.CommandLineGeneratorService.CommandLineGeneratorService import WSLCommandLineGenerator
from .....Common.OutputManager.BBoxOutputManager import BBoxOutputManager
from .....Common.YOROConfigFile.YOROConfigFile import YOROConfigFile
from .....Common.PathConverter.PathConverter import PathConverter
from ..Interfaces.ITrainCommandLineGeneratorService import ITrainCommandLineGeneratorService


class BBoxCLIGererator(ITrainCommandLineGeneratorService,WSLCommandLineGenerator):
    YORO_TRAIN_COMMAND="trainer"
    PRETRAIN_KEY="--pretrain"
    YORO_PRETRAIN_EXPORT_COMMAND="pretrain_exporter"
    PT_MODEL_FILE_NAME="model.pt"
    def __getTrainCommandLine(self)->str:
        return (self.YORO_TRAIN_COMMAND +self.PARAMETER_SPERATOR 
                + YOROConfigFile.CONFIG_FILE_NAME + self.COMMAND_SPERATOR )
    def __getPretrainCommandLines(self,lastModelFilePath)->str:
        return (self.__getPretrainExportCommandLine(lastModelFilePath) + self.PARAMETER_SPERATOR
                +self.__getPretrainCommandLine())
    def __getPretrainCommandLine(self):
        return (self.YORO_TRAIN_COMMAND + self.PARAMETER_SPERATOR
                +YOROConfigFile.CONFIG_FILE_NAME + self.PARAMETER_SPERATOR
                +self.PRETRAIN_KEY + self.PARAMETER_SPERATOR
                +self.PT_MODEL_FILE_NAME + self.COMMAND_SPERATOR)
    def __getPretrainExportCommandLine(self,lastModelFilePath):
        WSLmodelFilePath=(self.KEEP_FULL_PATH_KEY
                          +PathConverter.Windows2WSL(lastModelFilePath)
                          +self.KEEP_FULL_PATH_KEY)
        return (self.YORO_PRETRAIN_EXPORT_COMMAND +self.PARAMETER_SPERATOR
                +WSLmodelFilePath +self.PARAMETER_SPERATOR
                +self.PT_MODEL_FILE_NAME + self.COMMAND_SPERATOR)
    def __YOROTrainCommandLine(self)->str:
        lastModelFilePath=BBoxOutputManager().getLastModelFilePath()
        if isinstance(lastModelFilePath,str):
            return self.__getPretrainCommandLines(lastModelFilePath)
        return self.__getTrainCommandLine()
    def getCommandLine(self)->str:
        outputPath=BBoxOutputManager.getOutputDirPath()
        return (WSLCommandLineGenerator.getWSLLoginCommand(self.WSL_DISTRIBUTOR_NAME)+ self.PARAMETER_SPERATOR 
                + self.WSL_ACCEPT_COMMAND_KEY +self.PARAMETER_SPERATOR
                + WSLCommandLineGenerator.getCDCommandFromPath(outputPath)  + self.PARAMETER_SPERATOR 
                +self.__YOROTrainCommandLine())