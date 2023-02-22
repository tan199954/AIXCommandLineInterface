from TrainProcess.Src.SubDomains.Training.Services.Trainer.Implementations.SegTrainer import SegTrainer



def outputString(str):
    print(f"outputString: {str}")
def errorString(str):
    print(f"errorString: {str}")
if __name__=="__main__":
    # app = QtCore.QCoreApplication([])
    # # commandPromptService=CommandPromptService('wsl -d IMWI_WSL_Yoro -- cd /; cd "/mnt/d/Tanworking/python/AIXCommandLineInterface"; yolo segment train data=data.yaml model=yolov8n-seg.pt epochs=3 imgsz=320 batch=32 lr0=0.01;')
    # commandPromptService=CommandPromptService('wsl -d IMWI_WSL_Yoro -- cd /; cd "/mnt/d/Tanworking/python/AIXCommandLineInterface"; python "/mnt/d/Tanworking/python/AIXCommandLineInterface/loop.py;"')
    # commandPromptService.errorReceived.connect(errorString)
    # commandPromptService.outputReceived.connect(outputString)
    # commandPromptService.errorFinished.connect(errorString)
    # commandPromptService.finished.connect(app.quit)
    # commandPromptService.start()
    # app.exec()
    SegTrainer().execute()
    