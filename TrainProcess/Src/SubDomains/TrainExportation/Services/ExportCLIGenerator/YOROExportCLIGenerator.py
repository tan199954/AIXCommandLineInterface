from ....Common.CommandLineGeneratorService.CommandLineGeneratorService import WSLCommandLineGenerator
from ....Common.OutputManager.BBoxOutputManager import BBoxOutputManager
from ....Common.PathConverter.PathConverter import PathConverter
from ....Common.YOROConfigFile.YOROConfigFile import YOROConfigFile
class YOROExportCLIGenerator(WSLCommandLineGenerator):
    EXPORT_COMMAND="backup_exporter"
    def getCommandLine(self):
        lastModelPath=BBoxOutputManager().getLastModelFilePath()
        wslLastModelPath=(self.KEEP_FULL_PATH_KEY
                          + PathConverter.Windows2WSL(lastModelPath)
                          +self.KEEP_FULL_PATH_KEY)
        outputPath=BBoxOutputManager.getOutputDirPath()
        return (WSLCommandLineGenerator.getWSLLoginCommand(self.WSL_DISTRIBUTOR_NAME)+ self.PARAMETER_SPERATOR 
                + self.WSL_ACCEPT_COMMAND_KEY +self.PARAMETER_SPERATOR
                + WSLCommandLineGenerator.getCDCommandFromPath(outputPath)  + self.PARAMETER_SPERATOR 
                + self.EXPORT_COMMAND + self.PARAMETER_SPERATOR
                + YOROConfigFile.CONFIG_FILE_NAME +self.PARAMETER_SPERATOR
                + wslLastModelPath +self.COMMAND_SPERATOR)