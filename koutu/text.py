import random
import numpy as np
import xml.dom.minidom
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw
from os import getcwd


def bbox_iou(box1, box2):
    b1_x1, b1_y1, b1_x2, b1_y2 = box1
    b2_x1, b2_y1, b2_x2, b2_y2 = box2
    # get the corrdinates of the intersection rectangle
    inter_rect_x1 = max(b1_x1, b2_x1)
    inter_rect_y1 = max(b1_y1, b2_y1)
    inter_rect_x2 = min(b1_x2, b2_x2)
    inter_rect_y2 = min(b1_y2, b2_y2)
    # Intersection area
    inter_width = inter_rect_x2 - inter_rect_x1 + 1
    inter_height = inter_rect_y2 - inter_rect_y1 + 1
    if inter_width > 0 and inter_height > 0:  # strong condition
        inter_area = inter_width * inter_height
        # Union Area
        b1_area = (b1_x2 - b1_x1 + 1) * (b1_y2 - b1_y1 + 1)
        b2_area = (b2_x2 - b2_x1 + 1) * (b2_y2 - b2_y1 + 1)
        iou = inter_area / (b1_area + b2_area - inter_area)
    else:
        iou = 0
    return iou


def aug_data_method(wd, root_path, img_name, row):
    img = Image.open(root_path + '/' + img_name + ".jpg")
    lines_ = []
    # 见注1

    with open("train" + '.txt', 'r') as f:
        lines = f.readlines()
    for line in lines:
        line = line.split()
        lines_.append(line)

    bboxes = []
    lines_eachimg = []
    for i in range(len(lines_[row]) - 1):
        line = lines_[row][i + 1].split(',')
        lines_eachimg.append(line)
        bboxes.append([int(line[0]), int(line[1]), int(line[2]), int(line[3])])
    list_file.write('%s/VOCdevkit/VOC%s/JPEGImages/%s_.jpg' % (wd, year, image_id))
    for i in range(len(bboxes)):
        b = (int(bboxes[i][0]), int(bboxes[i][1]),
             int(bboxes[i][2]), int(bboxes[i][3]))
        list_file.write(" " + ",".join([str(a) for a in b]) + ',' + str(cls_id))

    specific_idxs = [0]
    threshold = 0.3
    sample_num_per_sample = 2

    for line in lines_eachimg:
        clsname = int(line[4])
        if clsname in specific_idxs:
            bbox_left, bbox_top, bbox_right, bbox_down = int(line[0]), int(line[1]), int(line[2]), int(line[3])
            for i in range(sample_num_per_sample):
                new_bbox_left = random.randint(0, width - bbox_right + bbox_left)
                new_bbox_top = random.randint(0, height - bbox_down + bbox_top)
                bbox1 = [new_bbox_left, new_bbox_top, new_bbox_left + bbox_right - bbox_left,
                         new_bbox_top + bbox_down - bbox_top]
                ious = [bbox_iou(bbox1, bbox) for bbox in bboxes]
                if max(ious) <= threshold:
                    bboxes.append(bbox1)
                    cls_id = 0  # 看着改
                    b = (int(bbox1[0]), int(bbox1[1]),
                         int(bbox1[2]), int(bbox1[3]))
                    list_file.write(" " + ",".join([str(a) for a in b]) + ',' + str(cls_id))

                    region = img.crop((bbox_left, bbox_top, bbox_right, bbox_down))
                    img.paste(region, (bbox1[0], bbox1[1]))
    img.save(root_path + '/' + img_name + "_.jpg")
    list_file.write('\n')
    print(row)
    return


if __name__ == '__main__':
    sets = [('2012', 'train')]
    for year, image_set in sets:
        image_ids = open('./VOCdevkit/VOC%s/ImageSets/Main/%s.txt' % (year, image_set)).read().strip().split()
        list_file = open('./%s_augdata.txt' % image_set, 'w')
        for image_index, image_id in enumerate(image_ids):
            aug_data_method(wd="/your/project/path", root_path="/VOCdevkit/VOC2012/JPEGImages",
                            img_name=image_id, row=image_index)
        list_file.close()