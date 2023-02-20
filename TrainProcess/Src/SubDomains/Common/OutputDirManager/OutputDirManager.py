import os

class OutputDirManager:
    OUTPUT_DIR_NAME="Output"
    @staticmethod
    def isLastModelExist()->bool:
        pass
    @staticmethod
    def getLastModelPath()->str:
        pass
    @staticmethod
    def getOutputDirPath()->str:
        currentPath = os.getcwd()
        return os.path.join(currentPath,OutputDirManager.OUTPUT_DIR_NAME)