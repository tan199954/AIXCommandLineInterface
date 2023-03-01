from typing import List
from .....Common.DataTypeChecker.DataTypeChecker import DataTypeChecker


class BBoxIOUCoefficientFinder:
     IOU_KEY="iou:"
     IOU_INDEX_OFFSET=1
     @staticmethod
     def getIOUfrStringData(stringData:str):
          """
          Return IOU  if it constanin in the stringData,\n
          Else return None
          """
          wordList=[word for word in stringData.split() if word]
          if not BBoxIOUCoefficientFinder.IOU_KEY in wordList:
               return
          iouIndex=wordList.index(BBoxIOUCoefficientFinder.IOU_KEY) + BBoxIOUCoefficientFinder.IOU_INDEX_OFFSET
          if not BBoxIOUCoefficientFinder.__isInOfRange(wordList,iouIndex):
               return
          return BBoxIOUCoefficientFinder.__getFloatFrStr(wordList[iouIndex])
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