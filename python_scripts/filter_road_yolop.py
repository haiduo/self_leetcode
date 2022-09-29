import os
import numpy as np
import shutil


img_dir = r"/YoloP_data/segmentation/train/image"
dest_img = r"C:\Users\haidu\Desktop\YOLOP\YoloP_data\segmentation\value\image"
lane_dir = r"/YoloP_data/segmentation/train/lane_label"
dest_lane = r"C:\Users\haidu\Desktop\YOLOP\YoloP_data\segmentation\value\lane_label"
road_dir = r"/YoloP_data/segmentation/train/road_label"
dest_road = r"C:\Users\haidu\Desktop\YOLOP\YoloP_data\segmentation\value\road_label"

dir_files = os.listdir(road_dir)
result = set()
while len(result) < 199:
    rand_index = np.random.randint(len(dir_files))
    if rand_index not in result:
        shutil.move(os.path.join(img_dir, dir_files[rand_index]),dest_img) #将文件f1 移动到 f2目录下
        shutil.move(os.path.join(lane_dir, dir_files[rand_index]),dest_lane) #将文件f1 移动到 f2目录下
        shutil.move(os.path.join(road_dir, dir_files[rand_index]),dest_road) #将文件f1 移动到 f2目录下
        result.add(rand_index)      

    