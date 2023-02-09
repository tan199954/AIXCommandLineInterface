from InitProcess.Src.Core.Models.InitEnum import InitType
from InitProcess.Src.AbstractFactory.Implementation.InitAbstractFactory import InitAbstractFactory
class InitProcessor:
    def __init__(self,imaegPath:str,labelPath:str,initType:InitType) -> None:
        initFactory=InitAbstractFactory().getFactory(initType)
        datasetItemService=initFactory.createDatasetItemService(imaegPath,labelPath)
        datasetItems=datasetItemService.getDatasetItems()
        self.dictributor=initFactory.createDatasetDistributor(datasetItems)
    def execute(self):
        self.dictributor.execute()
    def getDirFormat(self)->dict:
        """
        if dictributor have DatasetDirectoryFormat
        return DatasetDirectoryFormat dictData
        else
        return None
        """
        try:
            obj=self.dictributor.getDatasetDirectoryFormat()
            return {k: getattr(obj, k) for k in dir(obj) 
                    if not callable(getattr(obj, k)) 
                    and not k.startswith("__")
                    and not k.startswith("_")
                    and not k[0].isupper()}
        except:
            return None