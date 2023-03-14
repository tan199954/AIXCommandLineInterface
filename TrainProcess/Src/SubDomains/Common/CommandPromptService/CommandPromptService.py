from PySide6 import QtCore
import os

class CommandPromptService(QtCore.QObject):
    """
    this class is just run inside QCoreApplication
    """
    errorFinished=QtCore.Signal(str)
    outputReceived = QtCore.Signal(str)
    errorReceived = QtCore.Signal(str)
    finished=QtCore.Signal()
    ERROR_KEYS ="Traceback"
    def __init__(self, commandLine:str=None,parent: QtCore.QObject = None) -> None:
        super().__init__(parent)
        self.commandLine=commandLine
        self.process = QtCore.QProcess()
        self.currentError=str()
    def start(self):
        self.process.errorOccurred.connect(self.__onErrorOccurred)
        self.process.finished.connect(self.__onFinished)
        self.process.readyReadStandardError.connect(self.__onReadError)  
        self.process.readyReadStandardOutput.connect(self.__onReadOutput) 
        if self.commandLine is None:
            raise ValueError("self.commandLine is Node")
        commandLine = "cmd /c "+self.commandLine
        print(f"commandLine: {commandLine}")
        self.process.startCommand(commandLine)    
    def stop(self):
        if (self.process.state() == QtCore.QProcess.ProcessState.Running or self.process.state() == QtCore.QProcess.ProcessState.Starting):            
            self.process.kill()
            self.process.waitForFinished(-1)
            self.process.close()
        os.system("taskkill /F /im wsl.exe")
        os.system("taskkill /F /im wslhost.exe")

    def __onErrorOccurred(self,error:QtCore.QProcess.ProcessError):
        data = self.process.readAllStandardError()
        if self.process.waitForFinished(50):
            self.errorFinished.emit(data.data().decode())
        else:
            self.errorReceived.emit(data.data().decode())
    def __onFinished(self):
        data = self.process.readAllStandardError()
        if not data.isEmpty():
            self.errorFinished.emit(data.data().decode())  
        if not self.currentError == "":
            self.errorFinished.emit(self.currentError)
        else:
            self.finished.emit()
    def __onReadOutput(self):
        data = self.process.readAllStandardOutput()
        self.outputReceived.emit(data.data().decode()) 
    def __onReadError(self):
        data = self.process.readAllStandardError().data().decode()
        if self.ERROR_KEYS in data:
            self.currentError=data
        if not self.currentError == "":
            self.currentError += data
        if self.process.waitForFinished(50):
            self.errorFinished.emit(data)
        else:
            self.errorReceived.emit(data)
