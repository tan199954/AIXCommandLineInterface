from .AbstractOutputManager import AbstractYOLOOutputManager


class BoxOutputManager(AbstractYOLOOutputManager):
     @property
     def TRAIN_DIR_NAME(self)->str:
        return r"runs\detect"