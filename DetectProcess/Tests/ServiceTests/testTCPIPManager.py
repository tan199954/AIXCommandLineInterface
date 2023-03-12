import os
import sys
currentFilePath=os.path.abspath(__file__)
ServiceTestsPath=os.path.dirname(currentFilePath)
TestsPath=os.path.dirname(ServiceTestsPath)
modulePath=os.path.dirname(TestsPath)
parentPath=os.path.dirname(modulePath)
sys.path.append(parentPath)

import unittest
import socket
def cwd():
     return TestsPath
os.getcwd =cwd

from DetectProcess.Src.Services.Common.TCPIPManager.TCPIPManager import TCPIPManager

class TestWSLDetectingScriptCommandLineGenerator(unittest.TestCase):
     def testipv4Format(self):
          ipv4Format=TCPIPManager().isIpv4Format("127.0.0.1")
          self.assertEqual(ipv4Format,True)
          ipv4Format=TCPIPManager().isIpv4Format("127.0.0.1.2")
          self.assertEqual(ipv4Format,False)
     def test(self):
          listeningServer=TCPIPManager().isListeningServer("127.0.0.1",4444)
          self.assertEqual(listeningServer,False)
          
          s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
          host = '127.0.0.1'
          port = 4444
          s.bind((host, port))
          s.listen(1)
          listeningServer=TCPIPManager().isListeningServer("127.0.0.1",4444)
          self.assertEqual(listeningServer,True)
          s.close()


if __name__=="__main__":
     unittest.main()