import os
import torch

path1 = 'F:\data\铁皮误检原图/'
path = os.listdir(path1)
for img in path:
    if img.endswith('xml'):
        continue
    print(img)
    # old_name = path + img
    img1, end = img.split('.')
    # print(img1)
    new_name = img1 + '.jpg'
    # print(new_name)
    # print(old_name)
    print(type(img))
    os.rename(path1 + img, path1 + new_name)

