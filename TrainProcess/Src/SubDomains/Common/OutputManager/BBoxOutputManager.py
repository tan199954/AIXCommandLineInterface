import os
from .AbstractOutputManager import AbstractOutputManager


class BBoxOutputManager(AbstractOutputManager):
    MODEL_DIR_NAME="models.backup"
    MODEL_FILE_EXTENSION=".sdict"
    LAST_MODEL_FILE_INDEX=0
    def getLastModelFilePath(self)->str:
        """
        Return last model file path (string), if it is exists.\n
        Else return None
        """
        backupDir=self.__getBackupDir()
        if not os.path.exists(backupDir):
            return
        backupFiles=os.listdir(backupDir)
        modelFiles=[os.path.join(backupDir, file) for file in backupFiles if file.endswith(self.MODEL_FILE_EXTENSION)]
        sortedModelFiles = sorted(modelFiles, key=lambda filePath: os.path.getmtime(filePath),reverse=True)   
        if not sortedModelFiles:
            return
        return sortedModelFiles[self.LAST_MODEL_FILE_INDEX]
    def __getBackupDir(self)->str:
        outputDirPath=AbstractOutputManager.getOutputDirPath()
        return os.path.join(outputDirPath,self.MODEL_DIR_NAME)