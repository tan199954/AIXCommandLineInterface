from typing import List
from abc import ABC,abstractproperty
from .....Common.DataTypeChecker.DataTypeChecker import DataTypeChecker


class AbstractYOLOLossCoefficientFinder(ABC):
     TARGET_KEY="G"
     TARGET_INDEX=1
     BAD_STRINGS=["|","█"]
     @abstractproperty
     def LOSS_INDEX(self)->int:
          pass
     def getLossFrStr(self,stringData:str)->float:
          goodString=self.__getGoodStringData(stringData)
          wordList=[word for word in goodString.split() if word]
          if not self.__isConstaninRequireKeys(wordList):
               return None
          lossStringData = self.__getLossStringData(wordList)
          if DataTypeChecker.strIsFloat(lossStringData):
               return float(lossStringData)
          return None
     def __getGoodStringData(self,stringData:str)->str:
          newStringData=stringData
          for badStr in self.BAD_STRINGS:
               newStringData=newStringData.replace(badStr,"")
          return newStringData
     def __isConstaninRequireKeys(self,wordList:List[str])->str:
          targetValue=wordList[self.TARGET_INDEX]
          return self.TARGET_KEY in targetValue
     def __getLossStringData(self,wordList:List[str]):
          if self.__isInOfRange(wordList,self.LOSS_INDEX):
               return wordList[self.LOSS_INDEX]
          return None
     def __isInOfRange(self,wordList:List[str],index)->bool:
          return 0 <= index < len(wordList)
     
class SegLossCoefficientFinder(AbstractYOLOLossCoefficientFinder):
     @property
     def LOSS_INDEX(self)->int:
          return 5

class BoxLossCoefficientFinder(AbstractYOLOLossCoefficientFinder):
     @property
     def LOSS_INDEX(self)->int:
          return 4

          