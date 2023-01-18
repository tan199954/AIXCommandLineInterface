import os
import sys
currentFilePath=os.path.abspath(__file__)
testsPath=os.path.dirname(currentFilePath)
modulePath=os.path.dirname(testsPath)
parentPath=os.path.dirname(modulePath)
sys.path.append(parentPath)
from PySide6 import QtCore

import unittest

from InitProcess.Src.Service.LabelFileInfoService import TxtFileInfo,MarkFileInfo

class TestTxtFileInfo(unittest.TestCase):
    def testTxtBoxFileInfo(self):
        txtFileInfo = TxtFileInfo(QtCore.QFileInfo(testsPath+"/boxLabelPath/test.txt"))
        txtBoxFormat=txtFileInfo.isBoxFormat()
        self.assertEqual(True,txtBoxFormat)
    def testTxtBoxFileInfo(self):
        txtFileInfo = TxtFileInfo(QtCore.QFileInfo(testsPath+"/segLabelPath/test.txt"))
        txtSegFormat=txtFileInfo.isSegmentFormat()
        self.assertEqual(True,txtSegFormat)
class TestMarkFileInfo(unittest.TestCase):
    def testMarkFileInfo(self):
        markFileInfo = MarkFileInfo(QtCore.QFileInfo(testsPath+"/bbLabelPath/test.jpg.mark"))
        markFormat=markFileInfo.isMarkFormat()
        self.assertEqual(True,markFormat)
if __name__=="__main__":
     unittest.main()