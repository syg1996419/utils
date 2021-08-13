import os
import shutil

txt_path = r'C:\Users\GF\Desktop\yolov4-pytorch-master/'
xml_path = r'C:\Users\GF\Desktop\VOCdevkit\VOC2007\Annotations/'
img_path = r'C:\Users\GF\Desktop\VOCdevkit\VOC2007\JPEGImages/'
read_txt = '2007_train.txt'
with open(txt_path + read_txt) as f:
    total_line = f.readlines()
    # print(total_line)

    for line in total_line:
        line = line.strip()
        # print(line)
        sp = line.split()
        # print(sp)
        # print(len(sp))
        length = len(sp)
        if length == 1:
            path_sp = sp[0].split('/')
            # print(path_sp)
            filename = path_sp[4][:-4]
            # print(filename)
            old_img_path = img_path + filename + '.jpg'
            # print(old_img_path)
            new_img_path = r'C:\Users\GF\Desktop\VOCdevkit/imgs/'
            shutil.move(old_img_path, new_img_path)
            old_label_path = xml_path + filename + '.xml'
            new_label_path = r'C:\Users\GF\Desktop\VOCdevkit\labels/'
            shutil.move(old_label_path, new_label_path)
    else:
        print('处理完成')

