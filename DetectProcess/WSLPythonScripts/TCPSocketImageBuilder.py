from PySide6 import QtCore
import numpy as np

class TCPSocketImageBuilder(QtCore.QObject):
    TOTAL_NUM_LEN = 12
    SHAPE_NUMBER = 3
    WIDTH_POSITION = 0
    HIGHT_POSITION = 4
    CHANGES_POSITION = 8
    FIRST_QBYRTEARRAY_POSITION = 0
    imageBuilt = QtCore.Signal(np.ndarray)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.totalNum = int()
        self.height = int()
        self.width = int()
        self.channels = int()
        self.imageData = QtCore.QByteArray()
        self.latestUnusedData = QtCore.QByteArray()
    def buildImageFromData(self,data:QtCore.QByteArray):
        curentData = self.latestUnusedData.append(data)
        self.latestUnusedData = QtCore.QByteArray()
        if (not self.__hasBeenTotalNum()):
            self.__setTotalNum(curentData)
            return
        self.__appendImageData(curentData)
        if (not self.__imageDataIsFull()):
            return
        self.ImageBuilt.emit(self.__convertImageData2Ndarry())
    def __hasBeenTotalNum(self):
        return self.totalNum >0
    def __setTotalNum(self, data:QtCore.QByteArray):
        shapeData = data[:self.TOTAL_NUM_LEN]
        widthData = shapeData[self.WIDTH_POSITION:self.HIGHT_POSITION].data()[::-1]
        heightData = shapeData[self.HIGHT_POSITION:self.CHANGES_POSITION].data()[::-1]
        channelsData = shapeData[self.CHANGES_POSITION:self.TOTAL_NUM_LEN].data()[::-1]
        self.width = int.from_bytes(widthData, "big")
        self.height = int.from_bytes(heightData, "big")
        self.channels = int.from_bytes(channelsData, "big")
        self.totalNum = self.width * self.height * self.channels        
        data.remove(self.FIRST_QBYRTEARRAY_POSITION,self.TOTAL_NUM_LEN)
        self.__appendImageData(data)
    def __appendImageData(self, data:QtCore.QByteArray):
        dataLength = data.length()
        if (self.totalNum>=dataLength):
            self.imageData.append(data)
            self.totalNum -= dataLength
        else:
            lastImageData = data[:self.totalNum]
            self.imageData.append(lastImageData)
            nextImageData =  data.remove(self.FIRST_QBYRTEARRAY_POSITION,self.totalNum)
            self.__setLatestUnusedData(nextImageData)
            self.totalNum -= lastImageData.length()
    def __setLatestUnusedData(self,newLatestUnusedData:QtCore.QByteArray):
        self.latestUnusedData = newLatestUnusedData       
    def __convertImageData2Ndarry(self):
        data = np.frombuffer(self.imageData, dtype='uint8')
        return data.reshape(self.height, self.width, self.channels)
    def __imageDataIsFull(self):
        return self.totalNum <= 0