import time
count = 0
import sys
from PySide6 import QtCore

def onTimeout():
     global count
     sys.stderr.write(f"count: {count}")
     sys.stderr.flush()
     # print(f"count: {count}")
     count +=1
if __name__=="__main__":

     # app = QtCore.QCoreApplication(sys.argv)
     # timer = QtCore.QTimer()
     # timer.setInterval(2000)
     # timer.timeout.connect(onTimeout)
     # timer.start()
     # timer1 = QtCore.QTimer()
     # timer1.setInterval(10000)
     # timer1.timeout.connect(app.quit)
     # timer1.start()
     # sys.exit(app.exec())

     while count < 4:
          time.sleep(2)
          onTimeout()