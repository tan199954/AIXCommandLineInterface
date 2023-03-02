from .....Common.CommandPromptService.CommandPromptService import CommandPromptService
from .....Common.ApplicationThread.ApplicationThread import AbstractQCoreApplicationThreadManager
from ....Exceptions.DatasetError import DatasetQualityError
from ...ModelEvaluator.ModelEvaluator import ModelEvaluator
from ...TrainCommandLineGeneratorService.Implementations.BBoxCLIGererator import BBoxCLIGererator 
from ...ModelInfoBuilder.Implementations.BBoxModelInfoBuilder import ModelInfo, BBoxModelInfoBuilder
from ...YOROConfigDataService.IterIncrementor import IterIncrementor
from ...YOROConfigDataService.LearningRateDecrementor import LearningRateDecrementor
from ...YOROConfigDataService.BatchSizeChanger import BatchSizeChanger
from ..Interfaces.ITrainer import ITrainer



class BBoxTrainer(AbstractQCoreApplicationThreadManager,ITrainer):
    def __init__(self,learningRate:float,imageSize:int,batchSize:int,manual:bool=False) -> None:
          super().__init__()
          manual=manual or False
          self.manual=manual
          self.__updateConfigParams(batchSize)
    def __updateConfigParams(self,batchSize):
        if isinstance(batchSize,int):
              BatchSizeChanger.change(batchSize)
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
        IterIncrementor.increase()
        commandLine=BBoxCLIGererator().getCommandLine()
        self.CMDService.commandLine=commandLine
        self.CMDService.start()
    def __stopTrain(self):
        try:
            self.CMDService.finished.disconnect(self.__onFinished)
            self.CMDService.errorFinished.disconnect(self.__onErrorFinished)
            self.CMDService.outputReceived.disconnect(self.__onResultReceived)
        except:
            pass
        self.CMDService.stop()
    def __decreaseLearningRate(self):
        self.__stopTrain()
        LearningRateDecrementor.decrease()
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
        model=BBoxModelInfoBuilder.buildFromStr(result)
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