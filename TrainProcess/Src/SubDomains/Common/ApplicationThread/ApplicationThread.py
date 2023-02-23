from PySide6 import QtCore
from typing import Callable

class QCoreApplicationThread(QtCore.QThread):
    def __init__(self,defineMainFuncitionOfQCoreAppThread :Callable, parent: QtCore.QObject = None) -> None:
        super().__init__(parent)  
        self.defineMainFuncitionOfQCoreAppThread = defineMainFuncitionOfQCoreAppThread
    def run(self):
        self.app = QtCore.QCoreApplication([])
        self.defineMainFuncitionOfQCoreAppThread()
        self.app.exec()