from PySide6 import QtCore
from ...Enum.DetectType import DetectType
from ..Common.CommandPromptService.CommandPromptService import CommandPromptService
from ..Common.PathConverter.PathConverter import PathConverter
from .WSLDetectingScriptCommandLineGenerator import WSLDetectingScriptCommandLineGenerator



class WSLDetectingScriptCommandExcutor(CommandPromptService):
     def __init__(self ,ip:str,port:int,detectType:DetectType,modelFilePath:str, parent: QtCore.QObject = None) -> None:
         wSLModelFilePath=PathConverter.Windows2WSL(modelFilePath)
         wSLDetectingScriptCommandLineGenerator=WSLDetectingScriptCommandLineGenerator(ip,port,detectType,wSLModelFilePath)
         super().__init__(wSLDetectingScriptCommandLineGenerator.getCommandLine(), parent)

