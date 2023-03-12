import os
currentFilePath=os.path.abspath(__file__)
WSLDetectingScriptCommandExecutorPath=os.path.dirname(currentFilePath)
ServicesPath=os.path.dirname(WSLDetectingScriptCommandExecutorPath)
SrcPath=os.path.dirname(ServicesPath)
DetectProcessPath=os.path.dirname(SrcPath)
WSLPythonScriptsPath=os.path.join(DetectProcessPath,"WSLPythonScripts")
DetectingScriptFilePath=os.path.join(WSLPythonScriptsPath,"DetectingScript.py")


from ..Common.CommandLineGeneratorService.CommandLineGeneratorService import WSLCommandLineGenerator
from ...Enum.DetectType import DetectType


class WSLDetectingScriptCommandLineGenerator(WSLCommandLineGenerator):
    SCRIPT_LANGUAGE="python"
    IP_KEY ="--ip"
    PORT_KEY ="--port"
    TYPE_KEY ="--type"
    MODEL_FILE_PATH_KEY ="--modelFilePath"
    DETECTING_SCRIPTS_FILE_NAME="DetectingScript.py"
    def __init__(self,ip:str,port:int,detectType:DetectType,wslModelFilePath:str) -> None:
        super().__init__()
        self._ip=ip
        self._port=port
        self._detectTypeValue=detectType.value
        self._modelFilePath=wslModelFilePath
    def __getPythonScriptCommand(self):
        return (self.SCRIPT_LANGUAGE +self.PARAMETER_SPERATOR
                +self.DETECTING_SCRIPTS_FILE_NAME + self.PARAMETER_SPERATOR
                +self.IP_KEY + self.PARAMETER_SPERATOR + self._ip + self.PARAMETER_SPERATOR
                +self.PORT_KEY + self.PARAMETER_SPERATOR + str(self._port) + self.PARAMETER_SPERATOR
                +self.TYPE_KEY + self.PARAMETER_SPERATOR + self._detectTypeValue + self.PARAMETER_SPERATOR
                +self.MODEL_FILE_PATH_KEY + self.PARAMETER_SPERATOR + self.addQuotesToPath(self._modelFilePath) + self.COMMAND_SPERATOR)
    def getCommandLine(self)->str:
        return (WSLCommandLineGenerator.getWSLLoginCommand() +self.PARAMETER_SPERATOR
               + self.WSL_ACCEPT_COMMAND_KEY + self.PARAMETER_SPERATOR
               + WSLCommandLineGenerator.getCDCommandFromPath(WSLPythonScriptsPath) + self.PARAMETER_SPERATOR
               + self.__getPythonScriptCommand())