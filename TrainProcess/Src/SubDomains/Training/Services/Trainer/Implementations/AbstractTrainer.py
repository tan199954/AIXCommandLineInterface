import signal
from abc import abstractclassmethod
from .....Common.ApplicationThread.ApplicationThread import QCoreApplicationThread
from ..Interfaces.ITrainer import ITrainer


class AbstractQCoreAppTrainer(ITrainer):
     def __init__(self) -> None:
        signal.signal(signal.SIGINT,self.__cleanUp)
     @abstractclassmethod
     def definePySide6Classes(self):
          pass
     def execute(self):
          self.appThr=QCoreApplicationThread(self.definePySide6Classes)
          self.appThr.start()
          self.__keepPointer()
     def __keepPointer(self):
          while self.appThr.isRunning():
               pass
          signal.signal(signal.SIGINT,signal.default_int_handler)
     def __cleanUp(self,signalNum,frame):
          signal.signal(signal.SIGINT,signal.default_int_handler)
          if self.appThr.isRunning():
               self.appThr.quit()
               self.appThr.wait()
          signal.default_int_handler(signalNum,frame)
