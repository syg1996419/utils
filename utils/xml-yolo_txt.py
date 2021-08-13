import os
import random


trainval_percent = 0.9
train_percent = 1
xmlfilepath = r'C:\Users\GF\Desktop\yolov4-pytorch-master\VOCdevkit\VOC2007\Annotations'
txtsavepath = r'C:\Users\GF\Desktop\yolov4-pytorch-master\VOCdevkit\VOC2007\ImageSets'
total_xml = os.listdir(xmlfilepath)

num = len(total_xml)
list = range(num)
tv = int(num * trainval_percent)
tr = int(tv * train_percent)
trainval = random.sample(list, tv)
train = random.sample(trainval, tr)

ftrainval = open(r'C:\Users\GF\Desktop\yolov4-pytorch-master\VOCdevkit\VOC2007\ImageSets/trainval.txt', 'w')
ftest = open(r'C:\Users\GF\Desktop\yolov4-pytorch-master\VOCdevkit\VOC2007\ImageSets/test.txt', 'w')
ftrain = open(r'C:\Users\GF\Desktop\yolov4-pytorch-master\VOCdevkit\VOC2007\ImageSets/train.txt', 'w')
fval = open(r'C:\Users\GF\Desktop\yolov4-pytorch-master\VOCdevkit\VOC2007\ImageSets/val.txt', 'w')

for i in list:
    name = total_xml[i][:-4] + '\n'
    if i in trainval:
        ftrainval.write(name)
        if i in train:
            ftrain.write(name)
        else:
            fval.write(name)
    else:
        ftest.write(name)

ftrainval.close()
ftrain.close()
fval.close()
ftest.close()
