import os
import sys
currentFilePath=os.path.abspath(__file__)
testTrainPreparationPath=os.path.dirname(currentFilePath)
testsPath=os.path.dirname(testTrainPreparationPath)
modulePath=os.path.dirname(testsPath)
parentPath=os.path.dirname(modulePath)
sys.path.append(parentPath)
import unittest

from TrainProcess.Src.SubDomains.Training.Services.ModelInfoBuilder.Implementations.SegLossCoefficientFinder import SegLossCoefficientFinder

class TestSegLossCoefficientFinder(unittest.TestCase):
     def testGetLoss(self):
          lossCoefficientParser=SegLossCoefficientFinder()
          loss = lossCoefficientParser.getLossFrStr("Epoch    GPU_mem   box_loss   seg_loss   cls_loss   dfl_loss  Instances       Size"

"       2/3      1.76G        1.2      3.084       3.33      1.199        450        320:  33%|███▎      | 1/3 [00:05<00:11,  5.92s/it]"
"        2/3      1.76G        1.2      3.084       3.33      1.199        450        320:   0%|          | 0/3 [00:05<?, ?it/s]"
"        2/3      1.97G      1.186      3.024      3.366      1.184        556        320:  67%|██████▋   | 2/3 [00:07<00:03,  3.53s/it]"
"        2/3      1.97G      1.186      3.024      3.366      1.184        556        320:  33%|███▎      | 1/3 [00:07<00:11,  5.92s/it]"
"                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95)     Mask(P          R      mAP50  mAP50-95):   0%?, ?it/s]"
"        2/3      1.97G      1.185      3.002      3.385      1.175        188        320: 100%|██████████| 3/3 [00:08<00:00,  2.82s/it]"

"        2/3      1.97G      1.185      3.002      3.385      1.175        188        320: 100%|██████████| 3/3 [00:08<00:00,  2.21s/it]"
"        2/3      1.97G      1.185      3.002      3.385      1.175        188        320:  67%|██████▋   | 2/3 [00:08<00:03,  3.53s/it]")
          self.assertEqual(loss,1.175)

          loss = lossCoefficientParser.getLossFrStr(''
'      Epoch    GPU_mem   box_loss   seg_loss   cls_loss   dfl_loss  Instances       Size'
'   '
'        3/3      1.97G      1.203      3.095      3.321      1.202        456        320:  33%|███▎      | 1/3 [00:06<00:12,  6.14s/it]'
'        3/3      1.97G      1.203      3.095      3.321      1.202        456        320:   0%|          | 0/3 [00:06<?, ?it/s]'
'        3/3      1.97G      1.184      3.131      3.296        1.2        411        320:  67%|██████▋   | 2/3 [00:07<00:03,  3.60s/it]'
'        3/3      1.97G      1.184      3.131      3.296        1.2        411        320:  33%|███▎      | 1/3 [00:07<00:12,  6.14s/it]'
'                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95)     Mask(P          R      mAP50  mAP50-95):   0%?, ?it/s]'
'        3/3      1.98G      1.209      2.964      3.358      1.186        233        320: 100%|██████████| 3/3 [00:08<00:00,  2.88s/it]'
'   '
'        3/3      1.98G      1.209      2.964      3.358      1.186        233        320: 100%|██████████| 3/3 [00:08<00:00,  2.26s/it]'
'        3/3      1.98G      1.209      2.964      3.358      1.186        233        320:  67%|██████▋   | 2/3 [00:08<00:03,  3.60s/it]'
'                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95)     Mask(P          R      mAP50  mAP50-95): 100%00:00,  1.75s/it]'
'   '
'                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95)     Mask(P          R      mAP50  mAP50-95): 100%00:00,  1.61s/it]')
          self.assertEqual(loss,1.186)
          loss = lossCoefficientParser.getLossFrStr(''
      'Epoch    GPU_mem   box_loss   seg_loss   cls_loss   dfl_loss  Instances       Size'
''
'errorString: Image sizes 320 train, 320 val'
'Using 8 dataloader workers'
'Logging results to runs/segment/train9'
'Starting training for 3 epochs...'
' '
'val: Scanning /mnt/d/Tanworking/python/Yolov8/dataset/labels/val.cache... 26 images, 0 backgrounds, 0 corrupt: 100%|██████████| 26/26 [00:'
' '
'val: Scanning /mnt/d/Tanworking/python/Yolov8/dataset/labels/val.cache... 26 images, 0 backgrounds, 0 corrupt: 100%|██████████| 26/26 [00:'
'train: Scanning /mnt/d/Tanworking/python/Yolov8/dataset/labels/train.cache... 74 images, 0 backgrounds, 0 corrupt: 100%|██████████| 74/74 '
' '
'        1/3       1.5G      1.275      3.219      3.311      1.229        438        320:  33%|███▎      | 1/3 [00:10<00:21, 10.87s/it]'
'        1/3       1.5G      1.275      3.219      3.311      1.229        438        320:   0%|          | 0/3 [00:10<?, ?it/s]'
'        1/3      1.71G      1.237      3.112      3.354      1.189        547        320:  67%|██████▋   | 2/3 [00:13<00:06,  6.05s/it]'
'        1/3      1.71G      1.237      3.112      3.354      1.189        547        320:  33%|███▎      | 1/3 [00:13<00:21, 10.87s/it]'
'                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95)     Mask(P          R      mAP50  mAP50-95):   0%?, ?it/s]')
          self.assertEqual(loss,1.189)

if __name__ == "__main__":
    unittest.main()