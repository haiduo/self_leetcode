import os
import cv2
from tqdm import tqdm
import numpy as np
import json

categories = {0: "pedestrian", 1: "people", 2: "bicycle", 3: "car", 4: "van",
              5:  "truck", 6:  "tricycle", 7:  "awning-tricycle", 8:  "bus",
              9:  "motor"}
    
in_dir = r"C:\Users\haidu\Desktop\temp\VisDrone2019-DET"
out_dir = r"C:\Users\haidu\Desktop\temp\VisDrone2019-DET_resize"

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


def convert_annotation(img_id, txt_id, outdir_json):
    assert os.path.exists(txt_id)
    (_, name) = os.path.split(txt_id)  # 分割文件目录/文件名和后缀
    (_, name_extension) = os.path.splitext(txt_id)
    name = name.split(name_extension)[0]
    json_file = os.path.join(outdir_json, name+'.json')

    in_file = open(txt_id, encoding="utf-8")
    img = cv2.imread(img_id)
    h , w, _ = img.shape
    rate_x = 1280.0 / w
    rate_y = 720.0 / h

    result_boxs = []
    # 逐行读取
    for line in in_file:
        lst = line.strip().split(',')
        if int(lst[5])-1 in range(0, 10):
            box = (float(lst[0]), float(lst[1]), float(lst[2]), float(lst[3]))
            #xywh ---> x1y1x2y2 并 判断标注越界修正
            x1 = np.clip(box[0] - box[2] // 2.0, 0, w)
            x2 = np.clip(box[0] + box[2] // 2.0, 0, w)
            y1 = np.clip(box[1] - box[3] // 2.0, 0, h)
            y2 = np.clip(box[1] + box[3] // 2.0, 0, h)

            box_ = (x1* rate_x, y1* rate_y, x2* rate_x ,y2* rate_y)
        
            # 判断压缩后的标框是否合理
            if box_[2]-box_[0] <=2 or box_[3]-box_[1]<=2:
                continue
            #将标定框写进字典，方便后面写入json文件  
            item = {
                "category": categories[int(lst[5])-1],
                "id": int(lst[5])-1,
                "box2d": {
                    "x1": float(box_[0]),
                    "y1": float(box_[1]),
                    "x2": float(box_[2]),
                    "y2": float(box_[3])
                }
            } 
            result_boxs.append(item)
    gen_json(result_boxs, name, json_file) #生成json文件
    in_file.close()



def ResizeImage(img, dest_image):
    img1 = cv2.imread(img)
    img2 = cv2.resize(img1, (1280, 720))
    cv2.imwrite(dest_image, img2)

if __name__ == '__main__':
    for mode in ["train", "val"]:
        print(f"start loading {mode} data...")
        if mode == "train": 
            set_images = os.listdir(os.path.join(in_dir,mode,"images"))
            set_annotations = os.listdir(os.path.join(in_dir,mode,"annotations"))          
            images_path = os.path.join(in_dir,mode,"images")
            annotations_path = os.path.join(in_dir,mode,"annotations")
        else:            
            set_images = os.listdir(os.path.join(in_dir,mode,"images"))
            set_annotations = os.listdir(os.path.join(in_dir,mode,"annotations"))
            images_path = os.path.join(in_dir,mode,"images")
            annotations_path = os.path.join(in_dir,mode,"annotations")
            
        for img, txt in zip(set_images, set_annotations):
            ResizeImage(os.path.join(images_path,img), os.path.join(out_dir,mode,'images',img))
            convert_annotation(os.path.join(images_path,img), os.path.join(annotations_path,txt), os.path.join(out_dir,mode,'annotations'))

    print("json file write done...")
                             
