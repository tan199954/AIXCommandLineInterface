class PathConverter:
    @staticmethod
    def Windows2WSL(windowsPath:str)->str:
        currentPath = windowsPath.replace("\\","/")
        currentPathList = currentPath.split("/")
        disk = currentPathList[0].replace(":","").lower()
        currentPathList = currentPathList[1:]
        currentPathList.insert(0,disk)
        return "/mnt/" + '/'.join(currentPathList)
    @staticmethod
    def WSL2Windows(WSLPath:str)->str:
        pass