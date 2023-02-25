from .AbstractOutputManager import AbstractOutputManager

class BBoxOutputManager(AbstractOutputManager):
    MODEL_DIR_NAME="models.backup"
    MODEL_FILE_EXTENSION=".sdict"
    def getLastModelPath()->str:
        pass
    def isLastModelExist()->bool:
        pass