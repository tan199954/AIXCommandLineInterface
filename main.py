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

    initParser = subparsers.add_parser("init",help="initial initialize process")
    initParser.add_argument("-t","--typeOfTrain",type=TrainType,help="'Box' or 'BBox' or 'Seg'")
    initParser.add_argument("-i","--imagePath",type=str,help="full/path/to/images directory")
    initParser.add_argument("-l","--labelPath",type=str,help="full/path/to/labels directory")
    initParser.set_defaults(func=Init)

    trainParser = subparsers.add_parser("train",help="initial train process")
    trainParser.set_defaults(func=Train)

    detectParser = subparsers.add_parser('detect', help='initial detect process')
    detectParser.add_argument("-s","--source",type=str,help="full/path/to/image or video or ipAdress/port")
    detectParser.set_defaults(func=Detect)

    return parser

def Train():
     sys.stdout.write("Waiting for the training...\n")
     sys.stdout.flush()
     train = TrainProcess()
     train.execute()
def Detect(source):
     if source is None: 
          raise argparse.ArgumentTypeError('usage: AIXCLI.exe detect -h \nmissed some arguments')
     sys.stdout.write("Waiting for the detection...\n")
     sys.stdout.flush()
     detect = DetectProcess(source)
     detect.execute()      
def Init(labelPath,imagePath,typeOfTrain):
     if imagePath is None or labelPath is None or typeOfTrain is None:
         raise argparse.ArgumentTypeError('usage: AIXCLI.exe init -h \nmissed some arguments')
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