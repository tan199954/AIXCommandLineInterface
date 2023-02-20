from abc import abstractproperty
from ..Interfaces.ICommandLineGeneratorService import ICommandLineGeneratorService
from .....Common.PathConverter.PathConverter import PathConverter
from .....Common.OutputDirManager.OutputDirManager import OutputDirManager


class AbstractYOLOCLIGererator(ICommandLineGeneratorService):
    WSL_LOGIN_COMMAND="wsl -d IMWI_WSL_Yoro"
    DATA_FILE_NAME="data.yaml"
    COMMAND_SPERATOR=";"
    PARAMETER_SPERATOR=" "
    ACCEPT_COMMAND_KEY="--"
    KEEP_FULL_PATH_KEY='"'
    @abstractproperty
    def MODEL_DEFAULT(self)->str:
        pass
    @abstractproperty
    def TRAIN_COMMAND(self)->str:
        pass
    def __init__(self,learningRate:float=0.01,imageSize:int=320,batchSize:int=32) -> None:
        super().__init__()
        self.learningRate=learningRate
        self.imageSize=imageSize
        self.batchSize=batchSize
    def __getYOLOCommandLine(self)->str:
        if OutputDirManager.isLastModelExist():
            modelPath=(self.KEEP_FULL_PATH_KEY + 
                       PathConverter.Windows2WSL(OutputDirManager.getLastModelPath())
                    + self.KEEP_FULL_PATH_KEY)
        else:
            modelPath=self.MODEL_DEFAULT
        return (self.TRAIN_COMMAND + self.PARAMETER_SPERATOR
            + "data=" + self.DATA_FILE_NAME + self.PARAMETER_SPERATOR
            + "model=" + modelPath + self.PARAMETER_SPERATOR
            + "imgsz=" + str(self.imageSize) + self.PARAMETER_SPERATOR
            + "batch=" + str(self.batchSize) + self.PARAMETER_SPERATOR
            + "lr0=" + str(self.learningRate) + self.COMMAND_SPERATOR)
    def __getCDOutputCommandLine(self)->str:
        outputDirPath=OutputDirManager.getOutputDirPath()
        wslOutputPath= (self.KEEP_FULL_PATH_KEY 
                        + PathConverter.Windows2WSL(outputDirPath) 
                        + self.KEEP_FULL_PATH_KEY)
        return ("cd /" +self.COMMAND_SPERATOR + self.PARAMETER_SPERATOR
                + "cd " + wslOutputPath+ self.COMMAND_SPERATOR)
    def decreaseLearningRate(self):
        self.learningRate=self.learningRate/10
    def getCommadLine(self)->str:
        return (self.WSL_LOGIN_COMMAND + self.PARAMETER_SPERATOR 
                + self.ACCEPT_COMMAND_KEY + self.PARAMETER_SPERATOR
                + self.__getCDOutputCommandLine() + self.PARAMETER_SPERATOR 
                + self.__getYOLOCommandLine() + self.COMMAND_SPERATOR)