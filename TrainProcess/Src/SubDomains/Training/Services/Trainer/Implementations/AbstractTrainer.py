import signal
from abc import abstractclassmethod, abstractproperty
from .....Common.ApplicationThread.ApplicationThread import QCoreApplicationThread
from .....Common.CommandPromptService.CommandPromptService import CommandPromptService
from ....Exceptions.DatasetError import DatasetQualityError
from ...ModelEvaluator.ModelEvaluator import ModelEvaluator,ModelInfo
from ...ModelInfoBuilder.Interfaces.IModelInfoBuilder import IModelInfoBuilder
from ...TrainCommandLineGeneratorService.Implementations.AbstractYOLOCLIGererator import AbstractYOLOCLIGererator
from ..Interfaces.ITrainer import ITrainer
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

class AbstractYOLOTrainer(AbstractQCoreAppTrainer):
     def __init__(self,manual:bool=False) -> None:
          super().__init__()
          self.manual=manual
     @abstractproperty
     def YOLOCLIGenerator(self)->AbstractYOLOCLIGererator:
          pass
     @abstractproperty
     def modelInfoBuilder(self)->IModelInfoBuilder:
          pass
     def defineMainFuncitionOfQCoreAppThread(self):
          self.CMDService=CommandPromptService()
          if not self.manual:
               self.modelEvaluator=ModelEvaluator()
               self.modelEvaluator.bestModelFound.connect(self.__onBestModelFound)
               self.modelEvaluator.learningRateMustDecrease.connect(self.__decreaseLearningRate)
               self.modelEvaluator.datasetLowQuality.connect(self.__onDatasetLowQuality)
          self.appThr.app.aboutToQuit.connect(self.__cleanUpPySide6Classes)
          self.__startTrain()
     def __startTrain(self):
          self.CMDService.finished.connect(self.__onFinished)
          self.CMDService.errorFinished.connect(self.__onErrorFinished)
          self.CMDService.outputReceived.connect(self.__onResultReceived)
          self.CMDService.errorReceived.connect(self.__onResultReceived)
          commandLine=self.YOLOCLIGenerator.getCommadLine()
          self.CMDService.commandLine=commandLine
          self.CMDService.start()
     def __stopTrain(self):
          try:
               self.CMDService.finished.disconnect(self.__onFinished)
               self.CMDService.errorFinished.disconnect(self.__onErrorFinished)
               self.CMDService.outputReceived.disconnect(self.__onResultReceived)
               self.CMDService.errorReceived.disconnect(self.__onResultReceived)
          except:
               pass
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
          model=self.modelInfoBuilder.buildFromStr(result)
          if isinstance(model,ModelInfo):
               print(f"iou: {model.iOU}, loss: {model.loss}, map: {model.mAP}")
               self.modelEvaluator.evaluate(model)
     def __onFinished(self):
          """
          If the 'bestModelFound' signal has not been emitted after the cmdService finished,
          continue training.
          """
          self.__stopTrain()
          if not self.manual:
               self.__startTrain()
          else:
               self.quitQCoreAppThread()
     def __cleanUpPySide6Classes(self):
          self.__stopTrain()