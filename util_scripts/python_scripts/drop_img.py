import os

anno_dir = r"C:\Users\haidu\Desktop\highway_data\annotations"
img_dir = r"C:\Users\haidu\Desktop\highway_data\images"

anno_list = os.listdir(anno_dir)

img_list = os.listdir(img_dir)
img_set = set(img_list)
print("img_list:", len(img_list), "img_set:", len(img_set))

for anno in anno_list:
    img_anno = anno.replace(".xml", ".jpg")
    if img_anno not in img_set:
        print(anno)
        # os.remove(os.path.join(anno_dir, anno))

print("imgs:", len(os.listdir(img_dir)))
print("Finish delete!")

