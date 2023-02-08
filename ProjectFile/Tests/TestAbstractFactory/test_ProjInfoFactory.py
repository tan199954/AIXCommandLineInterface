import os
import sys
currentFilePath=os.path.abspath(__file__)
testServicePath=os.path.dirname(currentFilePath)
testsPath=os.path.dirname(testServicePath)
modulePath=os.path.dirname(testsPath)
parentPath=os.path.dirname(modulePath)
sys.path.append(parentPath)

import unittest
from ProjectFile.Src.AbstractFactory.ProjInfoV1Factory import ProjInfoV1Factory,AIXProjInfoV1Builder,AIXProjInfoV1CVT
class TestProjInfoV1Factory(unittest.TestCase):
    def testCreateBuilder(self):
        projInfoFactory=ProjInfoV1Factory()
        builderFrFactory=projInfoFactory.createProjInfoBuilder()
        builder=AIXProjInfoV1Builder()
        self.assertEqual(builder.__dict__,builderFrFactory.__dict__)
    def testCreateCVT(self):
        projInfoFactory=ProjInfoV1Factory()
        cvtFrFactory=projInfoFactory.createProjInfoConverter()
        cvt=AIXProjInfoV1CVT()
        self.assertEqual(cvtFrFactory.__dict__,cvt.__dict__)
if __name__=="__main__":
     unittest.main()