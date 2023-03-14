from ....Enum.TrainType import TrainType
from ..Services.TrainExporter.Interfaces.ITrainExporter import ITrainExporter
from ..Services.TrainExporter.Implementation.YOLOExporter import SegExporter,BoxExporter
from ..Services.TrainExporter.Implementation.YOROExporter import BBoxExporter
class TrainExporterFactory:
    TRAIN_EXPORTER_DICTIONARY={TrainType.Seg:SegExporter,
                               TrainType.BBox:BBoxExporter,
                               TrainType.Box:BoxExporter}
    @staticmethod
    def createTrainExporter(trainType:TrainType)->ITrainExporter:
        return TrainExporterFactory.TRAIN_EXPORTER_DICTIONARY[trainType]()