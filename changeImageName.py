'''
#input
image_dir = "./image_test/*.jpg"                         #orignial images name(perhaps abnormal)
#output
imgs_save_dir = "./image_test_change"                    #renamed images(e.g. img_1.jpg)
'''

import os
import path
import glob
from PIL import Image  
from PIL import ImageDraw
import os
import pandas as pd
from PIL import Image, ImageDraw
import csv

imgs_save_dir = r"C:\Users\rina\Desktop\深度学习\网络图像的文本检测\新建文件夹\image"

image_dir = r"C:\Users\rina\Desktop\深度学习\网络图像的文本检测\image_train/*.jpg"
imgDirs = []
imgLists = glob.glob(image_dir)

for item in imgLists:
    imgDirs.append(item)


count = 0;
for img_dir in imgDirs:

    img = Image.open(img_dir)
    count += 1
    count_s = str(count)
    count_s_img = "img_" + count_s + ".jpg"
    '''
    for idx, row in text_point.iterrows():

        point = row.loc[range(8)].tolist()  # 依次读取八个点的数据
        x = [point[i] for i in [0, 2, 4, 6]]
        y = [point[i] for i in [1, 3, 5, 7]]
        point = [(a, b) for a, b in zip(x, y)]
        draw.polygon(point, outline=(0, 128, 255))  # 画多边形

        x_min, x_max = min(x), max(x)
        y_min, y_max = min(y), max(y)
        draw.rectangle((x_min, y_min, x_max, y_max), outline=(0, 0, 255))
    '''
    if img.mode == "P" or img.mode == "RGBA":
        img = img.convert('RGB')


    name="img_" + str(count) + ".jpg"

    img.save(imgs_save_dir + '\\'+ name)
