import os


file_dir=r'C:\Users\rina\Desktop\深度学习\网络图像的文本检测\icpr_mtwi_task2\sample_task2'
for root, dirs, files in os.walk(file_dir):
    print(files[0])
    print(1)
import os
import path
import glob
from PIL import Image
from PIL import ImageDraw
path = r"C:\Users\rina\Desktop\深度学习\网络图像的文本检测\yolov5\runs\detect\exp4\labels" #文件夹目录
path_1=r'C:\Users\rina\Desktop\深度学习\网络图像的文本检测\result'
path_img=r'C:\Users\rina\Desktop\深度学习\网络图像的文本检测\icpr_mtwi_task2\image_test'
files= os.listdir(path) #得到文件夹下的所有文件名称
s = []
count=0;

for file in files: #遍历文件夹
#for i in range(10):
        file_name, extension = os.path.splitext(os.path.basename(file))
        f = open(path+"/"+file,encoding='utf-8')
        iter_f = iter(f);
        txt_name = file_name+'.txt'
        img_name = file_name+'.jpg'
        img_fullname = os.path.join(path_img, img_name)
        img = Image.open(img_fullname)
        img_w,img_h=img.size
        f_revised = open(os.path.join(path_1, txt_name), mode='w', encoding='utf-8')
        bf =iter_f.read().splitlines()
        for idx in bf:
            rect = []
            spt = idx.split(' ')
            #print(spt)
            rect.append(float(spt[1]))
            rect.append(float(spt[2]))
            rect.append(float(spt[3]))
            rect.append(float(spt[4]))
            x = rect[0]
            y = rect[1]
            w1 = rect[2]
            h1 = rect[3]
            xmin = round(img_w * (x - w1 * 1.0 / 2.0),2)
            xmax = round(img_w * (x + w1 * 1.0 / 2.0),2)
            ymin = round(img_h * (y - h1 * 1.0 / 2.0),2)
            ymax = round(img_h * (y + h1 * 1.0 / 2.0),2)
            a=[]
            a.append(str(xmax))
            a.append(str(ymin))
            a.append(str(xmax))
            a.append(str(ymax))
            a.append(str(xmin))
            a.append(str(ymax))
            a.append(str(xmin))
            a.append(str(ymin))
            print(a)
            sep = ','
            s1 = sep.join(a)
            s1 = s1 + '\n'
            f_revised.write(s1)
