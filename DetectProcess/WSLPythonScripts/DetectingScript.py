import argparse
from PySide6 import QtCore
import numpy as np
from .DetectorFactory import DetectorFactory,DetectorType
from .TCPSocketImageProcessor import TCPSocketImageProcessor
    
def parse_opt():
    choices = [dt.name for dt in DetectorType]
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", help="IP adress",type=str)
    parser.add_argument("--port", help="Port for TCP", type=int)
    parser.add_argument("--type", help="Detector Type",type=str, choices=choices)
    parser.add_argument("--modelFilePath", help="Full WSL path to model file",type=str)    
    args=parser.parse_args()
    args.type=DetectorType(args.type)
    return args

if __name__ =="__main__":
    args = parse_opt()
    app = QtCore.QCoreApplication()
    detector=DetectorFactory.createDetector(args.type,args.modelFilePath)
    imageTCPSocketProcessor=TCPSocketImageProcessor(args.ip,args.port)
    def onImageReceived(image:np.ndarray):
        result=detector.getObjectsInfo(image)
        imageTCPSocketProcessor.exportResult(result)
    imageTCPSocketProcessor.imageReceived.connect(onImageReceived)
    imageTCPSocketProcessor.socket.disconnected.connect(app.quit)
    imageTCPSocketProcessor.run()
    app.exec()
    