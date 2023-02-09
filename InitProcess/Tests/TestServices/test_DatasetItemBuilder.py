import os
import sys
currentFilePath=os.path.abspath(__file__)
testServicesPath=os.path.dirname(currentFilePath)
testsPath=os.path.dirname(testServicesPath)
modulePath=os.path.dirname(testsPath)
parentPath=os.path.dirname(modulePath)
sys.path.append(parentPath)

import unittest
from InitProcess.Src.Service.DatasetItemBuilder.ImageDatasetItemBuilder import ImageDatasetItemBuilder, ImageDatasetItem


class TestImageDatasetItemBuilder(unittest.TestCase):
    def testImageDatasetItemBuilder(self):
        imageFilePath=os.path.join(testsPath,r"imagePath\\test.jpg")
        labelFilePath=os.path.join(testsPath,r"bbLabelPath\\test.jpg.mark")

        imageDatasetItemBuilder=ImageDatasetItemBuilder().setImageFilePath(      
        imageFilePath).setLabelFilePath(labelFilePath).build()
        imageDatasetItem=ImageDatasetItem(imageFilePath,labelFilePath)
        self.assertEqual(imageDatasetItemBuilder.__dict__,imageDatasetItem.__dict__)

if __name__=="__main__":
     unittest.main()