from .AbstractOutputManager import AbstractOutputManager

class BBoxOutputManager(AbstractOutputManager):
    def MODEL_DIR_NAME(self)->str:
        pass
    def getLastModelPath()->str:
        pass
    def isLastModelExist()->bool:
        pass