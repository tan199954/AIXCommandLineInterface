from .AbstractOutputManager import AbstractYOLOOutputManager


class SegOutputManager(AbstractYOLOOutputManager):
     @property
     def TRAIN_DIR_NAME(self)->str:
        return r"runs\segment"