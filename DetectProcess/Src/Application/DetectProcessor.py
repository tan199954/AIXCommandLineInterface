from typing import Union
from PySide6 import QtNetwork
from ..Enum.DetectType import DetectType
from ..Factory.ImageSourceManagerFactory import ImageSourceManagerFactory
from ..Factory.DetectdObjectExporterFactory import DetectdObjectExporterFactory
from ..Services.Common.ApplicationThread.ApplicationThread import AbstractQCoreApplicationThreadManager
from ..Services.Common.WSLManager.WSLManager import WSLManager
from ..Services.WSLDetectingScriptsCommunicator.WSLDetectingScriptsCommunicator import WSLDetectingScriptsCommunicator
from ..Services.WSLDetectingScriptCommandExecutor.WSLDetectingScriptCommandExcutor import WSLDetectingScriptCommandExcutor

class DetectProcessor(AbstractQCoreApplicationThreadManager):
    def __init__(self,detectType:DetectType,modelFilePath:str,source: Union[str,dict]) -> None:
        super().__init__()
        self.detectType=detectType
        self.modelFilePath=modelFilePath
        self.source=source
        self.wslIp=WSLManager.getIPv4Adress()
        self.wslPort=WSLManager.getAvailablePort()
        self.imageSourceSocket = QtNetwork.QTcpSocket() # this socket is connect to image source if it use TCP to send image
    def defineMainFuncitionOfQCoreAppThread(self):
        self.wSLCommunicator=WSLDetectingScriptsCommunicator(self.wslIp,self.wslPort)
        self.wSLCommandExcutor=WSLDetectingScriptCommandExcutor(self.wslIp,self.wslPort,self.detectType,self.modelFilePath)
        self.imageSourceManager=ImageSourceManagerFactory.createImageSourceManager(self.source,self.imageSourceSocket)
        self.detectdObjectExporters=DetectdObjectExporterFactory.createDetectdObjectExporters(self.source,self.imageSourceSocket)
        
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
