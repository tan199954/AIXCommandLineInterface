from PySide6 import QtCore
import sys
import os
currentPath = os.getcwd()
detectProcessPath = os.path.join(currentPath,"DetectProcess") 
trainProcessPath = os.path.join(currentPath,"TrainProcess") 
sys.path.append(detectProcessPath)
sys.path.append(trainProcessPath)

import argparse

from TrainProcess.Api import TrainProcess
from DetectProcess.Api import DetectProcess

def parse_opt():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(required=True)

    trainParser = subparsers.add_parser("train",help="initial train process")
    trainParser.add_argument("-tr","--trainPath",type=str,help="full/path/to/train dataset directory")
    trainParser.add_argument("-val","--validPath",type=str,help="full/path/to/valid dataset directory")
    trainParser.add_argument("-out","--outputPath",type=str,help="full/path/to/output directory")
    trainParser.set_defaults(func=Train)

    detectParser = subparsers.add_parser('detect', help='initial detect process')
    detectParser.add_argument("-s","--source",type=str,help="full/path/to/image or video or ipAdress/port")
    detectParser.add_argument("-m","--modelPath",type=str,help="full/path/to/modelFile")
    detectParser.add_argument("-t","--type",type=str,help="")
    detectParser.set_defaults(func=Detect)

    return parser

def Train(trainPath,validPath, outputPath):
     if trainPath is None or validPath is None or outputPath is None: 
          raise argparse.ArgumentTypeError('usage: AIXCLI.exe train -h \nmissed some arguments ')
     train = TrainProcess(trainPath,validPath,outputPath)
     train.execute()

def Detect(source, modelPath,type):
     if source is None or modelPath is None or type is None: 
          raise argparse.ArgumentTypeError('usage: AIXCLI.exe detect -h \nmissed some arguments')
     detect = DetectProcess(source,modelPath,type)
     detect.execute()

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