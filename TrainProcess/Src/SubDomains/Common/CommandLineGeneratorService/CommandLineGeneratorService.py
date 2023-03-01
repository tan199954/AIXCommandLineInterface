from ..PathConverter.PathConverter import PathConverter

class CommandLineGeneratorService:
        COMMAND_SPERATOR=";"
        PARAMETER_SPERATOR=" "
        WSL_ACCEPT_COMMAND_KEY="--"
        KEEP_FULL_PATH_KEY='"'
        @staticmethod
        def getCDCommandFromPath(windowsPath:str)->str:
            wslOutputPath= (CommandLineGeneratorService.KEEP_FULL_PATH_KEY 
                            + PathConverter.Windows2WSL(windowsPath) 
                            + CommandLineGeneratorService.KEEP_FULL_PATH_KEY)
            return ("cd /" +CommandLineGeneratorService.COMMAND_SPERATOR + CommandLineGeneratorService.PARAMETER_SPERATOR
                    + "cd " + wslOutputPath+ CommandLineGeneratorService.COMMAND_SPERATOR)
    
        @staticmethod
        def getWSLLoginCommand(distributorName:str):
              return "wsl -d " +distributorName