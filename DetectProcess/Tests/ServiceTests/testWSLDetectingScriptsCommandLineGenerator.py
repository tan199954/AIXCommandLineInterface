import os
import sys
currentFilePath=os.path.abspath(__file__)
ServiceTestsPath=os.path.dirname(currentFilePath)
TestsPath=os.path.dirname(ServiceTestsPath)
modulePath=os.path.dirname(TestsPath)
parentPath=os.path.dirname(modulePath)
sys.path.append(parentPath)
import unittest
def cwd():
     return TestsPath
os.getcwd =cwd

from DetectProcess.Src.Services.WSLDetectingScriptCommandExecutor.WSLDetectingScriptCommandLineGenerator import (WSLDetectingScriptCommandLineGenerator, DetectType)
from DetectProcess.Src.Services.Common.PathConverter.PathConverter import PathConverter

class TestWSLDetectingScriptCommandLineGenerator(unittest.TestCase):
     def testGetcommandline(self):
          modelFilePath=os.path.join(TestsPath,"model.pt")
          wslModelFilePath=PathConverter.Windows2WSL(modelFilePath)
          WSLPythonScriptsPath=PathConverter.Windows2WSL(os.path.join(modulePath,"WSLPythonScripts"))
          commandLine=WSLDetectingScriptCommandLineGenerator(ip="127.0.0.1",port=4444,detectType=DetectType.Seg,wslModelFilePath=wslModelFilePath).getCommandLine()
          manualcommandLine=('wsl -d IMWI_WSL_Yoro -- cd /; cd "'
                             +WSLPythonScriptsPath +'"'
                             +'; python DetectingScript.py --ip 127.0.0.1 --port 4444 --type Seg --modelFilePath "'
                             +wslModelFilePath+'";')
          self.assertEqual(commandLine,manualcommandLine)

if __name__=="__main__":
     unittest.main()