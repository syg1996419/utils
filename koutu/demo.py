import os
import random
from os.path import join
import aug
import Helpers as hp
from util import *

# ###########Pipeline##############
"""
1 准备数据集和yolo格式标签, 如果自己的数据集是voc或coco格式的，先转换成yolo格式，增强后在转回来
2 run crop_image.py  裁剪出目标并保存图片
3 run demo.py   随机将裁剪出目标图片贴到需要增强的数据集上，并且保存增强后的图片集和label文件
"""

base_dir = os.getcwd()

save_base_dir = join(base_dir, 'txt_to_xml')  # 保存路径
check_dir(save_base_dir)

# imgs_dir = [f.strip() for f in open(join(base_dir, 'sea.txt')).readlines()]
# 所扣图片路径
imgs_dir = [os.path.join('fruit', f) for f in os.listdir('fruit') if f.endswith('jpg')]
print(imgs_dir)
# 所扣图片的txt文件
labels_dir = hp.replace_labels(imgs_dir)
# print(imgs_dir, '\n', labels_dir)

# small_imgs_dir = [f.strip() for f in open(join(base_dir, 'dpj_small.txt')).readlines()]
# 抠图图片路径
small_imgs_dir = [os.path.join('fruit_image', f) for f in os.listdir('fruit_image') if f.endswith('jpg')]

random.shuffle(small_imgs_dir)  # 目标图片打乱
# print(small_imgs_dir)

times = 5  # 随机选择增加多少个目标

for image_dir, label_dir in zip(imgs_dir, labels_dir):
    small_img = []
    for x in range(times):
        if small_imgs_dir == []:
            small_imgs_dir = [os.path.join('fruit_image', f) for f in os.listdir('fruit_image') if f.endswith('jpg')]
            random.shuffle(small_imgs_dir)
            #print(111111111111111111111111111111111111, small_imgs_dir)
        small_img.append(small_imgs_dir.pop())
    # print("ok")
    aug.copysmallobjects(image_dir, label_dir, save_base_dir, small_img, times)
    '''
    new_bboxes = random_add_patches(roi.shape,     # 此函数roi目标贴到原图像上，返回的bbox为roi在原图上的bbox,
                               rescale_labels,  # 并且bbox不会挡住图片上原有的目标
                               image.shape,
                               paste_number=1,  # 将该roi目标复制几次并贴到到原图上
                               iou_thresh=0)    # iou_thresh 原图上的bbox和贴上去的roi的bbox的阈值
    '''
