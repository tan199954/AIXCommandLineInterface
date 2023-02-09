from InitProcess.Src.AbstractFactory.Interfaces.IInitAbstracFactory import IInitAbstractFactory
from InitProcess.Src.AbstractFactory.Interfaces.IInitFactory import IInitFactory
from InitProcess.Src.Core.Models.InitEnum import InitType
from InitProcess.Src.AbstractFactory.Implementation.YOLOInitFactory import YOLOInitFactory
from InitProcess.Src.AbstractFactory.Implementation.YOROInitFactory import YOROInitFactory

class InitAbstractFactory(IInitAbstractFactory):
     def getFactory(self,initType:InitType)->IInitFactory:
          if initType == InitType.YOLO:
               return YOLOInitFactory()
          return YOROInitFactory()

          