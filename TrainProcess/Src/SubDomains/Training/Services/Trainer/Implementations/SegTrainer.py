from PySide6.QtCore import Qt,QCoreApplication
from ....Exceptions.DatasetError import DatasetQualityError
from ..Interfaces.ITrainer import ITrainer
from ...CommandPromptService.CommandPromptService import CommandPromptService
from ...ModelEvaluator.ModelEvaluator import ModelEvaluator

class SegTrainer(ITrainer):
    def __init__(self,manual:bool=False) -> None:
        super().__init__()
        self.segCMLGenerator=SegCLIGenerator()
        self.CMDService=CommandPromptService()
        self.modelEvaluator=ModelEvaluator()
        self.app = QCoreApplication()
        self.CMDService.finished.connect(self.__onFinished)
        self.CMDService.errorFinished.connect(self.__onErrorFinished)
        self.CMDService.resultReceived.connect(self.__onResultReceived)
        self.modelEvaluator.bestModelFound.connect(lambda: self.__stopTrain())
        self.modelEvaluator.learningRateMustChange.connect(self.__changeLearningRate)
        self.modelEvaluator.datasetLowQuality.connect(self.__onDatasetLowQuality)
    def execute(self):
        self.__startTrain()
        self.app.exec()
    def __startTrain(self,changeLearningRate:bool=False):
        commandLine=self.segCMLGenerator.getcommandLine(changeLearningRate)
        self.CMDService.commandLine=commandLine
        self.CMDService.start()
    def __stopTrain(self):
        self.CMDService.stop()
        self.app.quit()
    def __changeLearningRate(self):
        self.CMDService.stop()
        self.__startTrain(True)
    def __onDatasetLowQuality(self):
        self.__stopTrain()
        raise DatasetQualityError('The dataset is low quality, please check the dataset')
    def __onResultReceived(self,result:str):
        #builDerfromString
        #model=trainResultReader.onResultReceived(resultDictionary)
        #self.modelEvaluator.evaluate(model)
        pass
    def __onErrorFinished(self,error:str):
        self.__stopTrain()
        raise RuntimeError(error)
    def __onFinished(self):
        """
        If the 'bestModelFound' signal has not been emitted after the cmdService finished,
        continue training.
        """
        self.__startTrain()

