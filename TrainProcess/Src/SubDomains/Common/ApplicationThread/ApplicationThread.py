from PySide6 import QtCore
from typing import Callable

class QCoreApplicationThread(QtCore.QThread):
    def __init__(self,definePySide6Classes :Callable, parent: QtCore.QObject = None) -> None:
        super().__init__(parent)  
        self.definePySide6Classes = definePySide6Classes
    def run(self):
        app = QtCore.QCoreApplication([])
        self.definePySide6Classes()
        app.exec()