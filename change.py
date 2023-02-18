import os
import path
import glob
from PIL import Image
from PIL import ImageDraw
path = r"C:\Users\rina\Desktop\深度学习\网络图像的文本检测\txt_train" #文件夹目录
path_1=r'C:\Users\rina\Desktop\深度学习\网络图像的文本检测\新建文件夹\txt'
path_img=r'C:\Users\rina\Desktop\深度学习\网络图像的文本检测\新建文件夹\image'
files= os.listdir(path) #得到文件夹下的所有文件名称
s = []
count=0;
for file in files: #遍历文件夹
#for i in range(10):
    if not os.path.isdir(file): #判断是否是文件夹，不是文件夹才打开
        f = open(path+"/"+file,encoding='utf-8'); #打开文件
    iter_f = iter(f); #创建迭代器
    count += 1
    count_s = str(count)
    name="img_" + count_s
    count_s_txt = "img_" + count_s + ".txt"
    img_fullname = os.path.join(path_img, name + '.jpg')
    img=Image.open(img_fullname)
    img_w,img_h=img.size
    f_revised = open(os.path.join(path_1, count_s_txt), mode='w', encoding='utf-8')
    bf =iter_f.read().splitlines()
    for idx in bf:
        rect = []
        spt = idx.split(',')
        a =0
        rect.append(a)
        rect.append(float(spt[0]))
        rect.append(float(spt[1]))
        rect.append(float(spt[2]))
        rect.append(float(spt[3]))
        rect.append(float(spt[4]))
        rect.append(float(spt[5]))
        rect.append(float(spt[6]))
        rect.append(float(spt[7]))
        xmin=rect[1]
        xmax=rect[5]
        ymax=rect[4]
        ymin=rect[2]
        print(xmax,xmin,ymax,ymin)
        x = round((xmin + xmax) / (2.0 * img_w), 6)
        y = round((ymin + ymax) / (2.0 * img_h), 6)
        w1 = round((xmax - xmin) / (1.0 * img_w), 6)
        h1 = round((ymax - ymin) / (1.0 * img_h), 6)
        a=[]
        a.append(str(rect[0]))
        a.append(str(x))
        a.append(str(y))
        a.append(str(w1))
        a.append(str(h1))
        print(a)
        sep = ' '
        s1 = sep.join(a)
        s1 = s1 + '\n'
        f_revised.write(s1)
