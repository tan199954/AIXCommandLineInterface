from PySide6 import QtCore

class CommandPromptService(QtCore.QObject):
    """
    this class is just run inside QCoreApplication
    """
    errorFinished=QtCore.Signal(str)
    resultReceived = QtCore.Signal(str)
    finished=QtCore.Signal()
    def __init__(self, commandLine:str=None,parent: QtCore.QObject = None) -> None:
        super().__init__(parent)
        self.commandLine=commandLine
        self.process = QtCore.QProcess()
        self.process.readyReadStandardOutput.connect(self._onReadyRead)    
    def start(self):
        self.process.errorOccurred.connect(self._onFinished)
        self.process.finished.connect(self._onFinished)
        if self.commandLine is None:
            raise ValueError("self.commandLine is Node")
        commandLine = "cmd /c "+self.commandLine
        self.process.startCommand(commandLine)    
    def stop(self):
        self.process.errorOccurred.disconnect(self._onFinished)
        self.process.finished.disconnect(self._onFinished)
        if (self.process.state() == QtCore.QProcess.ProcessState.Running or self.process.state() == QtCore.QProcess.ProcessState.Starting):            
            self.process.kill()
            self.process.waitForFinished(-1)
            self.process.close()
    def _onFinished(self):
        data = self.process.readAllStandardError()
        if data.isEmpty():
            self.finished.emit()
        else:
            self.errorFinished.emit(data.data().decode())   
    def _onReadyRead(self):
        data = self.process.readAllStandardOutput()
        self.resultReceived.emit(data.data().decode()) 