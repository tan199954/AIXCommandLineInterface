from typing import Union, List
from ..Enum.DetectedObjectExporterType import DetectedObjectExporterType
from ..Services.SocketManager.SocketManager import TcpSocketManager
from ..Services.DetectedObjectExporter.Interfaces import IDetectedObjectExporter
from ..Services.DetectedObjectExporter.Implementation import TcpSocketExporter,TerminalExporter
from ..Services.DataTypeDetector.Detector import DetectedObjectExporterTypeDetector

class DetectedObjectExporterFactory:
    DETECTED_OBJECT_EXPORTER_DISTIONARY={
        DetectedObjectExporterType.TCPSocket:TcpSocketExporter,
        DetectedObjectExporterType.Terminal:TerminalExporter
    }
    @classmethod
    def createDetectdObjectExporters(cls,source:Union[str,dict],tcpSocketManager:TcpSocketManager)->List[IDetectedObjectExporter]:
        detectedObjectExporterTypes=DetectedObjectExporterTypeDetector.getDetectedObjectExporterTypes(source)
        detectedObjectExporters=[]
        for exporterType in detectedObjectExporterTypes:
            exporter=cls.DETECTED_OBJECT_EXPORTER_DISTIONARY[exporterType]
            if issubclass(exporter,TcpSocketExporter):
                exporter=exporter(tcpSocketManager)
            else:
                exporter=exporter()
            detectedObjectExporters.append(exporter)
        return detectedObjectExporters