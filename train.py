import warnings
warnings.filterwarnings('ignore')
from ultralytics import YOLO

# 训练参数官方详解链接：https://docs.ultralytics.com/modes/train/#resuming-interrupted-trainings:~:text=a%20training%20run.-,Train%20Settings,-The%20training%20settings

if __name__ == '__main__':
    model = YOLO('ultralytics/cfg/models/v8/DFPD.yaml')
    # model = YOLO('runs/train3/v8n-siou/weights/last.pt')
    # model.load('yolov8n.pt') # loading pretrain weights
    model.train(data=r'D:\yolov5\DFPD\kitti.yaml',
                cache=False,
                imgsz=640,
                epochs=200,
                batch=16,
                close_mosaic=0,
                workers=4,
                # device='0',
                optimizer='SGD', # using SGD
                # patience=0, # close earlystop
                resume=True, # 断点续训,YOLO初始化时选择last.pt
                # amp=False, # close amp    m
                # fraction=0.2,
                project='runs/train',
                name='v8'
                     '',
                )