import os
import json
import shutil

label_file =r"C:\Users\haidu\Desktop\YOLOP\YoloP_data\segmentation\lane_label\train\guangzhou_resize_000010.png"

dir_input = r"C:\Users\haidu\Desktop\YOLOP\YoloP_data\dectection\images\train"
dir_output = r"C:\Users\haidu\Desktop\YOLOP\YoloP_data\dectection\lane_label\train"

dict_file = {}
files = os.listdir(dir_input)
for fname in files:
    (_, name) = os.path.split(fname)  # 分割文件目录/文件名和后缀
    (_, name_extension) = os.path.splitext(fname)
    name = name.split(name_extension)[0]
    file_path = os.path.join(dir_output, name+'.png')

    shutil.copyfile(label_file, file_path)
    
