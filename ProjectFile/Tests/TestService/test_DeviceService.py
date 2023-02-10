import os
import sys
currentFilePath=os.path.abspath(__file__)
testServicePath=os.path.dirname(currentFilePath)
testsPath=os.path.dirname(testServicePath)
modulePath=os.path.dirname(testsPath)
parentPath=os.path.dirname(modulePath)
sys.path.append(parentPath)

import unittest
from ProjectFile.Src.Service.Common.DeviceService import DeviceService
class TestDeviceService(unittest.TestCase):
     def testGPUNumber(self):
          deviceService=DeviceService()
          num=deviceService.getGpuNumber()
          self.assertEqual(num,1)
     def testFreeGPUMemory(self):
          deviceService=DeviceService()
          freeMe=deviceService.getFreeGPUmemory(0)
          self.assertEqual(freeMe,3962) #4GB ~ 3962 MB
     def testTotalGPUMemory(self):
          deviceService=DeviceService()
          totalFreeMe=deviceService.getTotalFreeGPUmenmory()
          self.assertEqual(totalFreeMe,3962) #4GB ~ 3962 MB


if __name__=="__main__":
     unittest.main()