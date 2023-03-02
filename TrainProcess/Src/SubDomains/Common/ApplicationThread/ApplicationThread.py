from PySide6 import QtCore
from typing import Callable
import signal
from abc import abstractclassmethod

class QCoreApplicationThread(QtCore.QThread):
    def __init__(self,defineMainFuncitionOfQCoreAppThread :Callable, parent: QtCore.QObject = None) -> None:
        super().__init__(parent)  
        self.defineMainFuncitionOfQCoreAppThread = defineMainFuncitionOfQCoreAppThread
    def run(self):
        self.app = QtCore.QCoreApplication([])
        self.defineMainFuncitionOfQCoreAppThread()
        self.app.exec()

class AbstractQCoreApplicationThreadManager:
     def __init__(self) -> None:
        signal.signal(signal.SIGINT,self.__cleanUpOnSIGINT)
        self.appThr=QCoreApplicationThread(self.defineMainFuncitionOfQCoreAppThread)
     @abstractclassmethod
     def defineMainFuncitionOfQCoreAppThread(self):
          pass
     def execute(self):
          self.appThr.start()
          self.__keepPointer()
     def quitQCoreAppThread(self):
          self.appThr.app.quit()
     def __keepPointer(self):
          while self.appThr.isRunning():
               pass
          signal.signal(signal.SIGINT,signal.default_int_handler)
     def __cleanUpOnSIGINT(self,signalNum,frame):
          self.quitQCoreAppThread()
          while self.appThr.isRunning():
               pass
          signal.signal(signal.SIGINT,signal.default_int_handler)
          signal.default_int_handler(signalNum,frame)