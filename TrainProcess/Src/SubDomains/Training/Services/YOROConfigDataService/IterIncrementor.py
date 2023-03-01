import os
from ....Common.YOROConfigFile.YOROConfigFile import YOROConfigFile
from ....Common.OutputManager.BBoxOutputManager import BBoxOutputManager


class IterIncrementor:
    MIN_ITER=0
    @staticmethod
    def increase():
        currentIter=IterIncrementor.__getCurrentIter()
        newIter=currentIter + 3000
        IterIncrementor.__updateIter(newIter)
    def __getCurrentIter()->int:
        lastModelFilePath = BBoxOutputManager.getLastModelFilePath()
        if not isinstance(lastModelFilePath,str):
            return IterIncrementor.MIN_ITER
        return IterIncrementor.__getIterFromLastModelFilePath(lastModelFilePath)
    def __updateIter(newIter):
        newIterData = {"train_param":{
            "max_iter":newIter
        }}
        YOROConfigFile.updateData(newIterData)
    def __getIterFromLastModelFilePath(lastModelFilePath:str)->int:
        baseFileName=os.path.basename(lastModelFilePath)
        fileName=os.path.splitext(baseFileName)[0]
        digits = ""
        for c in fileName:
            if c.isdigit():
                digits += c
        if digits != "":
            return int(digits)
        return IterIncrementor.MIN_ITER