from PySide6 import QtCore
import sys
import argparse
import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from InitProcess.Src.Api import InitProcess
from InitProcess.Src.Core import TrainType
from TrainProcess.Src.Api import TrainProcess
from DetectProcess.Src.Api import DetectProcess


def parse_opt():

    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()
    choices = [dt.name for dt in TrainType]
    initParser = subparsers.add_parser("init",help="initial initialize process")
    initParser.add_argument("-t","--typeOfTrain",type=TrainType,choices=choices)
    initParser.add_argument("-i","--imagePath",type=str,help="full/path/to/images directory")
    initParser.add_argument("-l","--labelPath",type=str,help="full/path/to/labels directory")
    initParser.set_defaults(func=Init)

    trainParser = subparsers.add_parser("train",help="initial train process")
    trainParser.set_defaults(func=Train)

    detectParser = subparsers.add_parser('detect', help='initial detect process')
    detectParser.add_argument("-s","--source",type=str,nargs="+",help="'full/path/to/imageFile of videoFle'\n"
                                                            " or ip='IP adress' port='port number from 0 to 65535'\n ")
    detectParser.set_defaults(func=Detect)

    return parser

def Train():
     sys.stdout.write("Waiting for the training...\n")
     sys.stdout.flush()
     train = TrainProcess()
     train.execute()
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
     sys.stdout.write("Waiting for the detection...\n")
     sys.stdout.flush()
     detect = DetectProcess(source)
     detect.execute()      
def Init(labelPath,imagePath,typeOfTrain):
     if imagePath is None or labelPath is None or typeOfTrain is None:
         raise argparse.ArgumentTypeError('usage: AIXCLI.exe init -h \nmissed some arguments')
     typeOfTrain=TrainType(typeOfTrain)
     sys.stdout.write("Waiting for the initialization...\n")
     sys.stdout.flush()
     init = InitProcess(imagePath,labelPath,typeOfTrain)
     init.execute()
     sys.stdout.write("Initialization is Finished\n")
     sys.stdout.flush()
     sys.exit()

def main(parser: argparse.ArgumentParser):
     args = parser.parse_args() 
     args_ = vars(args).copy()
     args_.pop('command', None)
     args_.pop('func', None)
     args.func(**args_)

if __name__ == "__main__":
     app = QtCore.QCoreApplication(sys.argv)
     main(parse_opt())
     sys.exit(app.exec())