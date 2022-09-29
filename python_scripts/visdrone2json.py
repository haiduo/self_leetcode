import os
import cv2
from tqdm import tqdm
import json

def convert_to_cocodetection(dir, output_dir):
    train_dir = os.path.join(dir, "VisDrone2019-DET-train")
    val_dir = os.path.join(dir, "VisDrone2019-DET-val")
    train_annotations = os.path.join(train_dir, "annotations")
    val_annotations = os.path.join(val_dir, "annotations")
    train_images = os.path.join(train_dir, "images")
    val_images = os.path.join(val_dir, "images")
    id_num = 0

    categories = [{"id": 0, "name": "pedestrian"},
                  {"id": 1, "name": "people"},
                  {"id": 2, "name": "bicycle"},
                  {"id": 3, "name": "car"},
                  {"id": 4, "name": "van"},
                  {"id": 5, "name": "truck"},
                  {"id": 6, "name": "tricycle"},
                  {"id": 7, "name": "awning-tricycle"},
                  {"id": 8, "name": "bus"},
                  {"id": 9, "name": "motor"}
                  ]
    for mode in ["train", "val"]:


        print(f"start loading {mode} data...")
        if mode == "train":
            set = os.listdir(train_annotations)
            annotations_path = train_annotations
            images_path = train_images
        else:
            set = os.listdir(val_annotations)
            annotations_path = val_annotations
            images_path = val_images
        for i in tqdm(set):
            f = open(annotations_path + "/" + i, "r")
            name = i.replace(".txt", "")
            images = []
            annotations = []
            image = {}
            height, width = cv2.imread(images_path + "/" + name + ".jpg").shape[:2]
            file_name = name + ".jpg"
            image["file_name"] = file_name
            image["height"] = height
            image["width"] = width
            image["id"] = name
            images.append(image)
            annotation = {}
            dataset_dict = {}
            for line in f.readlines():
                line = line.replace("\n", "")
                if line.endswith(","):  # filter data
                    line = line.rstrip(",")
                line_list = [int(i) for i in line.split(",")]
                bbox_xywh = [line_list[0], line_list[1], line_list[2], line_list[3]]
                annotation["image_id"] = name
                annotation["score"] = line_list[4]
                annotation["bbox"] = bbox_xywh
                annotation["category_id"] = int(line_list[5])
                annotation["id"] = id_num
                annotation["iscrowd"] = 0
                annotation["segmentation"] = []
                annotation["area"] = bbox_xywh[2] * bbox_xywh[3]
                id_num += 1
                annotations.append(annotation)

            dataset_dict["images"] = images
            dataset_dict["annotations"] = annotations
            dataset_dict["categories"] = categories
            json_str = json.dumps(dataset_dict)
            with open(f'{output_dir}/{name}_coco.json', 'w') as json_file:
                json_file.write(json_str)

    print("json file write done...")


if __name__ == '__main__':
    convert_to_cocodetection(r"C:\Users\haidu\Desktop\temp\VisDrone2019-DET",
                             r"C:\Users\haidu\Desktop\temp\VisDrone2019-DET_resize")