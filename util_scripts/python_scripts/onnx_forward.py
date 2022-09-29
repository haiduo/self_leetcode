''' 参考：https://zhuanlan.zhihu.com/p/110269410'''
import cv2
import onnxruntime as rt
import numpy as np
import sys
import torch
import matplotlib.pyplot as plt
import os
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"

from PIL import Image
from torchvision import transforms

session = rt.InferenceSession("mobilenet_v2.onnx")
input_name = session.get_inputs()[0].name
output_name = session.get_outputs()[0].name
input_shape = session.get_inputs()[0].shape

trans = transforms.Compose([
                     transforms.Resize((224, 224)),
                     transforms.ToTensor(),
                     transforms.Normalize((0.485, 0.456, 0.406), (0.229, 0.224, 0.225)),
                  ])
#使用Pillow的Image来打开图片
image = Image.open("ILSV.JPEG")
img1 = trans(image).unsqueeze(0).numpy()
res = session.run([output_name], {input_name: img1})
print(res)