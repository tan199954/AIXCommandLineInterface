from InitProcess.Src.Core import ProjInputChecker
from InitProcess.Src.Service.LabelFileInfoService import TxtFileInfo,MarkFileInfo
from PySide6 import QtCore

class BoxProjInputChecker(ProjInputChecker):
     def check(self):
          self.checkLabel()
     def checkLabel(self):
          #check contain label file
          filters = [ "*.txt"]
          fileInfoList = QtCore.QDir(self.labelPath).entryInfoList(filters, QtCore.QDir.Files|QtCore.QDir.NoDotAndDotDot)
          if not fileInfoList:
               raise Exception(f"{self.labelPath} is not contain label (*.txt Files)")
          #check File is format true
          self.checkFile(fileInfoList[0])
     def checkFile(self,txtFileInfo:QtCore.QFileInfo):
          txtInfo=TxtFileInfo(txtFileInfo)
          if not txtInfo.isBoxFormat():
               raise Exception("Label file is not Box format")
class BBoxProjInputChecker(ProjInputChecker):
     def check(self):
          self.checkLabel()
     def checkLabel(self):
          #check contain label file
          filters = [ "*.mark"]
          fileInfoList = QtCore.QDir(self.labelPath).entryInfoList(filters, QtCore.QDir.Files|QtCore.QDir.NoDotAndDotDot)
          if not fileInfoList:
               raise Exception(f"{self.labelPath} is not contain label (*.mark Files)")
          #check File is format true
          self.checkFile(fileInfoList[0])
     def checkFile(self,markFileInfo:QtCore.QFileInfo):
          markInfo=MarkFileInfo(markFileInfo)
          if not markInfo.isMarkFormat():
               raise Exception("Label file is not BoundingBox format")
class SegProjInputChecker(ProjInputChecker):
     def check(self):
          self.checkLabel()
     def checkLabel(self):
          #check contain label file
          filters = [ "*.txt"]
          fileInfoList = QtCore.QDir(self.labelPath).entryInfoList(filters, QtCore.QDir.Files|QtCore.QDir.NoDotAndDotDot)
          if not fileInfoList:
               raise Exception(f"{self.labelPath} is not contain label (*.txt Files)")
          #check File is format true
          self.checkFile(fileInfoList[0])
     def checkFile(self,txtFileInfo:QtCore.QFileInfo):
          txtInfo=TxtFileInfo(txtFileInfo)
          if not txtInfo.isSegmentFormat():
               raise Exception("Label file is not Segment format")