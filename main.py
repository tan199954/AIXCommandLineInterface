import sys
import argparse
import winreg
import pyuac
import os

from InitProcess.Src.Application.InitProcessor import InitProcessor
from TrainProcess.Src.Application.TrainProcessor import TrainProcessor
from DetectProcess.Src.Application.DetectProcessor import DetectProcessor
from ProjectFile.Src.Application.AIXProjInfoService import AIXProjInfoService

from TrainProcess.Src.Enum.TrainType import TrainType
from InitProcess.Src.Core.Models.InitEnum import InitType
from DetectProcess.Src.Enum.DetectType import DetectType

from ProjectFile.Src.Core.Models.AIXProjInfoAggregate.DatasetInfo import DatasetInfo
from ProjectFile.Src.Core.Models.AIXProjInfoAggregate.OutputInfo import OutputInfo


def parse_opt():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()
    initParser = subparsers.add_parser("init",help="initial initialize process")
    initParser.add_argument("-n","--objectNames",type=str,nargs="+",help="name1 name2 name3 ...")
    initParser.add_argument("-i","--imagePath",type=str,help="full/path/to/images directory")
    initParser.add_argument("-l","--labelPath",type=str,help="full/path/to/labels directory")
    initParser.set_defaults(func=Init)

    trainParser = subparsers.add_parser("train",help="initial train process")
    trainParser.add_argument("--manual",type=str,nargs="+",default=False,help="batchSize=intValue "
                             "imageSize=intValue learningRate=floatValue")
    trainParser.set_defaults(func=Train)

    detectParser = subparsers.add_parser('detect', help='initial detect process')
    detectParser.add_argument("-s","--source",type=str,nargs="+",help="'full/path/to/imageFile of videoFle'\n"
                                                            " or ip='IP adress' port='port number from 0 to 65535'\n ")
    detectParser.set_defaults(func=Detect)

    return parser

def Train(manual):
     if manual == []:
          manual=True
     def checkManualArg(manual:list):
          manualArg = {}
          batchSize=imageSize=learningRate=None
          for item in manual:
               if '=' not in item or item.startswith('=') or item.endswith('='):
                    continue
               key, value = item.split('=')
               manualArg[key] = value
          if "batchSize" in manualArg.keys():
               batchSize=manualArg["batchSize"]
               if not isinstance(batchSize,int):
                    raise ValueError("batchSize must be interger")
          if "imageSize" in manualArg.keys():
               imageSize=manualArg["imageSize"]
               if not isinstance(imageSize,int):
                    raise ValueError("imageSize must be interger")
          if "learningRate" in manualArg.keys():
               learningRate=manualArg["learningRate"]
               if not isinstance(learningRate,float) or learningRate>0.01:
                    raise ValueError("learningRate must be less than 0.01")
          return batchSize,imageSize,learningRate
     if isinstance(manual,list):
          batchSize,imageSize,learningRate=checkManualArg(manual)
          manual=True
     else:
          batchSize=None
          imageSize=None
          learningRate=None
     #show ConsoleUI
     sys.stdout.write("Waiting for the training...\n")
     sys.stdout.flush()
     # get AIX Proj Info
     aixProjInfo=AIXProjInfoService().getAIXProjInfo()
     trainPath=aixProjInfo.datasetInfo.getTrainImagePath()
     validPath=aixProjInfo.datasetInfo.getValidImagePath()
     gpuMen=aixProjInfo.device.getTotalFreeGPUMemory()
     aixType=aixProjInfo.AIXSeedData.getAIXType()
     objectNames=aixProjInfo.AIXSeedData.getObjectNames()
     trainType=TrainType(aixType.value)
     # start train
     train = TrainProcessor(manual=manual,batchSize=batchSize,imageSize=imageSize,learningRate=learningRate,
                            trainPath=trainPath,validPath=validPath,gpuMenmory=gpuMen,trainType=trainType,objectNames=objectNames)
     train.execute()
     # update AIXProjFileInfo after initializing
     aIXProjInfoService=AIXProjInfoService()
     trainDictionary=train.getDictionaryData()
     outputInfo=OutputInfo(**trainDictionary)
     aIXProjInfoService.updateAIXProjInfo(outputInfo)
     #show ConsoleUI
     sys.stdout.write("The Training is Finished\n")
     sys.stdout.flush()

