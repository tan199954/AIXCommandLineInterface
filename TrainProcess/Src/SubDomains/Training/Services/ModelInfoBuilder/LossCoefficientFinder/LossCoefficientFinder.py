
from typing import List
from .....Common.DataTypeChecker.DataTypeChecker import DataTypeChecker
from .AbstractLossCoefficientFinder import AbstractYOLOLossCoefficientFinder


class SegLossCoefficientFinder(AbstractYOLOLossCoefficientFinder):
     @property
     def LOSS_INDEX(self)->int:
          return 5

class BoxLossCoefficientFinder(AbstractYOLOLossCoefficientFinder):
     @property
     def LOSS_INDEX(self)->int:
          return 4

class BBoxLossCoefficientFinder:
     LOSS_KEY="Loss:"
     LOSS_INDEX_OFFSET=1
     @staticmethod
     def getLossfrStringData(stringData:str):
          """
          Return LOSS  if it constanin in the stringData,\n
          Else return None
          """
          wordList=[word for word in stringData.split() if word]
          if not BBoxLossCoefficientFinder.LOSS_KEY in wordList:
               return
          iouIndex=wordList.index(BBoxLossCoefficientFinder.LOSS_KEY) + BBoxLossCoefficientFinder.LOSS_INDEX_OFFSET
          if not BBoxLossCoefficientFinder.__isInOfRange(wordList,iouIndex):
               return
          return BBoxLossCoefficientFinder.__getFloatFrStr(wordList[iouIndex])
     def __isInOfRange(wordList:List[str],index)->bool:
          return 0 <= index < len(wordList)
     def __getFloatFrStr(stringData:str):
          """
          Return decimals number, if it constanin in the stringData,\n
          Else return None 
          """
          decimals = ""
          for c in stringData:
               if c.isdigit() or c == ".":
                    decimals += c
          if DataTypeChecker.strIsFloat(decimals):
               return float(decimals)

          