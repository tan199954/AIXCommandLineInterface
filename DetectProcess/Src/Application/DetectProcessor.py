from typing import Union
from ..Enum.DetectType import DetectType
from ..Factory.ImageSourceManagerFactory import ImageSourceManagerFactory
from ..Factory.DetectdObjectExporterFactory import DetectedObjectExporterFactory
from ..Services.Common.ApplicationThread.ApplicationThread import AbstractQCoreApplicationThreadManager
from ..Services.Common.WSLManager.WSLManager import WSLManager
from ..Services.WSLDetectingScriptsCommunicator.WSLDetectingScriptsCommunicator import WSLDetectingScriptsCommunicator
from ..Services.WSLDetectingScriptCommandExecutor.WSLDetectingScriptCommandExcutor import WSLDetectingScriptCommandExcutor
from ..Services.SocketManager.SocketManager import TcpSocketManager


class DetectProcessor(AbstractQCoreApplicationThreadManager):
    def __init__(self,detectType:DetectType,modelFilePath:str,source: Union[str,dict]) -> None:
        super().__init__()
        self.detectType=detectType
        self.modelFilePath=modelFilePath
        self.source=source
        self.wslIp=WSLManager.getIPv4Adress()
        self.wslPort=WSLManager.getAvailablePort()
    def defineMainFuncitionOfQCoreAppThread(self):
        self.tcpSocketManager=TcpSocketManager()
        self.wSLCommunicator=WSLDetectingScriptsCommunicator(self.wslIp,self.wslPort)
        self.wSLCommandExcutor=WSLDetectingScriptCommandExcutor(self.wslIp,self.wslPort,self.detectType,self.modelFilePath)
        self.imageSourceManager=ImageSourceManagerFactory.createImageSourceManager(self.source,self.tcpSocketManager)
        self.detectdObjectExporters=DetectedObjectExporterFactory.createDetectdObjectExporters(self.source,self.tcpSocketManager)
        
        self.wSLCommunicator.server.newConnection.connect(self.__onWSLCommunicatorNewConnection)
        self.wSLCommunicator.resultReceived.connect(self.__onResultReceived)
        self.wSLCommandExcutor.finished.connect(self.__onFinished)
        self.wSLCommandExcutor.errorFinished.connect(self.__onErrorFinished)
        self.wSLCommandExcutor.errorReceived.connect(self.__onErrorReceived)
        self.appThr.app.aboutToQuit.connect(self.__cleanUpPySide6Classes)
        
        self.wSLCommandExcutor.start()
    def __onWSLCommunicatorNewConnection(self):
        self.__waitingForImageSourceManagerGenerateImage()
        self.__detectObjects()
    def __waitingForImageSourceManagerGenerateImage(self):
        while not self.imageSourceManager.isContinueGeneratingImages():
            pass
    def __onResultReceived(self,result:str):
        for exporter in self.detectdObjectExporters:
            exporter.export(result)
        self.__detectObjects()
    def __detectObjects(self):
        if not self.imageSourceManager.isContinueGeneratingImages():
            self.quitQCoreAppThread()
            return
        self.wSLCommunicator.writeImage(self.imageSourceManager.getImage())
    def __onErrorFinished(self,error:str):
        self.quitQCoreAppThread()
        raise RuntimeError(error)
    def __onErrorReceived(self,result:str):
        self.__onErrorFinished(result)
    def __onFinished(self):
        self.quitQCoreAppThread()
    def __cleanUpPySide6Classes(self):
        self.wSLCommandExcutor.stop()
        self.tcpSocketManager = None #smiler del pointer
        self.wSLCommunicator = None #smiler del pointer
        self.imageSourceManager = None #smiler del pointer
        for exporter in self.detectdObjectExporters:
            exporter = None #smiler del pointer
