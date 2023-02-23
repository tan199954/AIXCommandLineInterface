from ....Exceptions.DatasetError import DatasetQualityError
from ...CommandPromptService.CommandPromptService import CommandPromptService
from ...ModelEvaluator.ModelEvaluator import ModelEvaluator
from ...ModelInfoBuilder.Implementations.SegModelInfoBuilder import SegModelInfoBuilder, ModelInfo
from ...CommandLineGeneratorService.Implementations.SegCLIGererator import SegCLIGererator
from .AbstractTrainer import AbstractQCoreAppTrainer

class SegTrainer(AbstractQCoreAppTrainer):
    def defineMainFuncitionOfQCoreAppThread(self):
        self.segCLIGererator=SegCLIGererator()
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
        commandLine=self.segCLIGererator.getCommadLine()
        self.CMDService.commandLine=commandLine
        self.CMDService.start()
    def __stopTrain(self):
        self.CMDService.stop()
    def __decreaseLearningRate(self):
        self.__stopTrain()
        self.segCLIGererator.decreaseLearningRate()
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
        model=SegModelInfoBuilder().buildFromStr(result)
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