def Detect(source):
     def checkSourceArg(source:list):
          IMAGE_SOURCE_LEN=1
          TCP_IP_SOURCE_LEN=2
          if len(source) == IMAGE_SOURCE_LEN:
               return source[0]
          if len(source) != TCP_IP_SOURCE_LEN or 'ip=' not in source[0] or 'port=' not in source[1]:
               raise argparse.ArgumentTypeError("Invalid --source argument format.")
          ip = source[0].split('=')[1]
          port = source[1].split('=')[1]
          try:
               port = int(port)
               if not 0 <= port <= 65535:
                    raise ValueError()
          except ValueError:
               raise argparse.ArgumentTypeError("Invalid port number.")
          return {'ip': ip, 'port': port}
     source=checkSourceArg(source)
     aixProjInfo=AIXProjInfoService().getAIXProjInfo()
     aixType=aixProjInfo.AIXSeedData.getAIXType()
     detectType=DetectType(aixType.value)
     modelFilePath=aixProjInfo.outputInfo.getOutputModelFilePath()
     sys.stdout.write("Waiting for the object detection...\n")
     sys.stdout.flush()
     detect = DetectProcessor(detectType,modelFilePath,source)
     detect.execute()    
     sys.stdout.write("The object detection is Finished\n")
     sys.stdout.flush()
       
def Init(labelPath,imagePath,objectNames):
     def AIXType2InitType(aixType):
          if aixType.value=="BBox":
               return InitType.YORO
          return InitType.YOLO
     if imagePath is None or labelPath is None or objectNames is None:
         raise argparse.ArgumentTypeError('usage: AIXCLI.exe init -h \nmissed some arguments')
     sys.stdout.write("Waiting for the initialization...\n")
     sys.stdout.flush()
     # set AIXProjFileInfo
     aIXProjInfoService=AIXProjInfoService()
     aIXProjInfoService.setAIXProjInfo(imagePath,labelPath,objectNames)
     # get AIXProjFileInfo
     aIXProjInfo=aIXProjInfoService.getAIXProjInfo()
     aixType=aIXProjInfo.AIXSeedData.getAIXType()
     # start InitProcessor
     initType=AIXType2InitType(aixType)
     init = InitProcessor(imagePath,labelPath,initType)
     init.execute()
     # update AIXProjFileInfo after initializing
     initDictionary=init.getDirFormat()
     datasetInfo=DatasetInfo(**initDictionary)
     aIXProjInfoService.updateAIXProjInfo(datasetInfo)
     #show ConsoleUI
     sys.stdout.write("The Initialization is Finished\n")
     sys.stdout.flush()

def setupEnvVar():
     if not pyuac.isUserAdmin():
        pyuac.runAsAdmin()
     else:
          try:
               path_to_aix = os.getcwd()
               key = winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, 'SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Environment')
               path_value = winreg.QueryValueEx(key, 'Path')[0]
               if path_to_aix in path_value:
                    showResultSetupEnvVar("Successfully")
                    return
               new_path_value = path_value + path_to_aix +";"
               winreg.SetValueEx(key, 'PATH', 0, winreg.REG_EXPAND_SZ, new_path_value)
               winreg.CloseKey(key)
               showResultSetupEnvVar("Successfully")
          except Exception as e:
               showResultSetupEnvVar(str(e))

def showResultSetupEnvVar(text):
     from PySide6.QtWidgets import QMessageBox,QApplication
     app=QApplication()
     mess=QMessageBox()
     mess.setWindowTitle("Environment Variables")
     mess.setText(text)
     mess.setStandardButtons(QMessageBox.Ok)
     mess.setIcon(QMessageBox.Information)
     mess.show()
     app.exec()

def main(parser: argparse.ArgumentParser):
     args = parser.parse_args() 
     args_ = vars(args).copy()
     if not args_:
          setupEnvVar()
          return
     args_.pop('func', None)
     args.func(**args_)

if __name__ == "__main__":
     main(parse_opt())