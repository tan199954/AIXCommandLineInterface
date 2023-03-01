from ....Common.YOROConfigFile.YOROConfigFile import YOROConfigFile


class LearningRateDecrementor:
    LR_DECREASE_FACTOR =10
    @staticmethod
    def decrease():
        currentLr=LearningRateDecrementor.__getCurrentLr()
        newLr=currentLr/LearningRateDecrementor.LR_DECREASE_FACTOR
        LearningRateDecrementor.__updateLr(newLr)
    def __getCurrentLr()->float:
        data=YOROConfigFile.getCurrentData()
        return data["optimizer"]["args"]["lr"]
    def __updateLr(newLr):
        newLrData = {"optimizer":{
            "args":{
            "lr":newLr
            }
        }}
        YOROConfigFile.updateData(newLrData)