from typing import List
from .....Common.DataTypeChecker.DataTypeChecker import DataTypeChecker

class SegMAPCoefficientFinder:
     TARGET_KEY="all"
     MAP_INDEX_OFFSET=10
     def getMAPFrStr(self,stringData:str)->float:
          wordList=[word for word in stringData.split() if word]
          if not self.__isConstaninRequireKeys(wordList):
               return None
          targetIndex=wordList.index(self.TARGET_KEY)
          mAPIndex=targetIndex+self.MAP_INDEX_OFFSET
          if not self.__isInOfRange(wordList,mAPIndex):
               return None
          if not DataTypeChecker.strIsFloat(wordList[mAPIndex]):
               return None
          return float(wordList[mAPIndex])
     def __isConstaninRequireKeys(self,wordList:List[str]):
          return self.TARGET_KEY in wordList
     def __isInOfRange(self,wordList:List[str],index)->bool:
          return 0 <= index < len(wordList)