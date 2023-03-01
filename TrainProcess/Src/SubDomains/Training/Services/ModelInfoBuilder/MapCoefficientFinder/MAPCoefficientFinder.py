from typing import List
from .....Common.DataTypeChecker.DataTypeChecker import DataTypeChecker
from .AbstractMAPCoefficientFinder import AbstractYOLOMAPCoefficientFinder
     
class SegMAPCoefficientFinder(AbstractYOLOMAPCoefficientFinder):
     @property
     def MAP_INDEX_OFFSET(self)->int:
          return 10

class BoxMAPCoefficientFinder(AbstractYOLOMAPCoefficientFinder):
     @property
     def MAP_INDEX_OFFSET(self)->int:
          return 6

class BBoxMAPCoefficientFinder:
     MAP_KEY="{mAP:"
     MAP_INDEX_OFFSET=1
     @staticmethod
     def getMAPfrStringData(stringData:str):
          """
          Return MAP  if it constanin in the stringData,\n
          Else return None
          """
          wordList=[word for word in stringData.split() if word]
          if not BBoxMAPCoefficientFinder.MAP_KEY in wordList:
               return
          iouIndex=wordList.index(BBoxMAPCoefficientFinder.MAP_KEY) + BBoxMAPCoefficientFinder.MAP_INDEX_OFFSET
          if not BBoxMAPCoefficientFinder.__isInOfRange(wordList,iouIndex):
               return
          return BBoxMAPCoefficientFinder.__getFloatFrStr(wordList[iouIndex])
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