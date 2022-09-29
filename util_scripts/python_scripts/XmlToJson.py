import xml.etree.ElementTree as ET
import os
import cv2
from tqdm import tqdm
import numpy as np
import json

classes = ['Pedestrian', 'Car', 'Bicycle', 'Truck', 'Bus', 'DangerCar', 'Van', 'Construction']  # 自己训练的类别

def gen_json(result_boxs, name, json_file):   
    items = {
        "name": name,
        "frames": [
            {
                "objects": result_boxs
                
            }
        ]
    }
    with open(json_file, 'w') as dump_f:
        json.dump(items, dump_f)

def ResizeImage(img, dest_image):
    img1 = cv2.imread(img)
    img2 = cv2.resize(img1, (1280, 720))
    cv2.imwrite(dest_image, img2)


in_anno_dir = r"C:\Users\haidu\Desktop\highway_data\annotations"
out_anno_dir =r"C:\Users\haidu\Desktop\highway_data\annotations_json"
in_img_dir = r"C:\Users\haidu\Desktop\highway_data\images"
out_img_dir = r"C:\Users\haidu\Desktop\highway_data\images_json"

in_images = os.listdir(in_img_dir)
in_annotations = os.listdir(in_anno_dir)

for img, anno in zip(tqdm(in_images), in_annotations):
    in_anno = open(os.path.join(in_anno_dir, anno),'r', encoding='utf-8')
    tree = ET.parse(in_anno)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    img_file = cv2.imread(os.path.join(in_img_dir, img))
    h , w, _ = img_file.shape
    rate_x = 1280.0 / w
    rate_y = 720.0 / h
    # ResizeImage(os.path.join(in_img_dir, img), os.path.join(out_img_dir, img))

    json_file = os.path.join(out_anno_dir, anno.replace(".xml", ".json"))
    name = anno.split('.')[0]
    result_boxs = []
    for obj in root.iter('object'):
        cls = obj.find('name').text
        cls = cls.title()
        if cls == 'Dangercar':
            cls = 'DangerCar'
        if cls == 'Pedestrain' or cls == 'Pedetrian':
            cls = 'Pedestrian'
        if cls not in classes:
            print("error_classes:", anno," ", cls)
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        #x1y1x2y2 
        box = [float(xmlbox.find('xmin').text), float(xmlbox.find('ymin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymax').text)]
         # 标注越界修正
        np.clip(box[0], 0, w)
        np.clip(box[1], 0, h)
        np.clip(box[2], 0, w)
        np.clip(box[3], 0, h)
        # 判断压缩后的标框是否合理
        box_ = (box[0]* rate_x, box[1]* rate_y, box[2]* rate_x ,box[3]* rate_y)
        if box_[2]-box_[0] <=2 or box_[3]-box_[1]<=2:
            continue
        #将标定框写进字典，方便后面写入json文件  
        item = {
            "category": cls,
            "id": int(cls_id),
            "box2d": {
                "x1": float(box_[0]),
                "y1": float(box_[1]),
                "x2": float(box_[2]),
                "y2": float(box_[3])
            }
        } 
        result_boxs.append(item)
    gen_json(result_boxs, name, json_file) #生成json文件
    in_anno.close()

print('Finish!')
        
