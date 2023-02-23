import signal
from PySide6 import QtCore
from abc import abstractclassmethod
from .....Common.ApplicationThread.ApplicationThread import QCoreApplicationThread
from ..Interfaces.ITrainer import ITrainer


class AbstractQCoreAppTrainer(ITrainer):
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
          if self.appThr.isRunning():
               self.appThr.quit()
               if self.appThr is not QtCore.QThread.currentThread():
                    self.appThr.wait()
     def __keepPointer(self):
          while self.appThr.isRunning():
               pass
          signal.signal(signal.SIGINT,signal.default_int_handler)
     def __cleanUpOnSIGINT(self,signalNum,frame):
          signal.signal(signal.SIGINT,signal.default_int_handler)
          if self.appThr.isRunning():
               self.appThr.quit()
               self.appThr.wait()
          signal.default_int_handler(signalNum,frame)
