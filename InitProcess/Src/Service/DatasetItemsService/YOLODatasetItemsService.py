from InitProcess.Src.Service.DatasetItemsService.AbstractImageDatasetItemsService import AbstractImageDatasetItemsService
from InitProcess.Src.Service.LabelPathService.YOLOLabelPathService import YOLOLabelPathService, ILabelPathService

class YOLODatasetItemsService(AbstractImageDatasetItemsService):
    def getLabelPathService(self)->ILabelPathService:
        return YOLOLabelPathService()