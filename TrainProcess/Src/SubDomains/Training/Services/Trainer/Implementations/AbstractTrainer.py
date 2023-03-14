from abc import abstractproperty
from PySide6.QtCore import QThread
from .....Common.ApplicationThread.ApplicationThread import AbstractQCoreApplicationThreadManager
from .....Common.CommandPromptService.CommandPromptService import CommandPromptService
from ....Exceptions.DatasetError import DatasetQualityError
from ...ModelEvaluator.ModelEvaluator import ModelEvaluator,ModelInfo
from ...ModelInfoBuilder.Interfaces.IModelInfoBuilder import IModelInfoBuilder
from ...TrainCommandLineGeneratorService.Implementations.AbstractYOLOCLIGererator import AbstractYOLOCLIGererator
from ..Interfaces.ITrainer import ITrainer


class AbstractYOLOTrainer(AbstractQCoreApplicationThreadManager,ITrainer):
     def __init__(self,manual:bool=False) -> None:
          super().__init__()
          manual=manual or False
          self.manual=manual
     @abstractproperty
     def YOLOCLIGenerator(self)->AbstractYOLOCLIGererator:
          pass
     @abstractproperty
     def modelInfoBuilder(self)->IModelInfoBuilder:
          pass
     def train(self):
          self.execute()
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
          commandLine=self.YOLOCLIGenerator.getCommandLine()
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
          self.quitQCoreAppThread()
          raise DatasetQualityError('The dataset is low quality, please check the dataset')
     def __onBestModelFound(self):
          QThread.sleep(2)
          self.quitQCoreAppThread()
     def __onErrorFinished(self,error:str):
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