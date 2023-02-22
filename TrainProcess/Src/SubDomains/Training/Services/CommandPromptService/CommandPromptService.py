from PySide6 import QtCore

class CommandPromptService(QtCore.QObject):
    """
    this class is just run inside QCoreApplication
    """
    errorFinished=QtCore.Signal(str)
    outputReceived = QtCore.Signal(str)
    errorReceived = QtCore.Signal(str)
    finished=QtCore.Signal()
    def __init__(self, commandLine:str=None,parent: QtCore.QObject = None) -> None:
        super().__init__(parent)
        self.commandLine=commandLine
        self.process = QtCore.QProcess()
        self.process.readyReadStandardOutput.connect(self.__onReadOutput)
        self.process.readyReadStandardError.connect(self.__onReadError)    
    def start(self):
        self.process.errorOccurred.connect(self.__onErrorOccurred)
        self.process.finished.connect(self.__onFinished)
        if self.commandLine is None:
            raise ValueError("self.commandLine is Node")
        commandLine = "cmd /c "+self.commandLine
        self.process.startCommand(commandLine)    
    def stop(self):
        self.process.errorOccurred.disconnect(self.__onErrorOccurred)
        self.process.finished.disconnect(self.__onFinished)
        if (self.process.state() == QtCore.QProcess.ProcessState.Running or self.process.state() == QtCore.QProcess.ProcessState.Starting):            
            self.process.kill()
            self.process.waitForFinished(-1)
            self.process.close()
    def __onErrorOccurred(self,error:QtCore.QProcess.ProcessError):
        data = self.process.readAllStandardError()
        if self.process.waitForFinished():
            self.errorFinished.emit(data.data().decode())
        else:
            self.errorReceived.emit(data.data().decode())
    def __onFinished(self):
        data = self.process.readAllStandardError()
        if data.isEmpty():
            self.finished.emit()
        else:
            self.errorFinished.emit(data.data().decode())   
    def __onReadOutput(self):
        data = self.process.readAllStandardOutput()
        self.outputReceived.emit(data.data().decode()) 
    def __onReadError(self):
        data = self.process.readAllStandardError()
        if self.process.waitForFinished(300):
            self.errorFinished.emit(data.data().decode())
        else:
            self.errorReceived.emit(data.data().decode())
