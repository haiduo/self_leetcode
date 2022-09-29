import os
import numpy as np
import shutil


img_dir = r"C:\Users\haidu\Desktop\YOLOP\YoloP_data\dectection\images\train"
dest_img = r"C:\Users\haidu\Desktop\YOLOP\YoloP_data\dectection\images\val"
label_dir = r"C:\Users\haidu\Desktop\YOLOP\YoloP_data\dectection\label\train"
dest_laebl = r"C:\Users\haidu\Desktop\YOLOP\YoloP_data\dectection\label\val"
# road_dir = r"/YoloP_data/segmentation/train/road_label"
# dest_road = r"C:\Users\haidu\Desktop\YOLOP\YoloP_data\segmentation\value\road_label"

dir_imgs = os.listdir(img_dir)
dir_labels = os.listdir(label_dir)
result = set()
while len(result) < 580:
    rand_index = np.random.randint(len(dir_imgs))
    if rand_index not in result:
        shutil.move(os.path.join(img_dir, dir_imgs[rand_index]), dest_img) #将文件f1 移动到 f2目录下
        shutil.move(os.path.join(label_dir, dir_labels[rand_index]), dest_laebl) #将文件f1 移动到 f2目录下
        # shutil.move(os.path.join(road_dir, dir_files[rand_index]),dest_road) #将文件f1 移动到 f2目录下
        result.add(rand_index)      

    