from abc import abstractproperty
from ..Interfaces.ITrainCommandLineGeneratorService import ITrainCommandLineGeneratorService
from .....Common.PathConverter.PathConverter import PathConverter
from .....Common.OutputManager.AbstractOutputManager import AbstractYOLOOutputManager
from .....Common.CommandLineGeneratorService.CommandLineGeneratorService import WSLCommandLineGenerator

class AbstractYOLOCLIGererator(ITrainCommandLineGeneratorService,WSLCommandLineGenerator):
    DATA_FILE_NAME="data.yaml"
    @abstractproperty
    def MODEL_DEFAULT(self)->str:
        pass
    @abstractproperty
    def TRAIN_COMMAND(self)->str:
        pass
    @abstractproperty
    def abstractYOLOOutputManager(self)->AbstractYOLOOutputManager:
        pass
    def __init__(self,learningRate:float=0.01,imageSize:int=320,batchSize:int=32) -> None:
        super().__init__()
        learningRate=learningRate or 0.01
        imageSize=imageSize or 320
        batchSize=batchSize or 32
        self.learningRate=learningRate
        self.imageSize=imageSize
        self.batchSize=batchSize
    def __getYOLOCommandLine(self)->str:
        if self.abstractYOLOOutputManager.getLastModelFilePath() is not None:
            modelPath=(self.KEEP_FULL_PATH_KEY + 
                       PathConverter.Windows2WSL(self.abstractYOLOOutputManager.getLastModelFilePath())
                    + self.KEEP_FULL_PATH_KEY)
        else:
            modelPath=self.MODEL_DEFAULT
        return (self.TRAIN_COMMAND + self.PARAMETER_SPERATOR
            + "data=" + self.DATA_FILE_NAME + self.PARAMETER_SPERATOR
            + "model=" + modelPath + self.PARAMETER_SPERATOR
            + "imgsz=" + str(self.imageSize) + self.PARAMETER_SPERATOR
            + "batch=" + str(self.batchSize) + self.PARAMETER_SPERATOR
            + "lr0=" + str(self.learningRate) + self.COMMAND_SPERATOR)
    def decreaseLearningRate(self):
        self.learningRate=self.learningRate/10
    def getCommandLine(self)->str:
        outputPath=AbstractYOLOOutputManager.getOutputDirPath()
        return ( WSLCommandLineGenerator.getWSLLoginCommand(self.WSL_DISTRIBUTOR_NAME)+ self.PARAMETER_SPERATOR 
                + self.WSL_ACCEPT_COMMAND_KEY + self.PARAMETER_SPERATOR
                + WSLCommandLineGenerator.getCDCommandFromPath(outputPath)  + self.PARAMETER_SPERATOR 
                + self.__getYOLOCommandLine())