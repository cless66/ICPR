if os.path.exists(dstpath):
    shutil.rmtree(dstpath)  # delete output folder
os.makedirs(dstpath)  # make new output folder
filelist = util.GetFileFromThisRootDir(txtpath)  # fileist=['/.../P0005.txt', ..., /.../P000?.txt]
for fullname in filelist:  # fullname='/.../P000?.txt'
    objects = util.parse_dota_poly(fullname)
    '''
    objects =
    [{'name': 'ship', 
      'difficult': '1', 
      'poly': [(1054.0, 1028.0), (1063.0, 1011.0), (1111.0, 1040.0), (1112.0, 1062.0)], 
      'area': 1159.5
      },
      ...
    ]
    '''
    name = os.path.splitext(os.path.basename(fullname))[0]  # name='P000?'
    img_fullname = os.path.join(imgpath, name + '.png')  # img_fullname='/.../P000?.png'
    img = Image.open(img_fullname)
    img_w, img_h = img.size
    # print img_w,img_h
    with open(os.path.join(dstpath, name + '.txt'), 'w') as f_out:
        for obj in objects:
            poly = obj['poly']  # poly=[(x1,y1),(x2,y2),(x3,y3),(x4,y4)]
            bbox = np.array(util.dots4ToRecC(poly, img_w, img_h))  # bbox=[x y w h]
            if (sum(bbox <= 0) + sum(bbox >= 1)) >= 1:  # 若bbox中有<=0或>= 1的元素则将该box排除
                continue
            if (obj['name'] in extractclassname):
                id = extractclassname.index(obj['name'])  # id=类名的索引 比如'plane'对应id=0
            else:
                continue
            outline = str(id) + ' ' + ' '.join(list(map(str, bbox)))  # outline='id x y w h'
            f_out.write(outline + '\n')  # 写入txt文件中并加上换行符号 \n