# -*- codeing = utf-8 -*-
# @Time : 2021/4/15 14:54
# @Author : xiaoguanguang
# @File : voctotxt.py
# @Software : PyCharm
import os
# import os.path
# import xml.etree.ElementTree as ET
# import glob
#
# class_names = ['1', '2', '3', '4', '5', '6', '7']  # 类别名，依次写下来
# dirpath = './VOCdevkit/VOC2007/Annotations/'  # 原来存放xml文件的目录
# newdir = './train_data/'  # 修改label后形成的txt目录
#
# if not os.path.exists(newdir):
#     os.makedirs(newdir)
#
# for fp in os.listdir(dirpath):
#
#     root = ET.parse(os.path.join(dirpath, fp)).getroot()
#
#     xmin, ymin, xmax, ymax = 0, 0, 0, 0
#     sz = root.find('size')
#     width = float(sz[0].text)
#     height = float(sz[1].text)
#     filename = root.find('filename').text
#     for child in root.findall('object'):  # 找到图片中的所有框
#         name = child.find('name').text  # 找到类别名
#         class_num = class_names.index(name)  #
#
#         sub = child.find('bndbox')  # 找到框的标注值并进行读取
#         xmin = float(sub[0].text)
#         ymin = float(sub[1].text)
#         xmax = float(sub[2].text)
#         ymax = float(sub[3].text)
#         try:  # 转换成yolov3的标签格式，需要归一化到（0-1）的范围内
#             x_center = (xmin + xmax) / (2 * width)
#             y_center = (ymin + ymax) / (2 * height)
#             w = (xmax - xmin) / width
#             h = (ymax - ymin) / height
#         except ZeroDivisionError:
#             print(filename, '的 width有问题')
#
#         with open(os.path.join(newdir, fp.split('.')[0] + '.txt'), 'a+') as f:
#             f.write(' '.join([str(class_num), str(x_center), str(y_center), str(w), str(h) + '\n']))
import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join

sets = ['train', 'val']

classes = ['1', '2', '3', '4', '5']  # 自己训练的类别


def convert(size, box):
    dw = 1. / size[0]
    dh = 1. / size[1]
    x = (box[0] + box[1]) / 2.0
    y = (box[2] + box[3]) / 2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)


def convert_annotation(image_id):
    in_file = open(r'C:\Users\GF\Desktop\yolov4-pytorch-master\VOCdevkit\VOC2007\Annotations/%s.xml' % (image_id), encoding='utf-8')
    out_file = open('./labels/%s.txt' % (image_id), 'w')
    tree = ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult) == 1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text),
             float(xmlbox.find('ymax').text))
        bb = convert((w, h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')


wd = getcwd()
for image_set in sets:
    if not os.path.exists('./labels/'):
        os.makedirs('./labels/')
    image_ids = open(r'C:\Users\GF\Desktop\yolov4-pytorch-master\VOCdevkit\VOC2007\ImageSets\Main/%s.txt' % (image_set)).read().strip().split()
    list_file = open('./%s.txt' % (image_set), 'w')
    for image_id in image_ids:
        list_file.write(r'C:\Users\GF\Desktop\yolov4-pytorch-master\VOCdevkit\VOC2007\JPEGImages/%s.jpg\n' % (image_id))
        convert_annotation(image_id)
    list_file.close()
