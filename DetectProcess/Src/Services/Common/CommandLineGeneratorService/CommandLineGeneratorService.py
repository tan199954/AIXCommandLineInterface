from ..PathConverter.PathConverter import PathConverter

class CommandLineGeneratorService:
        COMMAND_SPERATOR=";"
        PARAMETER_SPERATOR=" "
        KEEP_FULL_PATH_KEY='"'
        @staticmethod
        def addQuotesToPath(path:str)->str:
               return (CommandLineGeneratorService.KEEP_FULL_PATH_KEY +
                       path + CommandLineGeneratorService.KEEP_FULL_PATH_KEY)

class WSLCommandLineGenerator(CommandLineGeneratorService):
        WSL_DISTRIBUTOR_NAME="IMWI_WSL_Yoro"
        WSL_ACCEPT_COMMAND_KEY="--"
        @staticmethod
        def getCDCommandFromPath(windowsPath:str)->str:
            wslPath = CommandLineGeneratorService.addQuotesToPath(PathConverter.Windows2WSL(windowsPath))
            return ("cd /" +CommandLineGeneratorService.COMMAND_SPERATOR + CommandLineGeneratorService.PARAMETER_SPERATOR
                    + "cd " + wslPath+ CommandLineGeneratorService.COMMAND_SPERATOR)    
        @staticmethod
        def getWSLLoginCommand()->str:
              return "wsl -d " +WSLCommandLineGenerator.WSL_DISTRIBUTOR_NAME