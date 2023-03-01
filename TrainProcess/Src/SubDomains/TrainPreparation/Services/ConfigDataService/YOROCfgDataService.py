from ....Common.PathConverter.PathConverter import PathConverter
from ....Common.YOROConfigFile.YOROConfigFile import YOROConfigFile

class YOROCfgDataService:
    SAMPLE_CFG_FILE_PATH=r"SampleFiles\YOROConfig.yaml"
    BATCH_SIZE_DEFAULT=32
    def __init__(self, gpuMenmory: int, trainPath: str, 
                 validPath: str,namesFilePath:str) -> None:
        self.gpuMenmory=gpuMenmory
        self.trainPath=trainPath
        self.validPath=validPath
        self.namesFilePath=namesFilePath
    def _getNewMaxIter(self,oldMaxIter:int):
        return oldMaxIter+3000
    def _getNewLr(self,oldMaxIter:float):
        return oldMaxIter/10
    def _getBathSize(self):
        #update later
        return self.BATCH_SIZE_DEFAULT
    def getNewConfigData(self):
        oldCofigData=YOROConfigFile.getCurrentData()
        oldMaxIter=oldCofigData["train_param"]["max_iter"]
        return {
            "dataset": {
                "names_file":PathConverter.Windows2WSL(self.namesFilePath),
                "train_dir":PathConverter.Windows2WSL(self.trainPath),
                "valid_dir":PathConverter.Windows2WSL(self.validPath)
            },
            "train_param":{
                "batch":self._getBathSize(),
                "max_iter":self._getNewMaxIter(oldMaxIter)
            }
        }