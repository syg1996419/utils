import os
import shutil
from os.path import join
import cv2
import glob

from conda.instructions import PRINT

root_dir = r"E:\boost\new\img_txt"
save_dir = "./fruit_image"

jpg_list = glob.glob(root_dir + "/*.jpg")  # 读取抠图图片地址

fo = open("dpj_small.txt", "w")  # 打开txt文档

max_s = -1
min_s = 1000
ii = 0
for jpg_path in jpg_list:
    # jpg_path = jpg_list[3]
    txt_path = jpg_path.replace("jpg", "txt")  # 将图片后缀名切换成txt
    jpg_name = os.path.basename(jpg_path)  # 图片名称 ‘20210625092242_034_image.jpg’
    ii += 1
    f = open(txt_path, "r")  # 打开txt文档

    img = cv2.imread(jpg_path)  # 读取图片路径

    height, width, channel = img.shape  # 获取长宽比

    file_contents = f.readlines()  # 按行读取txt文档内容

    for num, file_content in enumerate(file_contents):  # 循环输出每行结果
        save_dir_ = ''
        clss, xc, yc, w, h = file_content.split()  # 切割
        if clss == '1':
            continue
        xc, yc, w, h = float(xc), float(yc), float(w), float(h)  # 转换为浮点型

        # 长宽比
        xc *= width
        yc *= height
        w *= width
        h *= height

        max_s = max(w * h, max_s)
        min_s = min(w * h, min_s)

        half_w, half_h = w // 2, h // 2

        x1, y1 = int(xc - half_w), int(yc - half_h)
        x2, y2 = int(xc + half_w), int(yc + half_h)

        crop_img = img[y1:y2, x1:x2]  # 获取抠图的区域

        new_jpg_name = str(ii) + '_' + str(num) + "_crop_" + str(clss) + ".jpg"  # 抠图后名称

        cv2.imwrite(os.path.join(save_dir, new_jpg_name), crop_img)
        fo.write(os.path.join(save_dir, new_jpg_name) + "\n")

    f.close()

fo.close()

print(max_s, min_s)
