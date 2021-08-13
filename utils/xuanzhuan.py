import os
from PIL import Image
import cv2

root_path = 'F:\data\铁皮误检原图/'
img_name = os.listdir(root_path)
try:
    for img in img_name:
        image_path = root_path + img
        ep_img = Image.open(image_path)
        ep_img = ep_img.transpose(2)
        # ep_img.show()
        ep_img.save(image_path)
except:
    print('输入的可能是文件夹')
