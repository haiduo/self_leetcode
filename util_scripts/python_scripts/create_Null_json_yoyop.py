import os
import json

json_file =r"C:\Users\haidu\Desktop\YOLOP\YoloP_data\dectection\label\train\0000001_02999_d_0000005.json"

dir_input = r"C:\Users\haidu\Desktop\YOLOP\YoloP_data\segmentation\image\val"
dir_output = r"C:\Users\haidu\Desktop\YOLOP\YoloP_data\segmentation\label\val"

dict_file = {}
files = os.listdir(dir_input)
for fname in files:
    out_file = os.path.join(os.path.abspath(dir_output), fname.replace('.png', '.json'))
    with open(json_file, "r+", encoding="utf-8") as f:
        js = json.load(f)
        dict_file =js
    with open(out_file, 'w') as r:
        json.dump(dict_file, r)


