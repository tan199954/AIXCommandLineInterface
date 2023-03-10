from typing import Union, List
from PySide6 import QtNetwork
from ..Services.DetectedObjectExporter.Interfaces import IDetectedObjectExporter

class DetectdObjectExporterFactory:
    def createDetectdObjectExporters(source:Union[str,dict],imageSourceSocket:QtNetwork.QTcpSocket)->List[IDetectedObjectExporter]:
        pass