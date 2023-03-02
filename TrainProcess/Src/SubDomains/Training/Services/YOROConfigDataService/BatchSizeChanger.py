from ....Common.YOROConfigFile.YOROConfigFile import YOROConfigFile

class BatchSizeChanger:
    @staticmethod
    def change(newBatchSize:int):
        newIterData = {"train_param":{
            "batch":newBatchSize
        }}
        YOROConfigFile.updateData(newIterData)