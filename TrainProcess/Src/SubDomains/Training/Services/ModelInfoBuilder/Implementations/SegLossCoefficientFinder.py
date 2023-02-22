from typing import List
from .....Common.DataTypeChecker.DataTypeChecker import DataTypeChecker


class SegLossCoefficientFinder:
     LOSS_KEY="dfl_loss"
     TARGET_KEY="R"
     FRONT_LOSS_INDEX_OFFSET=-11
     REAR_LOSS_INDEX_OFFSET=38
     BAD_STRINGS=["|","█"]
     def getLossFrStr(self,stringData:str)->float:
          goodString=self.__getGoodStringData(stringData)
          wordList=[word for word in goodString.split() if word]
          if not self.__isConstaninRequireKeys(wordList):
               return None
          targetIndex=wordList.index(self.TARGET_KEY)
          frontLossIndex=targetIndex+self.FRONT_LOSS_INDEX_OFFSET
          rearLossIndex=targetIndex+self.REAR_LOSS_INDEX_OFFSET
          lossStringData = self.__getLossStringData(wordList,frontLossIndex,rearLossIndex)
          for element in lossStringData:
               if DataTypeChecker.strIsFloat(element):
                    return float(element)
          return None
     def __getGoodStringData(self,stringData:str)->str:
          newStringData=stringData
          for badStr in self.BAD_STRINGS:
               newStringData=newStringData.replace(badStr,"")
          return newStringData
     def __isConstaninRequireKeys(self,wordList:List[str])->str:
          return self.LOSS_KEY in wordList and self.TARGET_KEY in wordList
     def __getLossStringData(self,wordList:List[str],frontLossIndex,rearLossIndex):
          stringData = list()
          if self.__isInOfRange(wordList,rearLossIndex):
               stringData.append(wordList[rearLossIndex])
          if self.__isInOfRange(wordList,frontLossIndex):
               stringData.append(wordList[frontLossIndex])
          return stringData
     def __isInOfRange(self,wordList:List[str],index)->bool:
          return 0 <= index < len(wordList)

          