from PySide6.QtCore import Qt,QCoreApplication
from ....Exceptions.DatasetError import DatasetQualityError
from ...CommandPromptService.CommandPromptService import CommandPromptService
from ...ModelEvaluator.ModelEvaluator import ModelEvaluator
from ...ModelInfoBuilder.Implementations.SegModelInfoBuilder import SegModelInfoBuilder, ModelInfo
from ...CommandLineGeneratorService.Implementations.SegCLIGererator import SegCLIGererator
from .AbstractTrainer import AbstractQCoreAppTrainer

class SegTrainer(AbstractQCoreAppTrainer):
    def definePySide6Classes(self):
        self.segCLIGererator=SegCLIGererator()
        self.CMDService=CommandPromptService()
        self.modelEvaluator=ModelEvaluator()
        self.CMDService.finished.connect(self.__onFinished)
        self.CMDService.errorFinished.connect(self.__onErrorFinished)
        self.CMDService.outputReceived.connect(self.__onResultReceived)
        self.CMDService.errorReceived.connect(self.__onResultReceived)
        self.modelEvaluator.bestModelFound.connect(lambda: self.__stopTrain())
        self.modelEvaluator.learningRateMustDecrease.connect(self.__decreaseLearningRate)
        self.modelEvaluator.datasetLowQuality.connect(self.__onDatasetLowQuality)
        self.__startTrain()
    def __startTrain(self):
        commandLine=self.segCLIGererator.getCommadLine()
        self.CMDService.commandLine=commandLine
        self.CMDService.start()
    def __stopTrain(self):
        self.CMDService.stop()
        self.app.quit()
    def __decreaseLearningRate(self):
        self.CMDService.stop()
        self.segCLIGererator.decreaseLearningRate()
        self.__startTrain()
    def __onDatasetLowQuality(self):
        self.__stopTrain()
        raise DatasetQualityError('The dataset is low quality, please check the dataset')
    def __onResultReceived(self,result:str):
        print("__onResultReceived")
        model=SegModelInfoBuilder().buildFromStr(result)
        if isinstance(model,ModelInfo):
            self.modelEvaluator.evaluate(model)
            print("modelEvaluator.evaluate")
    def __onErrorFinished(self,error:str):
        self.__stopTrain()
        raise RuntimeError(error)
    def __onFinished(self):
        """
        If the 'bestModelFound' signal has not been emitted after the cmdService finished,
        continue training.
        """
        self.__startTrain()