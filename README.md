# ICPR2018：网络图像的文本识别 / 网络图像的文本检测 

TODO：
-  数据初始化：运行rechangeTxtName.py 和 changeImageName.py 转换文件名称 ；运行 change2yolo.py 转化为yolo格式
-  调用python train.py --data ICPR.yaml --weights '' --cfg yolov5s.yaml --img 640 开始训练
-  调用 python detect.py --weights best.pt --source  --save-txt 进行预测
-  调用 change.py 转化为提交要求格式
 

