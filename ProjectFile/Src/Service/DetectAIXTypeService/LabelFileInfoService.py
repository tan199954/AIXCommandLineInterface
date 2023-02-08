from PySide6 import QtCore
import yaml

class YOLOFileInfo:
     NUMBER_OF_BOX_PARAMETER = 5 #id, x, y,w,h
     def __init__(self,txtFileInfo:QtCore.QFileInfo) -> None:
          file = QtCore.QFile(txtFileInfo.filePath())
          if not file.exists():
               raise Exception(f"{txtFileInfo.filePath()} is not exists")
          file.open(QtCore.QFile.ReadOnly | QtCore.QFile.Text)
          self.firstLine = file.readLine()
          file.close()
     def isBoxFormat(self)->bool:
          if len(self.firstLine.data().decode().split(" "))==self.NUMBER_OF_BOX_PARAMETER:
               return True
          return False
     def isSegmentFormat(self)->bool:
          if len(self.firstLine.data().decode().split(" "))>self.NUMBER_OF_BOX_PARAMETER:
               return True
          return False
class YOROFileInfo:
     # Example data of markFile:
     # [{'label': 1, 'degree': -48.03114950830552, 'x': 355.2804642166344, 'y': 183.71134020618558, 
     # 'w': 139.4423356941823, 'h': 97.68724133985069},
     # {'label': 0, 'degree': 42.114551599074474, 'x': 173.61702127659578, 'y': 337.42268041237116, 
     # 'w': 123.53840472389126, 'h': 120.85490095921293}]
     DATA_KEYS = ["label","x","y","w","h","degree"]
     def __init__(self,markFileInfo:QtCore.QFileInfo) -> None:
          file = QtCore.QFile(markFileInfo.filePath())
          if not file.exists():
               raise Exception(f"{markFileInfo.filePath()} is not exists")
          with open(markFileInfo.filePath(),"r") as markFile:
            self.markData=yaml.load(markFile,Loader=yaml.FullLoader)
          markFile.close()
     def isMarkFormat(self)->bool:
          firstData=self.markData[0]
          for key in self.DATA_KEYS:
               if key not in firstData.keys():
                    return False
          return True