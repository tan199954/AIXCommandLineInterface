from InitProcess.Src.Service.DatasetItemsService.AbstractImageDatasetItemsService import AbstractImageDatasetItemsService
from InitProcess.Src.Service.LabelPathService.YOROLabelPathService import YOROLabelPathService, ILabelPathService

class YORODatasetItemsService(AbstractImageDatasetItemsService):
    def getLabelPathService(self)->ILabelPathService:
        return YOROLabelPathService()