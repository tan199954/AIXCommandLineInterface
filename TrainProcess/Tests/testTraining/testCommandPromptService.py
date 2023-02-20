import os
import sys
currentFilePath=os.path.abspath(__file__)
testTrainPreparationPath=os.path.dirname(currentFilePath)
testsPath=os.path.dirname(testTrainPreparationPath)
modulePath=os.path.dirname(testsPath)
parentPath=os.path.dirname(modulePath)
sys.path.append(parentPath)
import unittest
from PySide6 import QtCore

from TrainProcess.Src.SubDomains.Training.Services.CommandPromptService.CommandPromptService import CommandPromptService
class TestCMDService(unittest.TestCase):
    def testCMDService(self):
        CMDService=CommandPromptService("python --version")
        if QtCore.QCoreApplication.instance() is None:
            app = QtCore.QCoreApplication(sys.argv)
        else:
            app = QtCore.QCoreApplication.instance()
        CMDService.finished.connect(app.quit)
        CMDService.start()
        app.exec()
        self.assertEqual(CMDService.process.state(),QtCore.QProcess.ProcessState.NotRunning)
if __name__ == "__main__":
    unittest.main()