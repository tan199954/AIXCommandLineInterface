import yaml

class YAMLFileService:
    @staticmethod
    def writeDictData(filePath:str,data:dict):
        with open(filePath,"w") as file:
            yaml.dump(data=data,stream=file,sort_keys=False)
        file.close()
    @staticmethod
    def readDictData(filePath:str)->dict:
        with open(filePath,"r") as file:
            data=yaml.load(file,Loader=yaml.FullLoader)
            file.close()
        return data