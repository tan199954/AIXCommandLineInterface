import signal
from PySide6 import QtCore
from abc import abstractclassmethod, abstractproperty
from .....Common.ApplicationThread.ApplicationThread import QCoreApplicationThread
from ..Interfaces.ITrainer import ITrainer

from ....Exceptions.DatasetError import DatasetQualityError
from ...CommandPromptService.CommandPromptService import CommandPromptService
from ...ModelEvaluator.ModelEvaluator import ModelEvaluator,ModelInfo
from ...ModelInfoBuilder.Interfaces.IModelInfoBuilder import IModelInfoBuilder
from ...CommandLineGeneratorService.Implementations.AbstractYOLOCLIGererator import AbstractYOLOCLIGererator
from .AbstractTrainer import AbstractQCoreAppTrainer


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

class AbstractYOLOTrainer(AbstractQCoreAppTrainer):
     @abstractproperty
     def YOLOCLIGenerator(self)->AbstractYOLOCLIGererator:
          pass
     @abstractproperty
     def modelInfoBuilder(self)->IModelInfoBuilder:
          pass
     def defineMainFuncitionOfQCoreAppThread(self):
          self.CMDService=CommandPromptService()
          self.modelEvaluator=ModelEvaluator()
          self.CMDService.finished.connect(self.__onFinished)
          self.CMDService.errorFinished.connect(self.__onErrorFinished)
          self.CMDService.outputReceived.connect(self.__onResultReceived)
          self.CMDService.errorReceived.connect(self.__onResultReceived)
          self.modelEvaluator.bestModelFound.connect(self.__onBestModelFound)
          self.modelEvaluator.learningRateMustDecrease.connect(self.__decreaseLearningRate)
          self.modelEvaluator.datasetLowQuality.connect(self.__onDatasetLowQuality)
          self.appThr.finished.connect(self.__cleanUpPySide6Classes)
          self.__startTrain()
     def __startTrain(self):
          commandLine=self.YOLOCLIGenerator.getCommadLine()
          self.CMDService.commandLine=commandLine
          self.CMDService.start()
     def __stopTrain(self):
          self.CMDService.stop()
     def __decreaseLearningRate(self):
          self.__stopTrain()
          self.YOLOCLIGenerator.decreaseLearningRate()
          self.__startTrain()
     def __onDatasetLowQuality(self):
          self.__stopTrain()
          self.quitQCoreAppThread()
          raise DatasetQualityError('The dataset is low quality, please check the dataset')
     def __onBestModelFound(self):
          self.__stopTrain()
          self.quitQCoreAppThread()
     def __onErrorFinished(self,error:str):
          self.__stopTrain()
          self.quitQCoreAppThread()
          raise RuntimeError(error)
     def __onResultReceived(self,result:str):
          print(f"result: {result}")
          model=self.modelInfoBuilder.buildFromStr(result)
          if isinstance(model,ModelInfo):
               self.modelEvaluator.evaluate(model)
               print("modelEvaluator.evaluate")
     def __onFinished(self):
          """
          If the 'bestModelFound' signal has not been emitted after the cmdService finished,
          continue training.
          """
          self.__stopTrain()
          self.__startTrain()
     def __cleanUpPySide6Classes(self):
          self.CMDService.stop()
